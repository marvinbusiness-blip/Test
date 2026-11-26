#!/usr/bin/env python3
"""Rechner für die Immobilienbewertung (Standardbibliothek, kein Netzwerk).

Rechnet aus den Eckdaten einer Immobilie die Kennzahlen, die für Kaufpreisprüfung
und Kapitalanlage zählen, und gibt sie als Markdown aus. Jede Zahl kommt aus den
übergebenen Argumenten; fehlt etwas, wird der Abschnitt weggelassen statt geraten.

Beispiele:
  # Kapitalanlage-Wohnung
  python3 rechner.py --kaufpreis 129000 --wohnflaeche 55 --bundesland NW \
      --kaltmiete-monat 450 --nicht-umlagefaehig-monat 90 \
      --eigenkapital 30000 --zins 3.8 --tilgung 2 --grenzsteuersatz 35

  # Eigennutzung Haus, Vergleich mit Miete
  python3 rechner.py --kaufpreis 465000 --wohnflaeche 125 --bundesland NW --makler 3.57 \
      --eigenkapital 90000 --zins 3.7 --tilgung 2 --instandhaltung-monat 250 \
      --vergleichsmiete-qm 11.5

  # Mehrfamilienhaus mit vereinfachtem Ertragswert
  python3 rechner.py --kaufpreis 690000 --wohnflaeche 420 --bundesland NW \
      --kaltmiete-jahr 31200 --einheiten 6 --bodenwert 180000 \
      --liegenschaftszins 3.0 --restnutzungsdauer 30
"""

import argparse
import sys

# Nur Sätze, die beim Schreiben des Skills geprüft waren (Stand 2026). Für alle
# anderen Länder den aktuellen Satz nachschlagen und mit --grest übergeben.
GREST = {"NW": 6.5, "BY": 3.5}

# Voreinstellungen für Bewirtschaftungskosten nach ImmoWertV Anlage 3 (Größenordnung,
# jährlich indexiert; aktuellen Wert prüfen und bei Bedarf per Argument überschreiben).
VERWALTUNG_JE_WE = 360.0      # € pro Wohnung und Jahr
INSTANDHALTUNG_QM = 14.0      # € pro m² Wohnfläche und Jahr


def eur(x, nachkomma=0):
    s = f"{x:,.{nachkomma}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".") + " €"


def pct(x, nachkomma=1):
    return f"{x * 100:.{nachkomma}f} %".replace(".", ",")


def zahl(x, nachkomma=1):
    return f"{x:.{nachkomma}f}".replace(".", ",")


def vervielfaeltiger(lz, n):
    """Barwertfaktor der Ertragswertmethode (ImmoWertV), lz als Dezimalzahl."""
    if lz <= 0:
        return float(n)
    q = 1 + lz
    return (q ** n - 1) / (q ** n * (q - 1))


def main(argv=None):
    p = argparse.ArgumentParser(description="Kennzahlen für Immobilienbewertung")
    p.add_argument("--kaufpreis", type=float, required=True)
    p.add_argument("--wohnflaeche", type=float, required=True, help="m²")
    p.add_argument("--bundesland", default="", help="Kürzel, z. B. NW, BY")
    p.add_argument("--grest", type=float, help="Grunderwerbsteuer in %% (überschreibt Bundesland)")
    p.add_argument("--notar", type=float, default=2.0, help="Notar + Grundbuch in %% (Standard 2,0)")
    p.add_argument("--makler", type=float, default=0.0, help="Käuferprovision in %% inkl. MwSt.")
    p.add_argument("--renovierung", type=float, default=0.0, help="sofort nötige Investitionen in €")
    # Miete und Kosten
    p.add_argument("--kaltmiete-monat", type=float, help="Ist-Nettokaltmiete pro Monat (gesamt)")
    p.add_argument("--kaltmiete-jahr", type=float, help="Ist-Nettokaltmiete pro Jahr (gesamt)")
    p.add_argument("--nicht-umlagefaehig-monat", type=float, default=0.0,
                   help="nicht umlagefähige Kosten pro Monat (Verwaltung, Rücklage ...)")
    p.add_argument("--mietausfall", type=float, default=2.0, help="Mietausfallwagnis in %% der Kaltmiete")
    p.add_argument("--hausgeld-monat", type=float, default=0.0, help="Hausgeld gesamt (Eigennutzung ETW)")
    p.add_argument("--instandhaltung-monat", type=float, default=0.0,
                   help="eigene Instandhaltungsrücklage pro Monat (Haus, Eigennutzung)")
    p.add_argument("--vergleichsmiete-qm", type=float, help="ortsübliche Kaltmiete €/m² (Eigennutzung)")
    # Finanzierung
    p.add_argument("--eigenkapital", type=float)
    p.add_argument("--zins", type=float, help="Sollzins in %%")
    p.add_argument("--tilgung", type=float, default=2.0, help="anfängliche Tilgung in %%")
    # Steuer (vereinfacht)
    p.add_argument("--grenzsteuersatz", type=float, help="in %%, für Steuereffekt Kapitalanlage")
    p.add_argument("--gebaeudeanteil", type=float, default=70.0, help="Gebäudeanteil am Kaufpreis in %%")
    p.add_argument("--afa", type=float, default=2.0, help="AfA-Satz in %%")
    # Ertragswert
    p.add_argument("--einheiten", type=int, default=1, help="Zahl der Wohnungen")
    p.add_argument("--bodenwert", type=float)
    p.add_argument("--liegenschaftszins", type=float, help="in %%")
    p.add_argument("--restnutzungsdauer", type=int)
    p.add_argument("--bewirtschaftung-prozent", type=float,
                   help="Bewirtschaftungskosten in %% des Rohertrags (statt Detailrechnung)")
    a = p.parse_args(argv)

    out = []
    kp, wf = a.kaufpreis, a.wohnflaeche

    # --- Kaufnebenkosten ---
    grest = a.grest if a.grest is not None else GREST.get(a.bundesland.upper())
    if grest is None:
        out.append("> Grunderwerbsteuer unbekannt: aktuellen Satz des Bundeslands nachschlagen und mit `--grest` übergeben. Hier mit 0 gerechnet.")
        grest = 0.0
    nk_grest, nk_notar, nk_makler = kp * grest / 100, kp * a.notar / 100, kp * a.makler / 100
    nk = nk_grest + nk_notar + nk_makler
    gesamt = kp + nk + a.renovierung

    out.append("### Kauf")
    out.append("| Posten | Betrag |")
    out.append("|---|---:|")
    out.append(f"| Kaufpreis | {eur(kp)} |")
    out.append(f"| Preis pro m² | {eur(kp / wf)} |")
    out.append(f"| Grunderwerbsteuer ({zahl(grest)} %) | {eur(nk_grest)} |")
    out.append(f"| Notar + Grundbuch ({zahl(a.notar)} %) | {eur(nk_notar)} |")
    if a.makler:
        out.append(f"| Makler ({zahl(a.makler, 2)} %) | {eur(nk_makler)} |")
    if a.renovierung:
        out.append(f"| Sofortige Investitionen | {eur(a.renovierung)} |")
    out.append(f"| **Gesamtinvestition** | **{eur(gesamt)}** |")
    out.append(f"| Gesamtinvestition pro m² | {eur(gesamt / wf)} |")

    # --- Miete / Rendite ---
    jm = a.kaltmiete_jahr if a.kaltmiete_jahr is not None else (
        a.kaltmiete_monat * 12 if a.kaltmiete_monat is not None else None)
    nu_jahr = a.nicht_umlagefaehig_monat * 12
    if jm:
        ausfall = jm * a.mietausfall / 100
        rein = jm - nu_jahr - ausfall
        out.append("\n### Miete und Rendite")
        out.append("| Kennzahl | Wert |")
        out.append("|---|---:|")
        out.append(f"| Nettokaltmiete pro Jahr | {eur(jm)} |")
        out.append(f"| Miete pro m² und Monat | {eur(jm / 12 / wf, 2)} |")
        out.append(f"| Kaufpreisfaktor (Kaufpreis / Jahreskaltmiete) | {zahl(kp / jm)} |")
        out.append(f"| Bruttomietrendite (Miete / Kaufpreis) | {pct(jm / kp, 2)} |")
        out.append(f"| Nicht umlagefähige Kosten pro Jahr | {eur(nu_jahr)} |")
        out.append(f"| Mietausfallwagnis ({zahl(a.mietausfall)} %) | {eur(ausfall)} |")
        out.append(f"| Nettomietrendite (nach Kosten / Gesamtinvestition) | {pct(rein / gesamt, 2)} |")

    # --- Finanzierung ---
    if a.eigenkapital is not None and a.zins is not None:
        darlehen = max(gesamt - a.eigenkapital, 0)
        zinsen_j = darlehen * a.zins / 100
        tilg_j = darlehen * a.tilgung / 100
        rate_m = (zinsen_j + tilg_j) / 12
        out.append("\n### Finanzierung (Jahr 1)")
        out.append("| Kennzahl | Wert |")
        out.append("|---|---:|")
        out.append(f"| Eigenkapital | {eur(a.eigenkapital)} ({pct(a.eigenkapital / gesamt)} der Gesamtinvestition) |")
        if a.eigenkapital < nk:
            out.append(f"| Hinweis | Eigenkapital deckt die Nebenkosten ({eur(nk)}) nicht: Vollfinanzierung, meist schlechtere Zinsen |")
        out.append(f"| Darlehen | {eur(darlehen)} |")
        out.append(f"| Rate pro Monat ({zahl(a.zins, 2)} % Zins + {zahl(a.tilgung, 2)} % Tilgung) | {eur(rate_m)} |")
        out.append(f"| davon Zinsen / Tilgung pro Monat | {eur(zinsen_j / 12)} / {eur(tilg_j / 12)} |")

        if jm:
            ausfall = jm * a.mietausfall / 100
            cf_m = (jm - nu_jahr - ausfall) / 12 - rate_m
            out.append(f"| **Cashflow vor Steuern pro Monat** | **{eur(cf_m)}** |")
            # Höchster Kaufpreis, bei dem der Cashflow vor Steuern bei gleicher Finanzierung >= 0 ist
            annu = (a.zins + a.tilgung) / 100
            nk_quote = (grest + a.notar + a.makler) / 100
            if annu > 0:
                max_kp = ((jm - nu_jahr - ausfall) / annu + a.eigenkapital - a.renovierung) / (1 + nk_quote)
                out.append(f"| **Kaufpreis für Cashflow ≥ 0 (gleiche Finanzierung)** | **{eur(max_kp)}** ({pct(max_kp / kp - 1, 0)} ggü. Angebot) |")
            out.append(f"| Cashflow vor Steuern + Tilgung (Vermögensaufbau) pro Monat | {eur(cf_m + tilg_j / 12)} |")
            if a.eigenkapital > 0:
                ekr = (cf_m * 12 + tilg_j) / a.eigenkapital
                out.append(f"| Eigenkapitalrendite Jahr 1 (Cashflow + Tilgung, ohne Wertsteigerung) | {pct(ekr)} |")
            if a.grenzsteuersatz is not None:
                afa_basis = (kp + nk) * a.gebaeudeanteil / 100
                afa_j = afa_basis * a.afa / 100
                ergebnis = jm - nu_jahr - zinsen_j - afa_j
                steuer_j = ergebnis * a.grenzsteuersatz / 100
                out.append(f"| Steuerliches Ergebnis pro Jahr (Miete − Kosten − Zinsen − AfA {zahl(a.afa)} % auf {zahl(a.gebaeudeanteil, 0)} % Gebäudeanteil) | {eur(ergebnis)} |")
                out.append(f"| Steuer pro Monat bei {zahl(a.grenzsteuersatz, 0)} % (negativ = Ersparnis) | {eur(steuer_j / 12)} |")
                out.append(f"| **Cashflow nach Steuern pro Monat** | **{eur(cf_m - steuer_j / 12)}** |")
        else:
            belast = rate_m + a.hausgeld_monat + a.instandhaltung_monat
            out.append(f"| Monatliche Belastung (Rate + Hausgeld + Rücklage) | **{eur(belast)}** |")
            if a.vergleichsmiete_qm:
                miete_m = a.vergleichsmiete_qm * wf
                out.append(f"| Vergleich: Kaltmiete für dieselbe Fläche | {eur(miete_m)} pro Monat |")
                out.append(f"| Kaufpreis in Jahreskaltmieten | {zahl(kp / (miete_m * 12))} |")
                out.append(f"| Zinsen + Hausgeld/Rücklage (Kosten ohne Tilgung) vs. Miete | {eur(zinsen_j / 12 + a.hausgeld_monat + a.instandhaltung_monat)} vs. {eur(miete_m)} |")
    elif a.vergleichsmiete_qm:
        miete_m = a.vergleichsmiete_qm * wf
        out.append("\n### Vergleich mit Miete")
        out.append(f"- Ortsübliche Kaltmiete für die Fläche: {eur(miete_m)} pro Monat")
        out.append(f"- Kaufpreis in Jahreskaltmieten: {zahl(kp / (miete_m * 12))}")

    # --- Ertragswert (vereinfacht) ---
    if jm and a.bodenwert is not None and a.liegenschaftszins is not None and a.restnutzungsdauer:
        if a.bewirtschaftung_prozent is not None:
            bwk = jm * a.bewirtschaftung_prozent / 100
            bwk_txt = f"{zahl(a.bewirtschaftung_prozent)} % des Rohertrags"
        else:
            bwk = VERWALTUNG_JE_WE * a.einheiten + INSTANDHALTUNG_QM * wf + jm * a.mietausfall / 100
            bwk_txt = (f"Verwaltung {eur(VERWALTUNG_JE_WE)} × {a.einheiten} WE + Instandhaltung "
                       f"{eur(INSTANDHALTUNG_QM)}/m² + Mietausfall {zahl(a.mietausfall)} %")
        reinertrag = jm - bwk
        out.append("\n### Ertragswert (vereinfacht nach ImmoWertV)")
        out.append(f"Rohertrag {eur(jm)} − Bewirtschaftungskosten {eur(bwk)} ({bwk_txt}) = Reinertrag {eur(reinertrag)}; "
                   f"Bodenwert {eur(a.bodenwert)}; Restnutzungsdauer {a.restnutzungsdauer} Jahre.")
        out.append("")
        out.append("| Liegenschaftszins | Vervielfältiger | Ertragswert | Kaufpreis / Ertragswert |")
        out.append("|---:|---:|---:|---:|")
        for d in (-0.5, 0.0, 0.5):
            lz = (a.liegenschaftszins + d) / 100
            if lz <= 0:
                continue
            v = vervielfaeltiger(lz, a.restnutzungsdauer)
            ew = (reinertrag - a.bodenwert * lz) * v + a.bodenwert
            mark = " **(Basis)**" if d == 0 else ""
            out.append(f"| {pct(lz, 2)}{mark} | {zahl(v, 2)} | {eur(ew)} | {pct(kp / ew, 0)} |")

    print("\n".join(out))


if __name__ == "__main__":
    sys.exit(main())

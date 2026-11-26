---
name: immobilienbewertung
description: Bewertet Eigentumswohnungen, Einfamilienhäuser (auch Doppel- und Reihenhäuser) und Mehrfamilienhäuser in Deutschland, vor allem am Niederrhein. Prüft, ob ein Kaufpreis fair ist (Vergleichswert, bei Mehrfamilienhäusern Ertragswert), und ob sich ein Objekt als Kapitalanlage lohnt (Kaufpreisfaktor, Rendite, Cashflow bei Vollfinanzierung, Kaufpreis für positiven Cashflow). Recherchiert Vergleichspreise, Bodenrichtwerte, Mietspiegel und Bauzinsen und gibt ein kurzes Urteil mit Ampel im Chat. Nutze diesen Skill immer, wenn der Nutzer einen Link zu einer Immobilienanzeige, ein Exposé oder Eckdaten einer Wohnung oder eines Hauses schickt und wissen will, ob der Preis passt, was das Objekt wert ist, ob sich der Kauf oder die Vermietung lohnt, wie viel Cashflow oder Rendite drin ist, oder wie viel er bieten sollte, auch wenn er nicht ausdrücklich „bewerten“ sagt (z. B. „Was hältst du von der Wohnung?“, „Lohnt sich das?“, „Ist das zu teuer?“).
---

# Immobilienbewertung

Ziel: eine ehrliche, schnelle Einschätzung, ob ein konkretes Objekt den Preis wert ist und ob es als Kapitalanlage trägt, kurz im Chat, mit nachvollziehbaren Zahlen. Der Nutzer will damit entscheiden, ob er ein Objekt besichtigt, wie viel er bietet oder ob er es lässt. Eine schöne, aber falsche Zahl schadet ihm mehr als eine ehrliche Spanne.

Lies zuerst `references/profil.md`. Dort stehen seine Vorlieben: Region, Standardfinanzierung, K.-o.-Kriterien, Urteilsstil. Sie gelten, solange er im Gespräch nichts anderes sagt. `references/methoden.md` ist das Nachschlagewerk für Verfahren, Faustregeln und Prüfpunkte. Lies dort die Abschnitte, die zum Objekt passen.

## Ablauf

### 1. Objektdaten holen
- **Link:** Versuche, die Seite zu lesen (WebFetch oder, falls nicht vorhanden, der `web-fetch`-Agent). Immobilienportale blockieren automatisierte Abrufe oft, und manche Umgebungen haben keinen freien Netzzugang. Klappt es nicht, sag das in einem Satz und bitte um einen Screenshot des Exposés oder die Eckdaten. Rate nichts aus der URL zusammen.
- **Screenshot oder PDF:** Lies alle Seiten. Achte auf das Kleingedruckte: Hausgeld-Aufteilung, Erbbaurecht, vermietet/frei, Baujahr der Heizung, Energieausweis.
- **Wichtige Eckdaten:** Kaufpreis, Wohnfläche, Ort und Straße/Stadtteil, Baujahr, Zustand und letzte Modernisierungen, Heizung und Energiekennwert. Bei ETW zusätzlich Hausgeld (davon nicht umlagefähig), Etage, Balkon, Stellplatz. Bei Häusern die Grundstücksfläche. Bei Vermietung die Ist-Kaltmiete (bei MFH die Mietliste). Dazu die Maklerprovision.

### 2. Zweck klären
Kapitalanlage oder Eigennutzung? Meist ergibt es sich (vermietet, Mietliste → Anlage). Wenn nicht klar, frag kurz. Wenn beides denkbar ist, rechne den Hauptzweck und nenne den anderen in einem Satz.

### 3. Fehlende Angaben
- Angaben, die das Urteil kippen können (Miete, nicht umlagefähiges Hausgeld, größere Mängel, Sonderumlagen): **kurz nachfragen, höchstens drei Fragen auf einmal**.
- Alles andere: plausibel annehmen und in der Antwort als Annahme kennzeichnen.
- Wenn der Nutzer sagt „rechne einfach“, rechne mit markierten Annahmen.

### 4. Marktdaten recherchieren
Immer per Websuche, mit Quelle und Datum (Details in `references/methoden.md`, Abschnitt 9):
- **Vergleichspreis €/m²:** Immobilienrichtwerte bzw. Grundstücksmarktbericht des Gutachterausschusses (in NRW: BORIS-NRW), dazu Angebotspreise aus Portalen bzw. Preisatlanten. Angebotspreise liegen meist über echten Kaufpreisen.
- **Bodenrichtwert** bei Häusern und MFH (BORIS).
- **Vergleichsmiete:** Mietspiegel der Stadt, sonst Angebotsmieten.
- **Bauzins** für 10 Jahre Zinsbindung, beim Standardfall Vollfinanzierung mit dem üblichen Aufschlag oder diesen klar benennen.
- **Liegenschaftszins** bei MFH aus dem Grundstücksmarktbericht.

Findest du eine Zahl nicht, sag das und nimm die Spanne aus `methoden.md` als markierte Annahme. **Erfinde nie Marktdaten, Zinsen oder Quellen.** Eine falsche Zahl mit Quellenanschein ist das Schlimmste, was dieser Skill tun kann.

### 5. Rechnen mit `scripts/rechner.py`
Rechne nicht im Kopf. Das Skript liefert Kaufnebenkosten, €/m², Kaufpreisfaktor, Renditen, Finanzierung, Cashflow vor und nach Steuern, den **Kaufpreis für Cashflow ≥ 0** und bei MFH den vereinfachten Ertragswert mit Sensitivität. Alle Optionen zeigt `python3 scripts/rechner.py --help`.

```bash
# Kapitalanlage-Wohnung, Standard laut Profil: Vollfinanzierung, 2 % Tilgung, 35 % Grenzsteuersatz
python3 scripts/rechner.py --kaufpreis 149000 --wohnflaeche 62 --bundesland NW \
  --kaltmiete-monat 520 --nicht-umlagefaehig-monat 95 \
  --eigenkapital 0 --zins 4.1 --tilgung 2 --grenzsteuersatz 35

# Mehrfamilienhaus mit Ertragswert (Bodenwert = Bodenrichtwert × Fläche)
python3 scripts/rechner.py --kaufpreis 690000 --wohnflaeche 420 --bundesland NW \
  --kaltmiete-jahr 31200 --einheiten 6 --bodenwert 180000 --liegenschaftszins 3.0 \
  --restnutzungsdauer 30 --eigenkapital 0 --zins 4.1 --tilgung 2 --grenzsteuersatz 35

# Eigennutzung Haus: Belastung und Vergleich mit Miete
python3 scripts/rechner.py --kaufpreis 465000 --wohnflaeche 125 --bundesland NW --makler 3.57 \
  --eigenkapital 0 --zins 4.1 --tilgung 2 --instandhaltung-monat 300 --vergleichsmiete-qm 11.0
```

- Bekannte Mängel bzw. Sanierungskosten (Heizung, Dach) als `--renovierung` mitgeben, bei kleineren Arbeiten grob schätzen.
- **Chancen-Szenario:** Liegt die Ist-Miete unter dem Mietspiegel, ein zweites Mal mit der erreichbaren Miete rechnen. Dabei Kappungsgrenze und Mietpreisbremse beachten.
- Für den Vergleichswert gibt es kein Skript: Spanne aus den recherchierten €/m² bilden, nach Baujahr, Zustand, Lage und Ausstattung anpassen (`methoden.md`, Abschnitt 1).

### 6. Urteilen
**Ampel:**
- 🟢 **Gut:** Preis im oder unter dem Marktwert. Bei Kapitalanlage Cashflow ≥ 0 oder ein realistisches Potenzial schließt die Lücke. Kein K.-o.-Kriterium.
- 🟡 **Verhandeln / genauer prüfen:** Preis leicht über Markt, oder der Cashflow-Zielpreis liegt bis etwa 15 % unter dem Angebot, oder wichtige Unterlagen fehlen noch. Kein K.-o.
- 🔴 **Eher lassen:** K.-o.-Kriterium aus dem Profil erfüllt (Sanierungsstau/Sonderumlage, schlechte Mikrolage), oder deutlich über Markt, oder positiver Cashflow nur mit großem Preisnachlass und ohne Potenzial.

Urteile **chancenorientiert**, wie im Profil gewünscht. Zeig Potenziale mit Zahl, aber immer neben dem Basisszenario mit heutigen Werten. K.-o. bleibt K.-o.

Gleiche das Objekt mit seinen Wünschen ab: ETW mit Balkon und Stellplatz, Haus mit Garten bzw. Grundstück. Fehlt etwas, nenne es als Minuspunkt. Wenn alte Elektrik ein Thema ist, nenn als Plus, dass er die selbst machen kann.

## Ausgabe: kurz im Chat

Halte dich an dieses Format. Knapp, keine langen Tabellen. Zahlen auf sinnvolle Stellen runden.

```
**[Objekt in einem Satz: Art, Ort, m², Baujahr, Preis]** · Zweck: [Kapitalanlage/Eigennutzung]

**Urteil: [🟢/🟡/🔴] [ein Satz, warum]**

**Wert:** Markt ca. [X–Y] € ([Methode], [Quelle, Datum]) · Angebot [Z] € → [unter/im/über] Markt um ca. [N] %
**Zielpreis:** [Kapitalanlage: Cashflow ≥ 0 bis ca. … €] [Eigennutzung: fairer Verhandlungsrahmen …]

**Zahlen** ([Finanzierung], Zins [..] % laut [Quelle, Datum])
- Gesamtinvestition inkl. Nebenkosten: …
- [Kapitalanlage] Kaufpreisfaktor … · Bruttorendite … · Cashflow … vor / … nach Steuern pro Monat
- [Eigennutzung] Belastung … pro Monat · vergleichbare Miete … · Kaufpreis = … Jahresmieten
- [MFH] Ertragswert ca. … (Liegenschaftszins …–… %)

**Chancen:** [1–2 Punkte mit Zahl]
**Risiken / K.-o.-Check:** [2–3 Punkte, inkl. Abgleich Balkon/Stellplatz/Garten]
**Annahmen & offen:** [was angenommen wurde, was vor einem Gebot zu klären ist]

_Schätzung auf Basis öffentlicher Daten, kein Verkehrswertgutachten und keine Anlage- oder Steuerberatung._
```

Will der Nutzer Details, zeig die Tabellen aus dem Rechner. Ohne Nachfrage nicht.

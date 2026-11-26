---
name: immo
description: Bewertet Eigentumswohnungen, Einfamilien-, Doppel-, Reihen- und Mehrfamilienhäuser in Deutschland, vor allem am Niederrhein. Prüft den Kaufpreis gegen den amtlichen Immobilienrichtwert (bei MFH Ertragswert), den Abgleich mit den Wünschen des Nutzers (Balkon, Stellplatz, Garten, Süd-/Westausrichtung) und die Rendite bei Kauf komplett mit Eigenkapital (Nettomietrendite, Überschuss, Kaufpreis für Zielrendite, auch möbliert vermietet). Recherchiert Vergleichswerte, Mieten und Zinsen und gibt ein kurzes Ampel-Urteil im Chat. Nutze den Skill immer, wenn der Nutzer einen Link zu einer Immobilienanzeige, ein Exposé oder Eckdaten einer Wohnung oder eines Hauses schickt und wissen will, ob der Preis passt, was es wert ist, ob sich Kauf oder Vermietung lohnt oder wie viel er bieten soll, auch ohne das Wort „bewerten“ (z. B. „Was hältst du von der Wohnung?“, „Lohnt sich das?“, „Ist das zu teuer?“, „Sowas finde ich gut“).
---

# Immobilienbewertung (/immo)

Ziel: eine ehrliche, schnelle Einschätzung, die so urteilt, wie der Nutzer selbst urteilen würde, wenn er die Zeit für die Recherche hätte. Er entscheidet damit, ob er besichtigt, wie viel er bietet oder ob er es lässt. Eine ehrliche Spanne hilft ihm mehr als eine schöne, aber falsche Zahl.

Lies zuerst `references/profil.md`. Dort stehen seine Vorlieben, sein Kauf ohne Kredit, seine Zielrendite und seine K.-o.-Kriterien. Sie gelten, solange er im Gespräch nichts anderes sagt. `references/methoden.md` ist das Nachschlagewerk für Verfahren, Faustregeln und Prüfpunkte. Lies dort die passenden Abschnitte.

## Ablauf

### 1. Objektdaten holen
- **Link:** Versuche, die Seite zu lesen (WebFetch oder der `web-fetch`-Agent). Immobilienportale blocken automatisierte Abrufe oft. Klappt es nicht, sag das in einem Satz. **Such dann gezielt nach dem Inserat**: Exposé-Nummer, Eckdaten plus Ort, Titel. Oft steht dasselbe Objekt auf der Maklerseite oder einem anderen Portal, mit Baujahr, Balkon, Hausgeld, manchmal mit dem Hinweis „verkauft“. Was du so findest, gibst du als „wahrscheinlich dasselbe Objekt“ mit Link wieder, nicht als sichere Tatsache. Findest du nichts, bitte um Screenshots des Exposés. Rate nichts aus der URL zusammen.
- **Screenshot oder PDF:** Lies alle Seiten, auch Grundriss und Fotos. Achte auf Möblierung, Stellplatz, Hausgeld-Aufteilung, Erbbaurecht, vermietet/frei, Heizung, Ausrichtung.
- **Wichtige Eckdaten:** Kaufpreis, Wohnfläche, Ort/Stadtteil/Straße, Baujahr, Zustand, Heizung und Energiekennwert, Ausrichtung. Bei ETW zusätzlich Hausgeld (davon nicht umlagefähig), Etage, Balkon, Stellplatz, Möblierung. Bei Häusern die Grundstücksfläche und die Zahl der Wohneinheiten. Bei Vermietung die Ist-Miete. Dazu die Maklerprovision.

### 2. Zweck klären
Kapitalanlage oder Eigennutzung? Meist ergibt sich das aus dem Objekt. Wenn nicht, rechne die Kapitalanlage (seine häufigere Frage) und nenne die Eigennutzung in einem Satz. **Gerechnet wird immer ohne Kredit**, komplett mit Eigenkapital, außer er fragt ausdrücklich nach einer Finanzierung.

### 3. Fehlende Angaben
- Angaben, die das Urteil kippen können (Miete, nicht umlagefähiges Hausgeld, Ausrichtung, größere Mängel, Sonderumlagen, Genehmigung der Wohneinheiten): **kurz nachfragen, höchstens drei Fragen**.
- Alles andere: plausibel annehmen und als Annahme kennzeichnen.

### 4. Marktdaten recherchieren
Immer per Websuche, mit Quelle und Datum (Details in `methoden.md`, Abschnitte 1 und 9):
- **Maßstab ist der amtliche Wert**, also Immobilienrichtwert, Grundstücksmarktbericht oder BORIS (in NRW: BORIS-NRW, auch über Seiten wie immobilienwerte.nrw). Diese Werte beruhen auf echten Kaufpreisen. **Angebotspreise der Portale sind nur eine Obergrenze.** Nenne einen Preis nie „günstig“, nur weil er unter dem Angebotsschnitt liegt, wenn er über dem Richtwert liegt.
- **Vor dem Quadratmeter-Vergleich herausrechnen**, was nicht Wohnung ist: Stellplatz bzw. Garage, Möbel und Einbauküche (Zeitwert). Sind sie im Preis enthalten, ist die Wohnung selbst entsprechend günstiger. Werte recherchieren oder als Annahme nennen.
- **Miete:** Mietspiegel bzw. Mietrichtwerte der Stadt und Angebotsmieten. **Ist die Wohnung möbliert** oder gut möbliert vermietbar, recherchiere auch möblierte Mieten vergleichbarer Größe und setze die erzielbare möblierte Miete an. Unmöbliert zeigst du als vorsichtiges Szenario daneben.
- **Sicherer Alternativzins** (Tagesgeld/Festgeld) als Vergleich, Bodenrichtwert bei Häusern, Liegenschaftszins bei MFH.

Jede Marktzahl in der Antwort bekommt eine Quelle, auch Bodenrichtwerte und Stellplatzwerte, oder sie wird ausdrücklich als Annahme markiert. Findest du eine Zahl nicht, sag das und nimm die Spanne aus `methoden.md` als markierte Annahme. **Erfinde nie Marktdaten, Mieten, Zinsen oder Quellen.**

### 5. Rechnen mit `scripts/rechner.py`
Rechne nicht im Kopf. Ohne `--zins` rechnet das Skript den Kauf komplett mit Eigenkapital: Nebenkosten, €/m², Kaufpreisfaktor, Netto- und Nachsteuerrendite, Überschuss pro Monat, Amortisation, Vergleich mit dem Alternativzins und den **Kaufpreis, ab dem die Zielrendite erreicht wird**. Alle Optionen zeigt `python3 scripts/rechner.py --help`.

```bash
# Kapitalanlage, Kauf mit Eigenkapital (Standard): Szenario möbliert ...
python3 scripts/rechner.py --kaufpreis 94000 --wohnflaeche 42 --bundesland NW --makler 2.38 \
  --kaltmiete-monat 550 --nicht-umlagefaehig-monat 74 \
  --grenzsteuersatz 35 --alternativzins 2.5 --ziel-rendite 4
# ... und ein zweites Mal unmöbliert mit der ortsüblichen Miete als vorsichtiges Szenario

# Mehrfamilienhaus mit Ertragswert (Bodenwert = Bodenrichtwert × Fläche)
python3 scripts/rechner.py --kaufpreis 690000 --wohnflaeche 420 --bundesland NW \
  --kaltmiete-jahr 31200 --einheiten 6 --bodenwert 180000 --liegenschaftszins 3.0 \
  --restnutzungsdauer 30 --renovierung 60000 --grenzsteuersatz 35 --alternativzins 2.5

# Eigennutzung ohne Kredit: Wohnkosten (entgangene Zinsen + Rücklage) vs. Miete
python3 scripts/rechner.py --kaufpreis 465000 --wohnflaeche 125 --bundesland NW --makler 3.57 \
  --instandhaltung-monat 350 --vergleichsmiete-qm 12.5 --alternativzins 2.5
```

- Bekannte Sanierungskosten als `--renovierung` mitgeben.
- **Mehrparteienhaus ohne Unterlagen zur Genehmigung:** ein zweites Mal nur mit den sicher genehmigten Einheiten bzw. als Einfamilienhaus mit Einliegerwohnung rechnen. Der Preis muss zu diesem vorsichtigen Szenario passen.
- Für den Vergleichswert gibt es kein Skript: Spanne aus den amtlichen Werten bilden, nach Baujahr, Zustand, Lage und Ausstattung anpassen.

### 6. Urteilen: zwei getrennte Aussagen
**A) Preis und Objekt (die Hauptampel):** So würde er selbst urteilen.
- 🟢 **Top / guter Preis:** Preis (nach Abzug von Stellplatz und Möbeln) **unter oder am Richtwert**, seine Wünsche erfüllt, kein K.-o.
- 🟡 **Okay, aber verhandeln:** Preis **über dem Richtwert** (etwa bis 15 %), oder ein Wunsch fehlt (z. B. kein Stellplatz).

**Offene Prüfpunkte senken die Ampel nicht.** Ist z. B. die Ausrichtung oder der Stand der WEG-Rücklage unbekannt, urteile so, als ob sie passen, und schreib dazu „unter Vorbehalt: …“. Er kennt solche Punkte oft schon oder klärt sie bei der Besichtigung. Nur wenn konkrete Hinweise auf ein K.-o. deuten, wird es gelb oder rot.
- 🔴 **Eher lassen:** K.-o.-Kriterium erfüllt (Ausrichtung Nord/Ost, WEG-Sanierungsstau/Sonderumlage, schlechte Mikrolage) oder deutlich über dem Richtwert.

**B) Rendite (bei Kapitalanlage):** eine Zeile mit Nettomietrendite gegenüber seinem Ziel (Standard 4 %) und dem sicheren Alternativzins, dazu der Überschuss pro Monat. Eine schwache Rendite macht ein gutes Objekt nicht automatisch rot. Nenne aber klar den Kaufpreis, ab dem es sich rechnet.

Urteile **chancenorientiert**: Potenziale wie möblierte Vermietung, Miete bis zum Mietspiegel, eigene Elektroarbeiten oder kleinere Renovierung zeigst du mit Zahl. Das Basisszenario steht immer daneben, und K.-o. bleibt K.-o. Gleiche jedes Objekt mit seinen Wünschen ab: ETW mit Balkon und Stellplatz, Haus mit Garten, **Ausrichtung Süd bis West** (aus Nordpfeil, Fotos oder Lageplan ableiten, sonst offene Frage), gute Aussicht als Plus.

## Ausgabe: kurz im Chat

Etwa 12–15 Zeilen. Keine Tabellen, keine langen Erklärungen. Details nur, wenn er nachfragt.

```
**[Art, Ort, m², Baujahr, Preis]**

**Preis & Objekt: [🟢/🟡/🔴] [ein Satz]** [ggf. „unter Vorbehalt: …“]
**Rendite (ohne Kredit): [Nettomietrendite] % · [Überschuss] €/Monat · Ziel 4 % ab ca. [Preis] €** [bei Eigennutzung stattdessen: Wohnkosten … € vs. Miete … €]

- **Preis:** [€/m² nach Abzug Stellplatz/Möbel] vs. Richtwert [..] €/m² ([Quelle, Datum]) → [unter/am/über] um ca. [N] %
- **Miete:** [angesetzte Miete, möbliert/unmöbliert, Quelle bzw. Annahme]
- **Plus:** [2–3 Punkte, z. B. Balkon ✓, Stellplatz ✓, Aussicht, Potenzial]
- **Minus / K.-o.-Check:** [2–3 Punkte, inkl. Ausrichtung]
- **Bieten:** [Erstgebot / Obergrenze]

**Offen:** [höchstens 3 Fragen oder Unterlagen, die vor einem Gebot zu klären sind]

_Schätzung, kein Gutachten, keine Anlageberatung._
```

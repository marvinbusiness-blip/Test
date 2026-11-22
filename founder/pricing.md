# Preis: Smart-Home-Nachrüstung Willich (Rollläden per Shelly)

Stand: 22.11.2026 · Grundlagen: `pricing-curve.md` (Panel), `competitors.md`, `garantie.md`, `panel/results.md`

> **Wichtig:** Die Preisangaben stammen von 20 **simulierten** Käufern. Sie zeigen, welche Preise sich zu testen lohnen, beweisen aber nichts. Das CFO-Tool konnte noch nicht laufen, weil `founder/numbers.json` fehlt (Fixkosten, Versicherung, Kammerbeitrag, geplante Auftragszahl). Die Margen unten sind eine **Überschlagsrechnung mit gekennzeichneten Annahmen**, `/founder-cfo` rechnet sie sauber nach.

## 1. Der Preis: 119 € pro Rollladen (Standard ab 4 Rollläden)

**Was die Käufer sagten** (Van-Westendorp-Analyse, das Tool zeigt „$“, gemeint ist €):

| Punkt | Preis | Bedeutung |
|---|---:|---|
| PMC | 50 € | Darunter wirkt es zu billig |
| OPP | 50 € | Geringster Widerstand (stark nach unten gezogen von Bastlern und Preisvergleichern) |
| IPP | 80 € | Gleich viele finden es günstig wie teuer |
| PME | 140 € | Darüber kaufen zu viele nicht mehr |

**Akzeptabler Bereich: 50 bis 140 €.** Mittlere Antworten: zu billig 40 €, Schnäppchen 70 €, „wird teuer“ 129 €, zu teuer 169 €. Für 16 von 20 Käufern liegen 119 € unter ihrer Schmerzgrenze.

**Was die Konkurrenz nimmt** (Komplettpreis pro Rollladen inkl. Gerät, Einbau und Einrichtung): etwa 100–190 €, Median ≈117 €. Alboush ≈115 € (Blog-Beispiel), der Elektriker beim Bekannten ≈117 €, ein Forenangebot 190 €, der NRW-Richtwert 100–220 €.

**Warum 119 € und nicht billiger:**
- Der Preis liegt im akzeptablen Bereich, genau am Marktmedian und unter dem mittleren „wird teuer“ der Käufer (129 €).
- **Der Preis war nicht der Hauptgrund für die Absagen** (5 von 20), sondern das Vertrauen (11 von 20). Billiger zu werden löst das Vertrauensproblem nicht. Es zieht vor allem Bastler und Preisvergleicher an, und die sind nicht deine Zielgruppe.
- Unter etwa 100 € wärst du die Austauschware zum Kampfpreis, vor der das Board gewarnt hat.

**Was dir pro Rollladen bleibt (Überschlag, Annahmen gekennzeichnet):**

Kosten pro Rollladen ≈ **28 €**: Shelly 2PM Gen3 ≈18 € (Handelspreis 16–20 €), Kleinmaterial ≈2 € (Annahme), Rücklage für 2 Jahre Austausch vor Ort ≈8 € (aus `garantie.md`, 5–10 €).

Zeit (Annahme): **25 Minuten pro Rollladen** plus **90 Minuten pro Auftrag** (Foto-Check und Angebot, Anfahrt in Willich, App, Einweisung, Abnahme).

| Auftrag | Umsatz | Rohertrag* (Kleinunternehmer) | Zeit | ≈ €/Stunde* | wenn umsatzsteuerpflichtig** |
|---|---:|---:|---:|---:|---:|
| 2 Rollläden à 139 € | 278 € | 222 € | 2,3 h | ≈95 € | ≈76 € |
| 5 Rollläden à 119 € | 595 € | 455 € | 3,6 h | ≈127 € | ≈100 € |
| 10 Rollläden à 105 € | 1.050 € | 770 € | 5,7 h | ≈136 € | ≈106 € |
| Referenzkunde 5 à 95 € | 475 € | 335 € | 3,6 h | ≈94 € | ≈73 € |

\* Vor Versicherung, Kammerbeitrag, Auto, Werkzeug und Einkommensteuer. \*\* Gilt die Kleinunternehmerregelung nicht, stecken in 119 € brutto 19 € Umsatzsteuer, es bleiben 100 € netto. **Zu prüfen mit Steuerberater:** Neben dem Vollzeitjob wäre die Kleinunternehmerregelung (§ 19 UStG) wahrscheinlich möglich.

**Argument gegen den Preiseinwand (zu prüfen):** Privatkunden können 20 % der **Arbeitskosten** von der Steuer abziehen (Handwerkerleistungen, § 35a EStG, max. 1.200 € Ermäßigung pro Jahr). Voraussetzung: Arbeitslohn auf der Rechnung getrennt ausweisen, Zahlung per Überweisung. Bei ≈95 € Arbeitsanteil sind das ≈19 € pro Rollladen zurück. Ehrlich formulieren („kann steuerlich abgesetzt werden“), nicht als Rabatt verkaufen.

## 2. Die Preisstaffel

Alle Stufen enthalten dasselbe Vertrauenspaket:
- kostenloser Foto-Check vorab
- „Läuft, oder Sie zahlen nicht“ bei der Übergabe
- **2 Jahre kostenloser Austausch defekter Module vor Ort**
- **läuft auch ohne Internet, der Schalter funktioniert immer**
- 30 Tage Hilfe

| Stufe | Für wen | Preis | Grund für die nächste Stufe |
|---|---|---:|---|
| **Einstieg** (1–3 Rollläden) | „Erst mal nur oben im Dachgeschoss oder Schlafzimmer“ | 139 € je Rollladen | Anfahrt und Einrichtung verteilen sich auf wenige Geräte. Ab dem 4. wird es günstiger |
| **Haus** (4–7 Rollläden) | Die meisten Einfamilienhäuser | 119 € je Rollladen | Ab 8 Rollläden Ganzes-Haus-Preis |
| **Ganzes Haus** (ab 8 Rollläden) | Große Häuser, Preisvergleicher | 105 € je Rollladen | 8 Rollläden = 840 €, also unter der oft genannten Grenze von „über tausend Euro“ |

**Später dazu (nach den ersten Aufträgen):** Service-Pauschalen für Fälle ohne Mangel (Fernhilfe, Vor-Ort-Termin) und eventuell ein „Sorglos-Paket“ pro Jahr (siehe `garantie.md`). Licht und Steckdosen erst, wenn die Rollläden störungsfrei laufen.

**Wer bei den Absagen wegen des Preises gemeint war:** Die Staffel beantwortet die Klage „Stückpreis ohne Mengenrabatt ist nicht fair“ (P016, P020). Der Einstiegspreis beantwortet „erst nur oben“ (P010, P019). Den Bastlern, die 40–50 € für die reine Montage wollen (P018), läufst du bewusst nicht hinterher.

## 3. Das Eröffnungsangebot: Referenzkunden statt Rabattschlacht

- **Die ersten 5 Haushalte: 95 € je Rollladen** (Haus-Stufe). Im Gegenzug gibt es eine ehrliche Google-Bewertung, und du darfst die Anlage zwei bis drei Interessenten zeigen bzw. sie als Referenz nennen.
- **Klares Ende:** nach 5 Aufträgen oder spätestens 8 Wochen nach Start, je nachdem, was zuerst eintritt. Danach gelten 119 €.
- **Ehrlich formulieren:** „Referenzpreis für die ersten fünf Kunden“, kein „statt 119 €“, solange noch niemand 119 € bezahlt hat.
- **Empfehlungsbonus danach:** Bucht jemand auf Empfehlung eines Kunden, bekommen beide z. B. 25 € (Höhe mit `/founder-cfo` prüfen). Das zielt direkt auf den häufigsten Kipp-Grund im Panel, die Empfehlung durch Nachbarn.
- **Zeitpunkt:** Mehrere Käufer sagten „im November drängt die Hitze nicht“. Start mit den Referenzkunden im Winter oder Frühjahr, Werbung mit Hitzeschutz ab April oder Mai.
- Der Referenzpreis liegt deutlich über den Kosten (Rohertrag ≈67 € pro Rollladen), es wird also nicht unter Kosten verkauft.

## 4. Was mit echten Käufern getestet wird

**Zwei Preise in der Haus-Stufe: 109 € gegen 129 € pro Rollladen.**

So testest du das:
- Ein einfacher Flyer bzw. eine Landingpage in zwei Varianten. Die Unterschiede liegen nur im Preis, das Paket ist identisch.
- Die Varianten wechseln nach Ortsteil (z. B. Anrath und Neersen gegen Schiefbahn und Willich-Mitte) oder im Zwei-Wochen-Takt bei Kleinanzeigen und auf der Shelly-Installateur-Karte.
- Gemessen werden **Anfragen pro Variante** und **Angebote, die zum Auftrag werden**.
- Erst nach etwa 10 Angeboten pro Variante entscheiden.
- Echte Antworten schlagen die simulierten. Danach den Wert in `numbers.json` anpassen.

Zusätzlich solltest du die 3 Probeanfragen bei Elektro Lücke, Michiels und Alboush machen (4 Rollläden in Willich, Checkliste des Boards). Dann kennst du die echten lokalen Preise.

## 5. Die drei wichtigsten Preiseinwände aus dem Panel (wörtlich, simuliert)

1. *„Der Stückpreis läppert sich: Das Shelly-Ding kostet im Netz um die 25 Euro, also zahle ich fast 95 Euro Arbeit pro Schalter, obwohl das zehn Minuten pro Dose sind, wenn er eh schon da ist.“* (P013)
   → Antwort: Staffelpreis, Festpreis inklusive Garantie, Abnahme-Test und 2 Jahre Austausch vor Ort. Außerdem den Arbeitsanteil steuerlich absetzen.
2. *„Einen Preis pro Stück ohne Mengenrabatt finde ich bei so einer Menge nicht fair.“* (P016)
   → Antwort: Ganzes-Haus-Stufe ab 8 Rollläden.
3. *„Ich hab zehn Rollläden, das wären fast 1.200 €. … das rechne ich mir mit drei Angeboten von MyHammer locker günstiger aus.“* (P004)
   → Antwort: 10 Rollläden = 1.050 €, minus Steuerbonus auf den Arbeitsanteil. Und vor allem: einen Festpreis vorab mit Garantie, den andere Elektriker laut Recherche selten bieten.

## Offen für die nächsten Skills

- `/founder-offer`: das Vertrauenspaket (2-Jahres-Zusage, „läuft ohne Internet“, Referenzen, Empfehlungsbonus) als Angebot formulieren.
- `/founder-cfo`: `numbers.json` mit echten Fixkosten anlegen und die Margen dieser Staffel nachrechnen. Wichtigste Unbekannte: Zeit pro Rollladen, Versicherung, Kammerbeitrag, Umsatzsteuer-Status.

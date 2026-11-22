# CFO-Notiz (Stand 22.11.2026)

> Das Tool schreibt „$“, gemeint ist überall **€**. „Rollladens a day“ heißt hier **Rollläden pro Einsatztag**, gerechnet mit **4 Einsatztagen im Monat** (z. B. Samstage oder Abende). Keine Steuer-, Rechts- oder Finanzberatung: Bitte lass Rechtsform, Umsatzsteuer-Status und Einkommensteuer von einem Steuerberater prüfen, bevor Geld fließt.

**Die Marge.** Jeder Rollladen à 119 € lässt **87,30 € Deckungsbeitrag** (73 %). Abgezogen sind Shelly, Kleinmaterial, Garantie-Rücklage, Fahrt und Empfehlungsbonus. Die Fixkosten sind mit **114 €/Monat** klein. Break-even liegt deshalb bei nur **≈1,3 Rollläden pro Monat** (114 € ÷ 87,30 €). Im Plan bleiben **69 %** jedes Umsatzes als Gewinn, vor Einkommensteuer. Jahr 1 im Basisplan: **156 Rollläden (~31 Aufträge), 18.564 € Umsatz, 12.251 € Gewinn**, nach den Startkosten 10.915 €.

**Die Zeile, die man beobachten muss: die Auftragsmenge.** Der Preis ist es nicht.

| Was-wäre-wenn | Gewinn Jahr 1 | Unterschied |
|---|---:|---:|
| Basisplan (119 €, 156 Rollläden) | 12.251 € | – |
| Preis −10 % | 10.394 € | −1.857 € |
| Stückkosten +15 % | 11.509 € | −742 € |
| Menge −20 % | 9.527 € | −2.724 € |
| **Menge −50 %** (78 Rollläden) | **5.441 €** | **−6.810 €** |
| Menge −75 % (39 Rollläden, ~8 Aufträge) | 2.037 € | −10.214 € |
| Preis 105 € **und** Menge −50 % | 4.349 € | −7.902 € |

Selbst bei einem Viertel der geplanten Menge entsteht kein Verlust. Das Risiko dieses Geschäfts ist also nicht, Geld zu verlieren, sondern dass sich die Zeit kaum lohnt. Das Panel hat kalt 0 von 20 Käufen ergeben. Die Menge hängt deshalb fast ganz an Empfehlungen und Referenzen. Die Rampe unten ist eine **Schätzung** und nicht belegt.

**Cash.** Vor dem ersten Euro Umsatz brauchst du etwa **1.336 €**. 930 € davon sind ein VDE-Installationstester, **falls du noch keinen hast**. Ohne ihn sind es etwa 406 €. Im Basisplan ist das Geld im **3. Monat** wieder drin, bei halber Menge im 5. Monat.

**Dein Stundenlohn (Überschlag, nicht aus dem Tool):** 156 Rollläden × 25 min plus 31 Aufträge × 90 min ≈ **112 Stunden im Jahr**. Das sind etwa 2 bis 3 Stunden pro Woche, in Spitzenmonaten rund 14 Stunden pro Monat. 12.251 € ÷ 112 h ≈ **110 €/h vor Einkommensteuer**. Die Zeiten sind Annahmen und müssen bei den ersten Aufträgen gemessen werden.

**Drei Hebel für mehr Ergebnis** (aus den Was-wäre-wenn-Rechnungen):
1. **Mehr Aufträge über Empfehlungen:** Jede +20 % Menge bringt etwa **+2.700 €** pro Jahr. Das ist der größte Hebel. Dafür sorgen Referenzkunden, Bewertungen, Empfehlungsbonus und der Saisonstart im Frühjahr mit Hitzeschutz.
2. **Den Durchschnittspreis halten:** 139 € statt 119 € bringt **+3.120 €**, 105 € statt 119 € kostet **−2.184 €**. Die Ganzes-Haus-Stufe (105 €) und der Referenzpreis (95 €) senken den Schnitt. Den Referenzpreis deshalb wirklich auf 5 Kunden begrenzen. Die ersten 25 Rollläden zu 95 € kosten etwa 600 € gegenüber dem Plan.
3. **Stückkosten sind ein kleiner Hebel:** Shelly im Mehrfachpack beim Großhändler kaufen und Leerfahrten durch den Foto-Check vermeiden. −15 % Stückkosten bringen nur etwa **+740 €**. Nicht am Material sparen, das gefährdet die Garantie.

**Steuern, die das Ergebnis schmälern (zu prüfen):**
- **Einkommensteuer:** Der Gewinn kommt zu deinem Gehalt dazu und wird mit deinem persönlichen Grenzsteuersatz versteuert. Davon geht also ein spürbarer Teil ans Finanzamt.
- **Umsatzsteuer:** Mit ~18.600 € Umsatz im Jahr 1 läge der Betrieb unter der Grenze der Kleinunternehmerregelung (§ 19 UStG, Vorjahresumsatz bis 25.000 €). Dann gilt 119 € = 119 € ohne Umsatzsteuer. Gilt sie nicht, bleiben von 119 € brutto nur 100 € netto, und der Gewinn sinkt deutlich (vergleiche Preis −10 % bis −20 %).

**Bedingungen des Boards zu Geld (`board.md`):**
- [x] Preis nicht unter dem Marktmedian: 119 € ≈ Median 117 €.
- [~] Kosten von Garantie, Support und Leerfahrten: Die Garantie-Rücklage ist drin (8 €/Rollladen). Bezahlter Support (Pauschalen) ist noch nicht als Umsatz eingeplant. Leerfahrten sind nicht eingerechnet. Die Zeit pro Rollladen ist **noch nicht gemessen**.
- [ ] Kundenzugang mit bekannten Kosten pro Kunde: Bisher nur geschätzt (Empfehlungsbonus, 20 €/Monat Marketing). Belegen lässt sich das erst mit dem Testlauf.
- [ ] Testlauf mit Ziel aus dem Break-even: Der Break-even (≈1,3 Rollläden/Monat) ist zu niedrig, um als Ziel zu taugen. **Vorschlag:** Lohnenswert ist es ab etwa 2 Aufträgen pro Monat im Schnitt (≈10 Rollläden). Bringen 8 Wochen Testlauf weniger als 2 echte Anfragen, ist die Lücke in Willich nicht belegt.

---

# Unit economics: Smart-Home-Nachrüstung Willich (Rollläden per Shelly), nebenberuflich

Every number below comes from the input file. Nothing is looked up or guessed.

## One Rollladen

| line | per Rollladen |
| --- | ---: |
| Price | $119.00 |
| Shelly 2PM Gen3 (Handelspreis 16-20 €) | -$18.00 |
| Kleinmaterial, Klemmen (Schätzung) | -$2.00 |
| Rücklage 2 Jahre Vor-Ort-Austausch (Schätzung, garantie.md) | -$8.00 |
| Fahrtkosten (Ø 20 km/Auftrag × 0,30 €/km ÷ 5 Rollläden, Schätzung) | -$1.20 |
| Empfehlungsbonus (25 € je 2. Auftrag ÷ 5 Rollläden, Schätzung) | -$2.50 |
| **Contribution** (what each Rollladen leaves to pay the fixed costs) | **$87.30** (73%) |

## The margin that matters

Fixed costs: $114 a month (Betriebshaftpflicht Elektro (Schätzung 400 €/Jahr, Angebote einholen) $33, Handwerkskammer-Beitrag (Jahr 1 befreit; danach ermäßigt, Höhe erfragen) $0, Buchhaltung + Steuerberater Jahresabschluss (Schätzung) $35, Laufendes Marketing: Flyer, Anzeigen (Schätzung) $20, Telefon, Domain, Webseite (Schätzung) $10, Geschäftskonto (Schätzung) $8, Kalibrierung Prüfgerät (Schätzung ~100 €/Jahr) $8).

- **Break-even: 1 Rollladens a day.** Below that you lose money every month.
- **Profit margin at your plan** (5 a day): **69%** of every sale, after every cost.
- Capacity: 10 a day.

## Year 1, month by month

| month | Rollladens a day | revenue | profit | cumulative (after $1,336 startup) |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 2 | $952 | $584 | -$752 |
| 2 | 2 | $952 | $584 | -$167 |
| 3 | 2 | $952 | $584 | $417 |
| 4 | 3 | $1,428 | $934 | $1,351 |
| 5 | 4 | $1,904 | $1,283 | $2,634 |
| 6 | 5 | $2,380 | $1,632 | $4,266 |
| 7 | 5 | $2,380 | $1,632 | $5,898 |
| 8 | 5 | $2,380 | $1,632 | $7,530 |
| 9 | 4 | $1,904 | $1,283 | $8,812 |
| 10 | 3 | $1,428 | $934 | $9,746 |
| 11 | 2 | $952 | $584 | $10,330 |
| 12 | 2 | $952 | $584 | $10,915 |

- **Year 1 operating profit: $12,251** on $18,564 of revenue.
- After the $1,336 startup spend: $10,915.
- Startup money earned back: month 3.
- Cash you need before it pays for itself: **$1,336**.

## What if

| scenario | margin at plan | break-even a day | year 1 profit |
| --- | ---: | ---: | ---: |
| Base plan | 69% | 1 | $12,251 |
| Price -10% | 65% | 1 | $10,394 |
| Volume -20% | 67% | 1 | $9,527 |
| Unit costs +15% | 65% | 1 | $11,509 |

No red flags in these numbers. They are only as good as the inputs: check every cost against a real quote.

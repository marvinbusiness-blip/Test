# Betrieb: wie das Geschäft am ersten Tag wirklich läuft

Stand: 22.11.2026 · Grundlagen: `idea.md`, `numbers.json`, `garantie.md`, `pricing.md`, `board.md`
**Keine Rechts-, Steuer- oder Versicherungsberatung.** Regeln unterscheiden sich je nach Ort und ändern sich. Jeden Punkt in Abschnitt 6 bei der genannten Stelle bestätigen lassen.

> **Drei Funde, die vor dem Start geklärt sein müssen:**
> 1. **Rentenversicherungspflicht für Handwerker:** Wer in der Handwerksrolle eines zulassungspflichtigen Handwerks (Anlage A, dazu gehört Elektrotechnik) eingetragen ist, ist in der Regel rentenversicherungspflichtig, **auch im Nebenerwerb**. Ausnahme: Das Einkommen bleibt geringfügig (laut einer Quelle **603 €/Monat** in 2026). Der Plan (≈1.000 €/Monat Gewinn) liegt darüber. Mögliche Kosten: einkommensgerecht ≈18,6 % vom Gewinn (≈190 €/Monat beim Plan) oder pauschal (halber Regelbeitrag 2026 ≈368 €/Monat in den ersten Jahren). **Bei der DRV und der Handwerkskammer klären.** Das kann das Ergebnis um 2.000–4.400 € pro Jahr senken, oder es spricht dafür, den Gewinn bewusst unter der Geringfügigkeitsgrenze zu halten. ([HWK Halle 2026](https://www.hwkhalle.de/wp-content/uploads/Rentenversicherungspflicht-2026.pdf), [DRV-Meldung](https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2026/261109_handwerker_meldepflicht), [MittelstandsWiki](https://www.mittelstandswiki.de/wissen/Rentenversicherungspflicht_f%C3%BCr_Handwerker/))
> 2. **Arbeitgeber:** Die Nebentätigkeit melden. Ist dein Hauptjob in der Elektrobranche, kann ein Wettbewerbsverbot greifen. Den Arbeitsvertrag prüfen.
> 3. **Netzbetreiber (Installateurverzeichnis):** Die Stadtwerke Willich haben ein Installateurportal. Für die Eintragung bestätigt man in der Regel die Verfügbarkeit der **Mess- und Prüfgeräte und der Werkstattausrüstung**. Nur geliehene Geräte reichen laut einem Anbieter oft nicht. Also erst klären, ob du eingetragen sein musst, dann über den Kauf des Prüfgeräts entscheiden. ([Stadtwerke Willich Installateurportal](https://stadtwerke-service.de/installateure/installateurportal/), [Westnetz-Hinweise](https://www.westnetz.de/content/dam/revu-global/westnetz/documents/fuer-partnerfirmen/eintragung-strom-installationsunternehmen/hinweise-zum-antrag-eintragung-installateurverzeichnis-strom.pdf), [Wilmes: Eintragung 2026](https://wilmes.de/aein-und-installateurverzeichnis-warum-eintragungsberechtigung-2026-kein-papiernachweis-mehr-is/))

---

## 1. Der Ablauf eines Auftrags (statt eines Ladentags)

Mit 👁 markiert ist, was der Kunde sieht.

| # | Schritt | Wann | Dauer (Annahme) |
|---|---|---|---|
| 1 | 👁 Anfrage kommt rein (Telefon, WhatsApp, Kontaktformular, Shelly-Karte) | jederzeit | – |
| 2 | 👁 **Antwort innerhalb von 24 Stunden** mit Bitte um Fotos: Schalterdose geöffnet (Sicherung aus!) oder Schalter abgeschraubt, Rollladenmotor/Gurt, Anzahl Fenster, WLAN-Router-Standort | abends | 5 min |
| 3 | Foto-Check: Neutralleiter da? Dosentiefe? Motor 230 V mit Wandtaster? WLAN-Weg plausibel? | abends | 10 min |
| 4 | 👁 Festpreis-Angebot (Staffel aus `pricing.md`) + Widerrufsbelehrung + Leistungsbeschreibung; Terminvorschläge | abends | 10 min |
| 5 | Material bereitlegen (Shellys aus dem Vorrat, Klemmen, Ersatzgerät, tiefe Dosen falls nötig) | vor dem Termin | 10 min |
| 6 | 👁 Vor Ort: begrüßen, WLAN-Signal an jedem Fenster mit dem Handy prüfen, Plan kurz erklären | Samstag / Abend | 15 min |
| 7 | Einbau pro Rollladen: Sicherung aus, spannungsfrei prüfen, Foto vorher, Shelly einbauen, Taster an Eingänge, Foto nachher, Modul beschriften | | 25 min/Rollladen |
| 8 | Prüfung: Besichtigen, Erproben, Messen nach VDE 0100-600 soweit erforderlich (Shelly bei Isolationsmessung schützen) | | 10–20 min |
| 9 | 👁 Einrichtung: Shelly-App **auf dem Konto des Kunden**, Geräte benennen, Endlagen kalibrieren, Zeitpläne (morgens/abends/Urlaub/Hitzeschutz), lokal laufend; optional Freigabe für Fernhilfe | | 20–30 min |
| 10 | 👁 **Abnahme**: jeden Rollladen gemeinsam testen (Schalter, App, Zeitplan) → Abnahmeprotokoll unterschreiben | | 10 min |
| 11 | 👁 Übergabeblatt (Modul ↔ Raum, Konto-Inhaber, „Schalter geht immer“, Kontakt, Service-Pauschalen) + Bitte um Google-Bewertung | | 5 min |
| 12 | 👁 Rechnung (Arbeitslohn separat für § 35a EStG), Zahlung per Überweisung binnen 7 Tagen | am selben Abend | 10 min |
| 13 | Kundenakte anlegen: Fotos, Protokolle, Seriennummern, Firmware-Stand. **Keine WLAN-Passwörter speichern** | | 10 min |
| 14 | 👁 Nach 7 Tagen kurze Nachfrage „läuft alles?“; nach 30 Tagen Ende der Inklusiv-Hilfe ankündigen | | 5 min |

**Zeit pro Auftrag mit 5 Rollläden:** ≈3,5–4 Stunden inkl. Vorbereitung. Das passt zur Annahme in `numbers.json` (25 min/Rollladen + 90 min/Auftrag). **Bei den ersten 5 Aufträgen messen.**

## 2. Lieferanten

| Was | Bezugsquellen | Preis | Mindestmenge / Lieferzeit / Zahlung |
|---|---|---|---|
| **Shelly 2PM Gen3** | [Shelly-Shop](https://www.shelly.com/de/products/shelly-2pm-gen3-1) (18–20 €; Installateur-Programm mit 10 % Cashback, [Info](https://www.shelly.com/de/blogs/media-center/shelly-installer-portal-attraktive-vorteile-fur-installateure)); Onlinehändler wie [Alternate](https://www.alternate.de/Shelly/2PM-Gen3-Relais/html/product/100094762), [Proshop](https://www.proshop.de/Smart-Home/Shelly-2PM-Gen3/3302030), [Galaxus 4er-Pack](https://www.galaxus.de/en/s4/product/shelly-2pm-gen3-x4-switch-actuator-actuator-54257936), [Berrybase](https://www.berrybase.de/shelly/); Preisvergleich 15,99–60,89 € ([testberichte.de](https://www.testberichte.de/heimwerkerbedarf/shelly-2pm-gen3.html)) | ≈16–20 € einzeln, 4er-Pack ≈75 € | Kein Mindestbestellwert, Lieferung meist 1–3 Tage, Kauf per Firmenrechnung. **Elektrogroßhandel** (z. B. Sonepar, Rexel, regionale Großhändler): **Konditionen nur auf Anfrage**, Firmenkonto mit Gewerbenachweis |
| Verbindungsklemmen, tiefe Schalterdosen, Kleinteile | Elektrogroßhandel, Baumarkt (Notfall) | **Angebot einholen** | Firmenkonto |
| Ersatzvorrat | 3 Shellys immer im Auto | ≈55 € (im Material enthalten) | – |
| **Installationstester VDE 0100-600** (falls nötig) | Benning IT 105 ≈928 € ([Kaufland](https://www.kaufland.at/product/316536419/)); Chauvin Arnoux CA 6131 ≈728 € ([Datatec](https://datatec.eu/at/en/testers-comparison?p=2)); Fluke 1663 ≈1.591 €; gebraucht mit Kalibrierschein deutlich günstiger | 700–1.600 € | Kalibrierung ≈jährlich |
| Flyer, Visitenkarten | Online-Druckereien | **Angebot einholen** | – |

**Abgleich mit `numbers.json`:** Der Shelly-Preis (18 €) bestätigt sich. Die Gewerbeanmeldung kostet in NRW laut Landesgebührenordnung für Einzelunternehmer typischerweise 26 € ([Beispiel Dortmund](https://www.dortmund.de/services/gewerbeanmeldung.html), [Meerbusch](https://www.firma.de/gewerbeamt/meerbusch/)), daher in `numbers.json` von 30 € auf 26 € angepasst. Der Effekt ist vernachlässigbar, aber `/founder-cfo` neu laufen lassen, sobald echte Angebote für Haftpflicht, Großhandel und Kammer vorliegen.

## 3. Personen

**Es gibt nur dich.** Keine Löhne, keine Lohnnebenkosten.

| Phase | Wann arbeitest du | Volumen |
|---|---|---|
| **Langsamer Start** (Monat 1–3, Referenzkunden) | 2 Abende/Woche à 30 min für Anfragen, Angebote und Rechnungen + **1 Samstag alle 2 Wochen** für einen Einbau | ≈8 Rollläden/Monat |
| **Plan** (Saison Mai–August) | 2–3 Abende/Woche à 30 min + **jeden Samstag** 1 Auftrag (gelegentlich 2) | ≈20 Rollläden/Monat, ≈14 h/Monat |
| **Winter** | wie Start | ≈8 Rollläden/Monat |

- **Antwortversprechen, das du halten kannst:** Antwort innerhalb von 24 Stunden (abends), Termin innerhalb von 2–3 Wochen. Lieber das ehrlich zusagen als „sofort“ versprechen.
- **Urlaub/Krankheit:** Weil der Wandschalter immer funktioniert, gibt es keine echten Notfälle. Abwesenheiten auf Mailbox und WhatsApp-Status ansagen.
- **Später:** Bei mehr Nachfrage als Samstagen eher die Preise anheben oder Wartezeiten verlängern, statt jemanden einzustellen. Ein Mitarbeiter würde Lohnnebenkosten, die BG-Pflicht und Haftung auslösen. Das mit einem Steuerberater klären.
- **Arbeitszeit:** Achte auf Erholung neben dem Vollzeitjob. Dein Arbeitsvertrag kann Grenzen für Nebentätigkeiten setzen.

## 4. Routinen (je eine Seite)

### R1: Anfrage → Angebot (Ziel: innerhalb von 24 h)
1. Anfrage in die Kundenliste eintragen (Name, Ort, Kanal, Datum).
2. Standardantwort mit Bitte um Fotos schicken (Vorlage: Schalterdose offen **bei ausgeschalteter Sicherung** oder einfach Schalter und Rollladen fotografieren, Anzahl Fenster, Router-Standort).
3. Fotos prüfen. Kein Neutralleiter, Funkmotor ohne Taster oder Gurtwickler ohne Motor: **freundlich absagen** oder eine Alternative nennen, keine Anfahrt.
4. Festpreis nach Staffel berechnen, Angebot mit Leistungsbeschreibung, Ausschlüssen (WLAN, Router, Cloud), Widerrufsbelehrung und 2–3 Terminen senden.
5. Nach 5 Tagen ohne Antwort einmal freundlich nachfragen, dann nicht mehr.

### R2: Einbau-Termin
1. Am Vorabend: Material, Ersatz-Shellys, Klemmen, Messgerät, Spannungsprüfer, Beschriftungsetiketten, Protokolle, geladenes Handy.
2. Vor Ort: WLAN an jedem Fenster prüfen. Wenn es zu schwach ist: Lösung besprechen (Repeater kauft der Kunde), **bevor** du anfängst.
3. Pro Rollladen: Sicherung aus → spannungsfrei prüfen → Foto → einbauen → Taster an die Eingänge → Foto → beschriften.
4. Prüfen und messen, Werte ins Protokoll.
5. App auf dem Kundenkonto einrichten, Zeitpläne nach Kundenwunsch, Funktion „läuft ohne Internet“ zeigen (WLAN kurz aus → Schalter geht).
6. Weiter mit R3.

### R3: Übergabe und Abnahme
1. Jeden Rollladen gemeinsam testen: Schalter, App, ein Zeitplan.
2. Abnahmeprotokoll ausfüllen und unterschreiben lassen. Ab hier läuft die Gewährleistung.
3. Übergabeblatt übergeben. Darauf steht: welches Modul wo, Kontoinhaber, 30 Tage Hilfe, danach Pauschalen, 2 Jahre Vor-Ort-Austausch, Kontakt.
4. Um eine Google-Bewertung bitten (QR-Code auf dem Übergabeblatt).
5. Rechnung noch am selben Tag (Arbeitslohn getrennt ausweisen), Zahlungsziel 7 Tage.

### R4: Störung oder Reklamation (Antwort innerhalb von 24 h)
1. Zuhören, Fall notieren. Erste Frage: „Funktioniert der Wandschalter?“ Wenn ja, ist es kein Notfall.
2. Per Telefon/Video oder Fernzugriff (wenn freigegeben) eingrenzen: WLAN/Router neu? App-Update? Gerät offline?
3. **Mangel meiner Arbeit oder Defekt des Moduls (innerhalb von 2 Jahren)?** → kostenloser Termin, Modul tauschen, defektes Gerät über Shelly-Garantie bzw. den Händler zurückholen.
4. **Kein Mangel** (Router getauscht, Passwort geändert, Bedienung)? → in den ersten 30 Tagen gratis, danach Service-Pauschale freundlich ansagen, **bevor** du hilfst.
5. Bei Unzufriedenheit: erst lösen, dann diskutieren. Auf schlechte Bewertungen sachlich innerhalb von 48 h antworten.
6. Fall in der Kundenakte dokumentieren.

### R5: Wochenroutine (Sonntagabend, 20 min)
1. Offene Anfragen und Angebote durchgehen (R1 Schritt 5).
2. Offene Rechnungen prüfen, Zahlungseingänge buchen.
3. Material: Sind 3 Ersatz-Shellys im Auto? Sonst nachbestellen (1–3 Tage Lieferzeit).
4. Neue Shelly-Firmware? Erst am eigenen Vorführ-Board testen, dann bei Kunden einspielen (per Fernzugriff, falls freigegeben).
5. Neue Bewertungen beantworten, Referenzfotos (mit Erlaubnis) sichern.

## 5. Werkzeuge (der kleinste Satz)

| Wofür | Werkzeug | Preis | Warum |
|---|---|---|---|
| Anfragen, Kontakt | Handy mit **WhatsApp Business** + eigene Nummer bzw. Zweit-SIM | WhatsApp Business kostenlos | Panel-Käufer wünschten sich Erreichbarkeit per WhatsApp |
| Sichtbarkeit | **Google Unternehmensprofil**, **Shelly-Installateur-Karte** | kostenlos | Bewertungen sind der Haupthebel, Shelly-Karte bringt Kunden, die schon Shelly suchen |
| Termine | Google Kalender | kostenlos | Reicht für etwa 4 Termine im Monat |
| Angebote, Rechnungen, Buchhaltung | sevdesk (kostenloser Einstieg, Buchhaltung ≈19,89 €/Monat im Jahresabo) **oder** Lexware Office (S ≈7,90 €, M ≈12,90 € netto/Monat) ([sevdesk](https://sevdesk.de/ratgeber/buchhaltung-finanzen/rechnung-buchhaltung-programme/buchhaltungssoftware-kleinunternehmer-vergleich/), [Vergleich](https://kostenlose-erechnung.de/ratgeber/lexoffice-vs-sevdesk/)) | 0–20 €/Monat | Rechnungen mit Arbeitslohn-Ausweis, EÜR. Preise auf den Anbieterseiten prüfen |
| Bezahlung | Überweisung | 0 € | Nötig für § 35a EStG beim Kunden, keine Kartengebühren |
| Einrichtung beim Kunden | Shelly Smart Control App (Kundenkonto) | kostenlos | Kunde bleibt Eigentümer, du bekommst nur eine Freigabe |
| Doku | Handyfotos, ein Ordner pro Kunde (Cloud-Speicher mit Zugangsschutz) | vorhanden | Beweis bei Gewährleistung. Kundendaten sparsam halten (DSGVO) |
| Vorlagen | Angebot, Leistungsbeschreibung, Widerrufsbelehrung, Abnahmeprotokoll, Übergabeblatt, VDE-Prüfprotokoll | Muster von HWK/Innung | Einmal sauber machen, dann immer gleich |

## 6. Anmeldungen, Genehmigungen, Versicherungen (Checkliste)

| ✓ | Was | Wo / offizielle Stelle | Hinweis |
|---|---|---|---|
| ☐ | Bachelor abschließen | Hochschule | Voraussetzung für alles Weitere |
| ☐ | **Arbeitgeber über die Nebentätigkeit informieren** | Arbeitsvertrag, Personalabteilung | Wettbewerbsverbot prüfen |
| ☐ | **Eintragung in die Handwerksrolle** (Elektrotechniker) | [HWK Düsseldorf](https://gruenderplattform.de/partner/handwerkskammer-duesseldorf) | Schriftlich bestätigt, dass der Bachelor reicht. Gebühr erfragen. Kammerbeitrag im Anmeldejahr befreit, danach ermäßigt |
| ☐ | **Gewerbeanmeldung** | Stadt Willich bzw. [Wirtschafts-Service-Portal.NRW](https://www.ihk.de/duesseldorf/recht-und-steuern/querschnittfragen/gewerbeanmeldung-2596228) | ≈26 € (NRW-Gebührenordnung). Nur über offizielle Portale, Vorsicht vor bezahlten Formulardiensten |
| ☐ | **Steuerliche Erfassung beim Finanzamt** (Fragebogen über ELSTER) | Finanzamt Viersen/Kempen, zuständiges Amt prüfen | Kleinunternehmerregelung ja/nein **mit Steuerberater** entscheiden |
| ☐ | **Rentenversicherung**: Meldung innerhalb von 3 Monaten, Pflicht und Beitragshöhe klären | [Deutsche Rentenversicherung](https://www.deutsche-rentenversicherung.de/DRV/DE/Ueber-uns-und-Presse/Presse/Meldungen/2026/261109_handwerker_meldepflicht) | Siehe Kasten oben. Geringfügigkeitsgrenze bestätigen lassen |
| ☐ | **Berufsgenossenschaft (BG ETEM)**: Anmeldung innerhalb einer Woche nach Gewerbeanmeldung; klären, ob eine Unternehmer-Pflichtversicherung gilt | [BG ETEM](https://www.bgetem.de/redaktion/mitgliedschaft-beitrag/dokumente-und-dateien/befreiungsantrag-unternehmerpflichtversicherung/@@download/file/Befreiungsantrag%20Unternehmerpflichtversicherung_a11-2022.pdf), [Lexware-Leitfaden](https://www.lexware.de/wissen/gruendung/anmeldung-berufsgenossenschaft/) | Quellen widersprechen sich bei Ein-Personen-Betrieben, BG ETEM direkt fragen. Kosten noch unbekannt |
| ☐ | **Netzbetreiber: Installateurverzeichnis nötig?** | [Stadtwerke Willich Installateurportal](https://stadtwerke-service.de/installateure/installateurportal/) | Wenn ja: Nachweis der Messgeräte und Werkstattausrüstung, Prüfgerät kaufen |
| ☐ | **Betriebshaftpflicht** mit Tätigkeitsschäden, Mängelbeseitigungsnebenkosten, Aus-/Einbaukosten | Versicherungsmakler, mehrere Angebote | Schätzung 400 €/Jahr (`numbers.json`) |
| ☐ | AGB, Widerrufsbelehrung, Abnahmeprotokoll | HWK/Innung (Muster) | Kostenfreie HWK-Beratung nutzen |
| ☐ | Webseite: Impressum, Datenschutzerklärung | – | Pflicht, sobald es eine Webseite gibt |
| ☐ | Geschäftskonto | Bank | Privat und Geschäft trennen |

## 7. Risikoregister

| # | Risiko | Wie wahrscheinlich | Wie schlimm | Plan |
|---|---|---|---|---|
| 1 | Vor Ort kein Neutralleiter, Dose zu flach oder Motor passt nicht | mittel | mittel (verlorener Termin) | Foto-Check vorab (R1). Tiefe Dosen dabei. Klare Regel: Geht es nicht, kostet es den Kunden nichts, und du fährst nicht ohne Fotos raus |
| 2 | WLAN reicht nicht bis zum Fenster | mittel | mittel | Signal vorab per Handy prüfen. Repeater als Lösung, die der Kunde kauft. Ausschluss im Angebot |
| 3 | Hauptjob, Krankheit oder Urlaub kollidieren mit Terminen oder Störungen | hoch | niedrig–mittel | Der Schalter funktioniert immer, also keine Notfälle. Antwort innerhalb von 24 h ehrlich zusagen. Abwesenheit ansagen |
| 4 | Defekte Module oder Serienfehler/Firmware-Bug bei vielen Kunden | niedrig–mittel | mittel–hoch | Ersatzvorrat, Firmware gestaffelt einspielen, Garantie-Rücklage 8 €/Rollladen, Shelly-Garantie und Rückgriff beim Händler |
| 5 | Schaden beim Einbau (Motor, Dose, Tapete) oder Schmorschaden/Brand | niedrig | hoch | Saubere Arbeit, Messprotokoll, Haftpflicht mit Tätigkeitsschäden **vor** dem ersten Auftrag |
| 6 | Bestehende Anlage ist mangelhaft (kein FI, alte Leitungen) | mittel | mittel (Haftung, Streit) | Vorher prüfen, **schriftlich auf Mängel hinweisen**. Bei Gefahr nicht einbauen. Ggf. separates Angebot (z. B. FI nachrüsten) |
| 7 | Rentenversicherung, BG oder Steuern kosten mehr als geplant | mittel | mittel | Vor dem Start klären (Abschnitt 6). CFO mit echten Beiträgen neu rechnen |
| 8 | Zu wenige Anfragen (kalt 0 von 20 im Panel) | hoch | mittel (Zeit lohnt nicht) | Referenzkunden, Bewertungen, Empfehlungsbonus, Saisonstart Frühjahr. Testlauf mit Ziel ≥2 Aufträge/Monat (`cfo.md`) |
| 9 | Schlechte Bewertung oder Streit mit Kunde | niedrig–mittel | mittel | R4, schnelle Antwort, Abnahmeprotokoll und Fotos als Beleg |
| 10 | Arbeitgeber untersagt die Nebentätigkeit | niedrig–mittel | hoch | **Vor** Gewerbeanmeldung klären |
| 11 | Kunde zahlt nicht oder widerruft | niedrig | niedrig–mittel | Rechnung bei Abnahme, Zahlungsziel 7 Tage, korrekte Widerrufsbelehrung und ausdrückliche Bitte um früheren Beginn |
| 12 | Shelly-Cloud fällt aus oder Shelly ändert die App | niedrig | niedrig | Lokale Zeitpläne, Schalter funktioniert, Kunde ist Kontoinhaber |

## Offene Fragen (wer beantwortet sie)

- DRV und HWK: Rentenversicherungspflicht im Nebenerwerb, Geringfügigkeitsgrenze, Beitragshöhe in den ersten Jahren.
- BG ETEM: Muss ein Ein-Personen-Elektrobetrieb pflichtversichert sein? Was kostet das?
- Stadtwerke Willich / Netzbetreiber: Ist für diese Arbeiten der Eintrag ins Installateurverzeichnis nötig? Welche Messgeräte müssen nachgewiesen werden?
- Arbeitgeber: Ist die Nebentätigkeit erlaubt?
- Versicherungsmakler: Haftpflicht-Angebote.
- Großhändler: Firmenkonto, Preise für Shelly und Klemmen.
- HWK: Gebühr für die Eintragung, Muster-AGB, Pflicht-Prüfprotokolle für diesen Fall.
- Steuerberater: Kleinunternehmerregelung, Einkommensteuer auf den Nebenverdienst.

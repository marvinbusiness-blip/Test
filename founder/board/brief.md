# Board-Briefing (Runde 2): Smart-Home-Nachrüstung Willich (Arbeitstitel)

Dies ist die zweite Sitzung. Seit der ersten Runde gibt es zwei neue Erkenntnisse: die Antwort der Handwerkskammer und eine Wettbewerbsrecherche. Beides steht unten. Die erste Runde (Votum 2× FUND IF, 1× PASS, Schnitt 4,0) liegt in `founder/board/runde-1/board.md`. Lies sie nur, um Veränderungen zu benennen, nicht um sie zu übernehmen.

## Die Idee

- **Was:** Bestehende elektrische Rollläden (später auch Licht und Steckdosen) werden smart gemacht, indem ein Shelly-Unterputzmodul (WLAN-Relais/Rollladen-Aktor, z. B. Shelly 2PM) hinter den vorhandenen Wandschalter gesetzt wird. Leistung: Einbau, Einbindung ins WLAN des Kunden, Einrichtung der kostenlosen Shelly-App, Zeitpläne, optional Übertragung nach Apple Home oder in andere Smart-Home-Systeme, Einweisung.
- **Für wen:** Besitzer/Bewohner von Einfamilienhäusern, Reihenhäusern und Wohnungen in Willich (Niederrhein, NRW) und Umgebung, die bereits elektrische Rollläden haben. Typischer Auftrag: mehrere Rollläden pro Haushalt (z. B. 5–12).
- **Preis:** noch offen. Referenz des Gründers: Ein Elektriker hat bei einem Bekannten für 12 Shellys hinter Rollläden inkl. Einbau und Einrichtung 1.400 € berechnet (≈117 €/Rollladen).
- **Wo und wie:** Vor Ort, Willich und Umkreis. Kundengewinnung zunächst Mundpropaganda, eventuell kleine Webseite und Portale wie MyHammer.
- **Rahmen:** Nebenberuflich neben einem Vollzeitjob. Werkzeug vorhanden, Startbudget unkritisch. Gründer hat den Einbau bei Rollläden schon selbst ausprobiert, es funktioniert, er ist mit Shelly zufrieden. Start bewusst eng: nur Rollläden. Ziel jetzt: herausfinden, ob die Idee trägt; Wachstum ist später.

## Neu 1: Qualifikation und Recht

- Gründer hat eine abgeschlossene Ausbildung zum **Elektroniker für Geräte und Systeme** und schließt in Kürze den **Bachelor of Engineering Elektrotechnik** ab.
- Schriftliche Antwort der **Handwerkskammer Düsseldorf**: Der Bachelor-Abschluss Elektrotechnik gilt als gleichwertig zur Meisterprüfung. Nach Abschluss ist die Eintragung in die Handwerksrolle möglich; danach darf er das **volle Elektrotechniker-Handwerk** anbieten. Kostenfreie Beratung wurde angeboten.
- Noch offen: Bachelor ist noch nicht abgeschlossen, Eintragung noch nicht erfolgt; ob ein Eintrag ins Installateurverzeichnis des Netzbetreibers nötig ist, wurde nicht beantwortet; Betriebshaftpflicht noch nicht abgeschlossen.

## Neu 2: Wettbewerb (Details: `founder/competitors.md`)

Recherche vom 22.11.2026 aus öffentlichen Quellen über Websuche (Seiten selbst nicht direkt geöffnet, Google-Bewertungen nicht abrufbar).

- **Marktpreise für einen Rollladen inklusive Gerät, Einbau und Einrichtung:** etwa 100–190 €, Median ≈117 €. Datenpunkte: NRW-Richtwert 100–220 € (raumfaktum); Alboush-Blog-Beispiel ≈115 €; tink ≈130–140 € (grob gerechnet); ein Elektriker-Angebot im Forum 190 €; nur Montage mit Kundenmaterial ≈20 € pro Stück. Gerät allein: Shelly 2PM Gen3 ca. 16–20 €.
- **Lokale Anbieter in Willich:** Elektro Lücke GmbH (Smart Home und Gebäudesteuerung, Google 4,5 aus 32) und Elektro Michiels (im Verzeichnis unter Smart Home). Keiner nennt öffentlich Shelly-Rollläden oder einen Preis. Dazu mehrere allgemeine Elektromeister in den Ortsteilen und Notdienstportale.
- **Stärkster regionaler Wettbewerber:** Alboush Elektro, Krefeld (Nachbarstadt). VDE-Meisterbetrieb mit KNX, Homematic und Shelly, Smart-Home-Festpreise ab 669 €, Anfahrt in 36 NRW-Städten inklusive (ob Willich dazugehört, ist unklar), eigener Ratgeber zur Rollladen-Nachrüstung.
- **Überregional:** Gerlach Smart Solutions (Aschaffenburg, Shelly-Komplettservice mit Konfigurator, Funktionstest und Einweisung, Preis auf Anfrage). tink-Onlineshop mit Installationsservice durch Partner (≈200 € für 3 Aktoren, Bosch/Homematic statt Shelly). Remote-Einrichtungshilfe auf Kleinanzeigen.
- **Hersteller-Kanal:** Shelly betreibt eine Installateur-Karte (über 2.000 Installateure in DACH). Registrierte Installateure bekommen Sichtbarkeit, Schulungen und 10 % Cashback.
- **Ersatzlösungen:** Shelly selbst einbauen (16–20 € Gerät), Batterie-Funkmotor oder Gurtwickler selbst einbauen (180–220 €), Somfy- oder Rademacher-Systeme (8er-Set ≈416 €, Somfy-Komplettset ≈581 €), nichts tun, ein Bekannter macht es.
- **Was Kunden bemängeln (Foren, keine Einzelbewertungen):**
  1. Elektriker lehnen kleine Shelly-Aufträge ab oder melden sich nicht (5 Threads, überwiegend 2021–2023, bundesweit, teils andere Shelly-Geräte; z. B. eine MyHammer-Anfrage an 12 Firmen ohne eine einzige Antwort).
  2. Manche Elektriker scheuen Shelly wegen der Gewährleistung (2 Threads, dünn).
  3. Preise unklar, kaum Festpreise (dünn).
  4. Vor Ort klappt es nicht, z. B. weil der Neutralleiter fehlt (dünn).
- **Lücke laut Recherche:** ein lokaler Shelly-Spezialist in Willich mit Festpreis pro Rollladen, der kleine Aufträge annimmt und Übergabe und Support mitliefert. Die Lücke ist schmal, weil technisch jeder Elektromeister dasselbe kann.
- **Bedrohungen:** Alboush (Mindestpreis 669 € spricht eher für größere Aufträge), Willicher Betriebe mit vorhandenem Kundenstamm, neue Einträge auf der Shelly-Karte.

## Was noch niemand weiß (keine Annahmen treffen)

- Marktgröße in Willich und Umkreis (Haushalte mit elektrischen Rollläden).
- Ob und zu welchem Preis Kunden kaufen (`/founder-consumer`, `/founder-pricing`).
- Zeit pro Rollladen, Kosten pro Auftrag, Kosten der Kundengewinnung, Supportaufwand (`/founder-cfo`).
- Wie oft es vor Ort nicht passt (kein Neutralleiter, flache Dose, WLAN).

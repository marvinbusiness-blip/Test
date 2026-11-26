# Methoden, Faustregeln und Prüfpunkte

Nachschlagewerk für den Skill `immobilienbewertung`. Zahlen hier sind **Größenordnungen und Faustregeln**, keine festen Grenzwerte. Lage, Zustand und Markt schlagen jede Faustregel. Wenn ein Wert für das Urteil wichtig ist, aktuell nachschlagen.

## Inhalt
1. Vergleichswert (Wohnung, Haus)
2. Ertragswert (Mehrfamilienhaus, vermietete Objekte)
3. Sachwert (nur als Plausibilitätscheck für Häuser)
4. Kaufnebenkosten
5. Kennzahlen für Kapitalanleger und ihre Einordnung
6. Eigennutzung: Kaufen vs. Mieten, Belastung
7. Steuer bei Vermietung (vereinfacht)
8. Prüfpunkte und Risiken nach Objektart
9. Datenquellen

---

## 1. Vergleichswert

Das Hauptverfahren für Eigentumswohnungen und Ein-/Zweifamilienhäuser: Was zahlen andere für Vergleichbares?

- **Bestes Datum:** Immobilienrichtwerte und Grundstücksmarktberichte der Gutachterausschüsse. In NRW stehen Immobilienrichtwerte (€/m² für Wohnungen und Häuser, mit Umrechnung nach Baujahr, Größe, Ausstattung) kostenlos bei **BORIS-NRW**. Andere Länder haben eigene BORIS-Portale bzw. Marktberichte.
- **Zweitbestes Datum:** Angebotspreise auf Portalen (ImmoScout24, Immowelt, Kleinanzeigen) und deren Preisatlanten. **Angebotspreise liegen oft über den tatsächlichen Kaufpreisen**, sie sind eine Obergrenze, keine Mitte.
- **Anpassen für:** Baujahr und Modernisierung, Energieeffizienz, Etage/Aufzug, Balkon/Garten, Stellplatz, Mikrolage (Straße, Lärm), Grundstücksgröße beim Haus.
- **Ergebnis als Spanne**, nie als Punktwert. Lieber „ca. 3.200–3.600 €/m²“ als „3.417 €/m²“.

## 2. Ertragswert (vereinfacht nach ImmoWertV)

Das Hauptverfahren für Mehrfamilienhäuser und vermietete Objekte, bei denen der Ertrag den Preis bestimmt. Das Skript `rechner.py` rechnet es mit Sensitivität (Liegenschaftszins ±0,5 %).

```
Rohertrag (marktübliche Jahresnettokaltmiete)
− Bewirtschaftungskosten (Verwaltung, Instandhaltung, Mietausfallwagnis)
= Reinertrag
− Bodenwertverzinsung (Bodenwert × Liegenschaftszins)
= Gebäudereinertrag
× Vervielfältiger (Barwertfaktor aus Liegenschaftszins und Restnutzungsdauer)
+ Bodenwert
= Ertragswert
```

- **Bewirtschaftungskosten** (ImmoWertV Anlage 3, jährlich indexiert, aktuellen Stand prüfen): Verwaltung grob **≈350–420 € pro Wohnung und Jahr**, Instandhaltung grob **≈13–15 € pro m² Wohnfläche und Jahr** (bei alten oder schlechten Gebäuden höher), Mietausfallwagnis **2 %** des Rohertrags. Zusammen bei MFH meist **≈18–28 %** des Rohertrags.
- **Liegenschaftszins:** Kommt aus dem Grundstücksmarktbericht des örtlichen Gutachterausschusses. Für Mehrfamilienhäuser in westdeutschen Mittelstädten oft im Bereich **≈2,5–4,5 %**, in Top-Lagen niedriger, in schwachen Lagen höher. **Kleiner Zins → höherer Wert.** Ohne lokale Zahl immer die Sensitivität zeigen.
- **Restnutzungsdauer:** Gesamtnutzungsdauer Wohngebäude nach ImmoWertV 80 Jahre, minus Alter, plus Verlängerung durch Modernisierung. Ein 1965er Haus ohne große Modernisierung hat rechnerisch kaum noch Restnutzungsdauer; Gutachter setzen dann modernisierungsabhängig meist ≈20–35 Jahre an.
- **Marktübliche statt Ist-Miete:** Liegt die Ist-Miete deutlich unter oder über dem Mietspiegel, mit der marktüblichen rechnen und den Unterschied als Chance oder Risiko benennen. Mieterhöhungen sind durch Kappungsgrenze und Mietpreisbremse begrenzt.
- **Bodenwert:** Bodenrichtwert (BORIS) × Grundstücksfläche.

## 3. Sachwert (Plausibilität für Häuser)

Bodenwert + Herstellungskosten des Gebäudes nach Alter gemindert, × Marktanpassungsfaktor. Für eine schnelle Einschätzung zu aufwendig und zu ungenau ohne Normalherstellungskosten-Tabellen. Im Chat nur als grober Check: **Bodenwert allein** zeigt, welcher Teil des Preises das Grundstück ist. Wenn der Kaufpreis kaum über dem Bodenwert liegt, ist das Gebäude im Preis wenig wert (Abriss- oder Sanierungsfall?).

## 4. Kaufnebenkosten

| Posten | Höhe | Hinweis |
|---|---|---|
| Grunderwerbsteuer | **NRW 6,5 %**, **Bayern 3,5 %**, andere Länder dazwischen | Länder ändern Sätze. Für andere Länder aktuell nachschlagen. Hessen zahlt Erstkäufern einen Zuschuss (Hessengeld) |
| Notar + Grundbuch | ≈1,5–2,0 % | Mit Grundschuld eher 2 % |
| Makler | bis **3,57 %** inkl. MwSt. (Käuferanteil) | Bei Wohnungen und Einfamilienhäusern an Verbraucher: Käufer zahlt höchstens so viel wie der Verkäufer (Halbteilung). Bei MFH frei verhandelbar |

Nebenkosten zahlen Banken meist nicht mit. Faustregel: **Eigenkapital mindestens in Höhe der Nebenkosten**, besser 20 % mehr.

## 5. Kennzahlen für Kapitalanleger

| Kennzahl | Formel | Einordnung (Faustregel, Lage beachten) |
|---|---|---|
| Kaufpreisfaktor | Kaufpreis / Jahresnettokaltmiete | < 20 eher günstig, 20–25 normal, > 25–30 teuer. In Großstadt-Top-Lagen sind 30+ verbreitet, dort lebt der Kauf von Wertsteigerung |
| Bruttomietrendite | Jahreskaltmiete / Kaufpreis | ≈ 1 / Kaufpreisfaktor. Unter ≈4 % ist es bei heutigen Zinsen schwer, Cashflow zu erzielen |
| Nettomietrendite | (Miete − nicht umlagefähige Kosten − Mietausfall) / Gesamtinvestition | Sollte über dem Sollzins liegen, sonst wirkt Fremdkapital gegen dich (negativer Hebel) |
| Cashflow vor Steuern | Miete − nicht umlagefähige Kosten − Mietausfall − Rate | Negativ heißt: monatliche Zuzahlung aus eigener Tasche |
| Cashflow + Tilgung | wie oben + Tilgungsanteil | Zeigt Vermögensaufbau. Kann positiv sein, obwohl Cashflow negativ ist |
| Eigenkapitalrendite | (Jahrescashflow + Tilgung) / Eigenkapital | Ohne Wertsteigerung gerechnet, also konservativ |

**Zinsen:** Nie einen Zins erfinden. Den Nutzer fragen oder aktuelle Bauzinsen recherchieren (10 Jahre Zinsbindung) und Quelle und Datum nennen.

## 6. Eigennutzung

- **Kaufpreis in Jahreskaltmieten:** Kaufpreis / (ortsübliche Kaltmiete für die gleiche Fläche × 12). Je höher, desto mehr spricht wirtschaftlich fürs Mieten. Werte deutlich über ≈25–30 sind aus rein finanzieller Sicht teuer.
- **Echte Wohnkosten vergleichen:** Zinsen + Hausgeld bzw. Instandhaltung + entgangene Zinsen auf das Eigenkapital vs. Kaltmiete. Die Tilgung ist Sparen, keine Wohnkosten.
- **Instandhaltung beim Haus selbst einplanen:** grob **≈1–1,5 % des Gebäudewerts pro Jahr**, bei älteren Häusern mehr.
- **Belastung:** Monatliche Gesamtbelastung sollte meist **unter ≈35–40 % des Haushaltsnettoeinkommens** bleiben. Fragen, wenn es fürs Urteil zählt.

## 7. Steuer bei Vermietung (vereinfacht)

- Absetzbar: Zinsen, nicht umlagefähige Kosten, Abschreibung (AfA) auf den **Gebäudeanteil** von Kaufpreis plus Nebenkosten (nicht auf das Grundstück).
- **AfA-Satz:** 2 % für Gebäude ab Baujahr 1925, 2,5 % vor 1925, 3 % für Neubauten ab Fertigstellung 2023. Für bestimmte Neubauten gibt es zeitlich begrenzt eine degressive AfA. Aktuelle Regeln prüfen.
- **Gebäudeanteil:** Hängt vom Bodenwert ab, die Arbeitshilfe des BMF berechnet ihn. Ohne Daten 70 % annehmen und als Annahme nennen. In teuren Lagen ist er niedriger.
- Grenzsteuersatz beim Nutzer erfragen oder annehmen und nennen. Keine Steuerberatung.

## 8. Prüfpunkte nach Objektart

**Alle Objekte**
- Energieausweis und Heizung: Alter, Energieträger. Gebäudeenergiegesetz (GEG) bei Eigentümerwechsel (Nachrüstpflichten wie Dämmung oberste Geschossdecke, Austausch sehr alter Konstanttemperatur-Kessel). Bei neuer Heizung gelten die Anforderungen an erneuerbare Energien. Kosten für Sanierung einpreisen.
- Baujahr-typische Themen: 1950–70er (Elektrik, Dämmung, Fenster), 1960–80er (Asbest möglich, Flachdach), Nachkriegsbauten (Schallschutz).
- Erbbaurecht, Wegerechte, Baulasten (Baulastenverzeichnis), Altlasten.

**Eigentumswohnung**
- Hausgeld aufteilen: umlagefähig vs. nicht umlagefähig. Höhe der **Erhaltungsrücklage** gesamt und je m².
- Protokolle der Eigentümerversammlungen der letzten 3 Jahre: geplante Sanierungen, **Sonderumlagen**, Streit.
- Teilungserklärung: Sondernutzungsrechte, was gehört zur Wohnung.

**Einfamilienhaus**
- Dach, Fenster, Heizung, Leitungen: Alter und geplanter Ersatz in den nächsten 10 Jahren.
- Feuchtigkeit im Keller, Dämmung.
- Grundstück: Bodenrichtwert × Fläche vs. Kaufpreis (siehe Sachwert).

**Mehrfamilienhaus / vermietete Objekte**
- Mietliste: Ist-Miete je Wohnung vs. Mietspiegel, Leerstand, Mietrückstände, Mietdauer.
- Mietverträge: Staffel-/Indexmieten, Kautionen, Streitigkeiten.
- Instandhaltungsstau: je älter und je niedriger die Miete, desto wahrscheinlicher.
- Bei Wohnung „vermietet gekauft“ zur Eigennutzung: Eigenbedarfskündigung ist eingeschränkt und dauert.

## 9. Datenquellen (zum Recherchieren, Quelle und Datum immer nennen)

- **BORIS-NRW**: Bodenrichtwerte, Immobilienrichtwerte, Grundstücksmarktberichte (NRW). Andere Länder: BORIS-D bzw. Landesportale.
- **Grundstücksmarktbericht** des Gutachterausschusses von Kreis/Stadt: Kaufpreise, Liegenschaftszinsen, Marktanpassungsfaktoren.
- **Mietspiegel** der Stadt (falls vorhanden), sonst Mietpreisatlanten der Portale (Angebotsmieten, eher hoch).
- **Bauzinsen**: aktuelle Vergleiche von Kreditvermittlern, mit Datum.

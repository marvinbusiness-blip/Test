---
name: marktscanner
description: Durchsucht den Immobilienmarkt am Niederrhein (Willich und Umgebung) nach neuen Inseraten, die zum Suchprofil des Nutzers passen (Eigentumswohnungen bis 140.000 €, Häuser bis 350.000 €), bewertet neue Treffer kurz mit dem Skill immo, meldet nur wirklich interessante und merkt sich, was schon gemeldet wurde. Nutze diesen Skill, wenn der Marktscanner läuft (z. B. als geplante Aufgabe), oder wenn der Nutzer fragt „Gibt es was Neues?“, „Scan mal den Markt“, „Neue Wohnungen in Willich?“ oder nach aktuellen Angeboten in seinem Suchprofil.
---

# Marktscanner

Ziel: Der Nutzer soll von neuen, wirklich passenden Inseraten früh erfahren und sich nicht durch Rauschen klicken müssen. Lieber zwei gute Treffer als zehn mittelmäßige. Eine Meldung, die sich als Fehlalarm herausstellt, kostet ihn Vertrauen in den Scanner.

## Dateien
- `references/suchprofil.md`: Was gesucht wird, Region, Ausschlüsse, Quellen, Referenzwerte. **Zuerst lesen.**
- `marktscanner/gesehen.json` (im Repo): bereits gesehene Inserate. Nur Neues melden.
- `marktscanner/funde.md` (im Repo): Protokoll der gemeldeten Funde, neueste oben.
- Für die Bewertung: Skill `immo` (`.claude/skills/immo/`), vor allem `references/profil.md` und `scripts/rechner.py`.

## Ablauf eines Laufs

### 1. Neue Inserate finden
- Websuche mit mehreren gezielten Anfragen: je Objektart (Wohnung, Haus, Mehrfamilienhaus, Zwangsversteigerung) und Ort (zuerst Willich mit Ortsteilen, dann Umgebung). Suchbegriffe wie „Eigentumswohnung kaufen Willich“, „Mehrfamilienhaus kaufen Krefeld“, „Zwangsversteigerung Willich“, gern mit Portal (`site:`) oder Maklername. Bevorzuge aktuelle Treffer (Monat/Jahr im Suchbegriff).
- Seiten direkt öffnen (WebFetch) nur, wenn es erlaubt ist. Wird ein Host blockiert, nicht wiederholen, sondern mit den Suchergebnissen arbeiten. **Keine Sperren umgehen, kein Login, nur öffentlich sichtbare Angaben.**
- Halte die Zahl der Suchanfragen vernünftig (etwa 10–20 pro Lauf). Der Lauf soll zügig sein.

### 2. Vorfiltern
- Preis über dem Höchstpreis aus dem Suchprofil → weg. Ort außerhalb der Region → weg (außer außergewöhnlich gut).
- Bereits in `gesehen.json` (gleiche Exposé-Nummer, gleiche URL oder gleiche Kombination aus Ort, Fläche und Preis) → weg. Dasselbe Objekt taucht oft auf mehreren Portalen und beim Makler auf: als ein Objekt behandeln.
- Offensichtlich verkaufte oder reservierte Objekte → nur in `gesehen.json` eintragen, nicht melden.

### 3. Kurz bewerten
Für jeden neuen Kandidaten die Schnellversion des Skills `immo`. Nutze die Referenzwerte aus dem Suchprofil statt jedes Mal neu zu recherchieren. Recherchiere nur nach, wenn ein Ort neu ist oder die Werte älter als ein Jahr sind.
- €/m² (nach Abzug von Stellplatz/Möbeln, falls bekannt) gegen den Richtwert
- Wünsche: Balkon, Stellplatz, Garten, Ausrichtung (falls erkennbar), Aussicht
- Rendite ohne Kredit mit `rechner.py`, wenn eine Miete bekannt oder sinnvoll schätzbar ist
- K.-o.-Hinweise aus dem Suchprofil

Ampel wie im Skill `immo`. **Gemeldet wird nur 🟢 oder 🟡 mit klarem Grund.** 🔴 nur in `gesehen.json` eintragen.

### 4. Merken und protokollieren
- Alle geprüften neuen Inserate (auch nicht gemeldete) in `marktscanner/gesehen.json` eintragen: `id` (Portal + Exposé-Nr. oder Kurzname), `quelle` (URL), `art`, `ort`, `preis`, `flaeche`, `gesehen` (Datum), `urteil` (ein Satz).
- Gemeldete Funde oben in `marktscanner/funde.md` eintragen: Datum, Ampel, Kurzbeschreibung, Link.
- Änderungen committen und pushen, wie es die Aufgabe vorgibt (Branch dort angegeben).

### 5. Meldung an den Nutzer (die letzte Nachricht des Laufs)
**Gibt es Treffer:** Die erste Zeile lautet `🏠 [N] neue interessante Inserate`. Danach pro Treffer höchstens 4 Zeilen:

```
**[🟢/🟡] [Art], [Ort], [m²], [Preis] ([€/m²])**
[Warum interessant, 1 Satz: Preis vs. Richtwert, Rendite ohne Kredit, Wünsche erfüllt]
[Haken oder offene Frage, 1 Satz]
[Link]
```

**Keine Treffer:** nur eine Zeile, `Keine neuen passenden Inserate (geprüft: [Zahl] neue, [Zahl] aussortiert).` Nicht mehr. So entsteht nur bei echten Funden eine Benachrichtigung, die er beachten muss.

Keine erfundenen Inserate, Preise oder Links. Jede gemeldete Angabe muss aus einer gefundenen Quelle stammen. Was unsicher ist (z. B. „wahrscheinlich dasselbe Objekt wie …“), so kennzeichnen.

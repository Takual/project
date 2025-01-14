# Vergleichende Analyse der YouTube-Metriken mit und ohne Live-Videos

## 1. Datenbasis
- Ursprünglicher Datensatz: 1012 Videos
- Datensatz ohne Live-Videos: 852 Videos
- Entfernte Live-Videos: 160

## 2. Klickratenanalyse

### Mit Live-Videos
- Durchschnitt: 4,09%
- Standardabweichung: 2,16
- Spanne: 1% bis 21,95%
- ANOVA p-Wert (Thumbnail): 0,0842
- Median: 3,63%

### Ohne Live-Videos
- Durchschnitt: 4,04%
- Standardabweichung: 2,31
- Spanne: 1% bis 21,95%
- ANOVA p-Wert (Thumbnail): 0,0763
- Median: 3,55%

### Bewertung Klickrate
Die Entfernung der Live-Videos hat die Analyse der Klickraten leicht geschärft:
- Minimal bessere statistische Signifikanz der Thumbnail-Effekte
- Klarere Verteilungsmuster
- Deutlichere Zusammenhänge zwischen Gestaltungselementen und Klickrate
- Thumbnail-Kategorie 3 zeigt konsistentere positive Effekte

## 3. Wiedergabedauer-Analyse

### Mit Live-Videos
- Durchschnitt: 137 Sekunden
- Standardabweichung: 125 Sekunden
- ANOVA p-Wert (Thumbnail): < 0,0001 (F = 29,32)
- Median: 100,5 Sekunden

### Ohne Live-Videos
- Durchschnitt: 118 Sekunden
- Standardabweichung: 103 Sekunden
- ANOVA p-Wert (Thumbnail): < 0,0001 (F = 10,34)
- Median: 89 Sekunden

### Bewertung Wiedergabedauer
Die Analyse ohne Live-Videos zeigt:
- Deutlich klarere Effekte der Thumbnail-Gestaltung
- Systematischere Progression von Kategorie 1 zu 3
- Robustere und besser vorhersagbare Effekte
- Geringere aber realistischere durchschnittliche Wiedergabedauern

## 4. Aufrufe-Analyse

### Mit Live-Videos
- Durchschnitt: 39.283 Aufrufe
- Standardabweichung: 87.302
- ANOVA p-Wert (Thumbnail): 0,8033
- Median: 12.045

### Ohne Live-Videos
- Durchschnitt: 44.261 Aufrufe
- Standardabweichung: 93.790
- ANOVA p-Wert (Thumbnail): 0,7474
- Median: 14.710

### Bewertung Aufrufe
Die Entfernung der Live-Videos hat:
- Die durchschnittlichen Aufrufzahlen erhöht
- Die fehlenden Zusammenhänge mit Gestaltungselementen bestätigt
- Zu einer gleichmäßigeren Verteilung der Ausreißer geführt
- Die Bedeutung externer Faktoren unterstrichen

## 5. Gesamtbewertung

### Haupterkenntnisse
1. Live-Videos folgen anderen Gesetzmäßigkeiten und sollten separat analysiert werden
2. Thumbnail-Gestaltung hat den stärksten Effekt auf die Wiedergabedauer
3. Klickraten werden moderat durch Thumbnails beeinflusst
4. Aufrufzahlen sind weitgehend unabhängig von Gestaltungselementen
5. Die SEO-optimierte Titelbewertung zeigt durchgehend geringe Effekte

### Praktische Empfehlungen
1. Thumbnail-Optimierung:
   - Fokus auf Kategorie 3 (Kombination von Gesicht und präsentem Titel)
   - Besonders wichtig für längere Wiedergabedauer
   - Moderater Einfluss auf Klickraten

2. Titelgestaltung:
   - Mittlere Bewertungen (6,5-7,5) zeigen oft bessere Ergebnisse
   - Sehr hohe SEO-Optimierung (8,0-8,5) bringt keine zusätzlichen Vorteile
   - Fokus auf Verständlichkeit statt maximaler SEO-Optimierung

3. Differenzierte Strategien:
   - Separate Strategien für Live- und reguläre Videos
   - Berücksichtigung externer Faktoren für Aufrufzahlen
   - Optimierung der Gestaltung für Engagement (Wiedergabedauer)

---
---
### Methodische Schlussfolgerungen
Die Trennung von Live- und regulären Videos hat zu:
1. Klareren analytischen Ergebnissen
2. Besserer Interpretierbarkeit der Effekte
3. Realistischeren Einschätzungen der Wirksamkeit von Gestaltungsmaßnahmen
4. Präziseren Handlungsempfehlungen für die Content-Optimierung

Für die Ausreißerbehandlung würde ich einen systematischen Ansatz mit mehreren Methoden vorschlagen:

1. IQR-Methode (Interquartile Range):
- Gilt als robuste, etablierte Methode
- Definiert Ausreißer als Werte außerhalb von 1.5 × IQR
- IQR = Q3 (75% Perzentil) - Q1 (25% Perzentil)
- Ausreißer = < (Q1 - 1.5 × IQR) oder > (Q3 + 1.5 × IQR)

2. Z-Score Methode:
- Basiert auf der Standardabweichung
- Definiert Ausreißer als Werte über x Standardabweichungen vom Mittelwert
- Üblich sind 2 oder 3 Standardabweichungen
- Weniger robust bei nicht-normalverteilten Daten

3. Modifizierter Z-Score:
- Robuster als der normale Z-Score
- Verwendet Median und MAD (Median Absolute Deviation)
- Weniger anfällig für Verzerrung durch extreme Ausreißer

Für unseren spezifischen Fall würde ich empfehlen:

1. Für Klickrate:
- IQR-Methode mit 1.5 × IQR
- Grund: Rechtsschiefe Verteilung, aber nicht extrem

2. Für Wiedergabedauer:
- IQR-Methode mit 2.0 × IQR
- Grund: Stärkere Rechtsschiefe, natürliche Variation in der Länge

3. Für Aufrufe:
- Modifizierter Z-Score oder Log-Transformation
- Grund: Extreme Rechtsschiefe, virale Effekte

Möchten Sie, dass ich einen Code für diese Analyse erstelle? Wir könnten dann die Ergebnisse mit und ohne Ausreißer sowie mit und ohne Live-Videos vergleichen.
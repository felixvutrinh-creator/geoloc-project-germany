Englische Version unten
-----------------------------------------------------------
Ein Geolokator der mit Hilfe von Schatten- und Sonnenstandsanalyse die ungefähre Position aus einem Bild entnehmen soll.
Geplant ist eine Integration von Sentinel 2.
-----------------------------------------------------------
Dev Log

Der Schatten-Maskierer steht. Ein Otsu-Threshold soll bei einem graugestuften Bild die Schatten segmentieren. 
Beim ersten Testlauf mit einem Bild vom Jubiläumsgrat (Alpines Gelände), konnte Otsu nicht korrekt Schatten von dunklem Gestein unterscheiden. Jede Konstrastkante wurde markiert.
Otsu berechnet einen globalen Schwellenwert. Es war zu erwarten, dass er zwischen Schatten und etwas dunklerem Stein nicht unterscheiden kann. 
Nächster Ansatz wäre es ein weniger komplexes Bild zu testen, und einen adaptiven Threshold zu bauen.

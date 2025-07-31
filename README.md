Jobs_Analyz_DA
Ein moderner Data-Analytics-Workflow für die Analyse von aktuellen IT-Stellenanzeigen und die Visualisierung der Ergebnisse in einem interaktiven Power BI Dashboard.
Projekt als freiwilliges Praktikum für eine Schule, die gezielt neue Berufe ins Curriculum aufnehmen möchte.

Überblick
Das Ziel des Projekts ist die Analyse von fünf ausgewählten IT-Berufen anhand von echten Jobangeboten. Die Daten wurden selbstständig gescrapt, bereinigt, zusammengeführt und auf zwei Ebenen analysiert: quantitativ und detailliert.
Alle Ergebnisse sind im Power BI Dashboard übersichtlich visualisiert – für HRs, Schulen und Entscheider.

Features
Automatischer Web-Scraping-Prozess (Python, aiohttp, BeautifulSoup, requests)

Datensäuberung & -fusion: Alle Jobs werden vereinheitlicht und verbunden

Zwei Analyseebenen:

Quantitative Analyse (z.B. Anzahl Angebote, Gehälter, gefragte Skills)

Detaillierte Analyse (Trends, Anforderungen, usw.)

Power BI Dashboard: Mit Berufsfilter, interaktiven Grafiken und einfacher UX

Speziell abgesicherte Python-Skripte für stabiles Arbeiten (sowohl in Jupyter als auch lokal)

Zielgruppe
HR-Spezialist:innen, Recruiter

Unternehmen oder Schulen, die Weiterbildung/ Umschulung anbieten

Wie starten?
Repository klonen:

bash
Kopieren
Bearbeiten
git clone https://github.com/DmtiriyK/Jobs_Analyz_DA.git
cd Jobs_Analyz_DA/notebooks
Benötigte Libraries installieren:

bash
Kopieren
Bearbeiten
pip install -r requirements.txt
Jupyter Notebook öffnen und gewünschtes Skript ausführen (Scarp.ipynb, Cleaner.ipynb etc.)

Ergebnisse können im Power BI Dashboard (Job_analyz_DA.pbix) betrachtet werden.

Power BI Dashboard
Das Dashboard liefert interaktive Einblicke in die Berufsanalyse – Gehälter, Skills, Trends. Einfach gewünschte Profession auswählen und alle Daten sofort durchklicken! Perfekt für datenbasiertes Recruiting oder Kursplanung.

Motivation
„Ich wollte ein skalierbares, robustes Analyse-Produkt bauen, das die Arbeit von HR und Schulen wirklich einfacher macht – datengetrieben, verständlich, und mit allen State-of-the-Art Tools aus Data Science & BI!“

Fragen oder Interesse? Kontakt über GitHub

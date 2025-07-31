Jobs_Analyz_DA – Data‑Analytics‑Workflow zur Analyse von IT‑Stellenanzeigen
Diesem Projekt liegt das Ziel zugrunde, aktuelle IT‑Stellenanzeigen für Deutschland zu sammeln, zu bereinigen und zu analysieren. Das Ergebnis wird in einem interaktiven Power‑BI‑Dashboard präsentiert. Die Daten werden über verschiedene Scraper gesammelt, anschließend mit Python‑Notebooks bereinigt und schliesslich zu einer Gesamtdatenbasis zusammengeführt. In diesem Repository ist die Verzeichnisstruktur überarbeitet, um die Datenquellen nach Beruf zu sortieren und die verwendeten Notebooks nachvollziehbar zu ordnen.

Projekt‑Struktur
dashboards/ – Berichte und Power‑BI‑Dashboards.

data/ – Roh‑ und bereinigte CSV‑Dateien.

docs/ – Dokumentation (z. B. Konzept oder Bericht).

libs/ – Hilfsfunktionen und wiederverwendbare Python‑Module.

models/ – Trainierte Modelle (z. B. zur Klassifikation der Stellen).

notebooks/ – Enthält die Skripte zum Scrapen und Bereinigen der Daten (siehe unten).

reports/ – Berichte über die Ergebnisse.

scripts/ – Kleinere Helferskripte.

Ordner notebooks
Für jede der fünf untersuchten Berufsgruppen gibt es einen eigenen Unterordner. Jeder Unterordner enthält zwei verschiedene Scraper‑Notebooks (jeweils mit anderen Scrape‑Ansätzen) und ein Notebook zur Datenbereinigung. Für die Zusammenführung der bereinigten Datensätze wurde ein weiterer Ordner angelegt.

text
Kopieren
Bearbeiten
notebooks/
├─ marketing/            # Jobs im Bereich Marketing / Online‑Marketing
│  ├─ Pars.ipynb         # Scraper für Marketing‑Stellen (Indeed)
│  ├─ Scarp_m_Big.ipynb  # Scraper für Marketing‑Stellen (LinkedIn)
│  └─ Cleaner.ipynb      # Datenbereinigung der Marketing‑Daten
│
├─ tech_support/         # IT‑Support / Helpdesk
│  ├─ Pars_supp.ipynb    # Scraper für Support‑Stellen
│  ├─ Scarp_big.ipynb    # Scraper für Support‑ und System‑Stellen
│  └─ Cleaner_supp.ipynb # Datenbereinigung für Support‑Stellen
│
├─ sys_admin/            # Systemadministrator / Netzwerkadministrator
│  ├─ Scarp_big.ipynb    # Scraper für Sys‑Admin‑Stellen
│  ├─ Pars_supp.ipynb    # Alternative Scraper‑Variante
│  └─ Cleaner_supp.ipynb # Bereinigung (mangels separaten Cleaners gemeinsam mit Support)
│
├─ qa_tester/            # QA Manual Tester / Software‑Tester
│  ├─ Scarp_minim.ipynb  # Scraper für QA/Manual Tester
│  ├─ Neu_Scarp_Tester.ipynb  # Asynchroner Scraper für QA‑Stellen
│  └─ (kein spezieller Cleaner vorhanden)  # Daten werden über allgemeine Skripte bereinigt
│
├─ office_manager/       # Büro‑/Office‑Manager und Verwaltung
│  ├─ Pars_off.ipynb     # Scraper für Büro‑Stellen  
│  ├─ Scarp_buro_big.ipynb # Scraper für Büro‑Jobs (LinkedIn)  
│  └─ Cleaner.ipynb      # Nutzung des allgemeinen Cleaners
│
└─ stitchers/            # Zusammenführung aller bereinigten Daten
   ├─ Big_data.ipynb     # Fügt alle bereinigten CSVs zusammen und erstellt ein Master‑Dataset
   └─ Untitled.ipynb     # Zweite Variante der Datenfusion
Hinweise zu den einzelnen Notebooks
Scraper (Prefixed mit Pars* oder Scarp_*) sammeln Stellenanzeigen von verschiedenen Jobportalen. Die Notebooks enthalten jeweils Keyword‑Listen, mit denen die Stellenanzeigen abgefragt werden. Beispielsweise liest Pars.ipynb Marketing‑Stellen über Keywords wie “Marketing Specialist”, “Marketing Manager” oder “Digital Marketing”

github.com
, während Pars_supp.ipynb nach Support‑Begriffen wie “Technical Support Specialist”, “IT Support” oder “Kundensupport”

github.com
 sucht. Scarp_big.ipynb greift System‑Administrator‑Stellen über Keywords wie “Systemadministrator”, “Netzwerkadministrator” oder “IT‑Administrator”

github.com
 ab.

Cleaner–Notebooks bereinigen die rohen Datensätze: sie entfernen Dubletten, filtern kurze Titel heraus und bereinigen Sonderzeichen. Der Cleaner für den Support‑Bereich (Cleaner_supp.ipynb) nutzt außerdem ein Flag‑System, um typische Support‑Skills zu markieren (z. B. “support”, “helpdesk”, “linux”, “hardware”)

github.com
.

Stitcher (Big_data.ipynb) verbindet die einzelnen bereinigten CSV‑Dateien. Dabei wird jeder Zeile eine Spalte Profession hinzugefügt, um die berufliche Zuordnung zu speichern, und die Daten werden zu einer einzigen Datei ALL_QUAN_FOR_BI_RELABLED.csv zusammengeführt

github.com
.

Wie Sie die Struktur anlegen
Neue Ordner erstellen: Navigieren Sie im GitHub‑Webinterface in das Verzeichnis notebooks/ und erstellen Sie dort die Unterordner marketing, tech_support, sys_admin, qa_tester, office_manager und stitchers.

Notebooks verschieben: Für jede Berufsgruppe verschieben Sie jeweils zwei Scraper‑Notebooks und das zugehörige Cleaner‑Notebook in den entsprechenden Unterordner (siehe oben). Die Verschiebung können Sie im GitHub‑Interface über Edit → Rename durchführen; bei der Benennung der Datei geben Sie den neuen Pfad an (z. B. notebooks/marketing/Pars.ipynb).

Stitcher platzieren: Legen Sie die Notebooks Big_data.ipynb und Untitled.ipynb im Ordner stitchers/ ab.

README aktualisieren: Ersetzen Sie den bisherigen Text durch diese Datei, damit künftige Nutzerinnen und Nutzer sofort den Überblick erhalten.

Nächste Schritte
Erweiterung der Datenbasis: Ergänzen Sie für Berufsgruppen, für die nur ein Scraper existiert (z. B. Tech‑Support und Sys‑Admin), einen zweiten Ansatz, um die Datenerhebung robuster zu machen.

Verfeinerung der Bereinigung: Entwickeln Sie ggf. separate Cleaner‑Notebooks für Sys‑Admin‑ und QA‑Stellen, um besser auf die dort verwendeten Begriffe einzugehen.

Automatisierung: Die einzelnen Notebooks lassen sich zu Python‑Skripten refaktorieren und über ein Workflow‑Tool wie GitHub Actions oder Prefect automatisiert ausführen.

Dieses überarbeitete README soll Leben in das Projekt bringen und neuen Mitwirkenden einen schnellen Einstieg ermöglichen. Viel Erfolg bei der weiteren Analyse der Job‑Daten!

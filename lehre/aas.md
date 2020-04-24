---
layout: basic
linktext: Algorithmen auf Sequenzen
instructor: Prof. Dr. Sven Rahmann
---

# Vorlesung “Algorithmen auf Sequenzen”
Bachelor-Modul INF-Bsc-315 (Informatik, TU Dortmund)

## Sommersemester 2020

Wegen der COVID-19-Situation findet die Vorlesung ausschließlich online statt.
Der Vorlesungsinhalt wird per Video zur Verfügung gestellt.
Zu den Kontaktzeiten werden online Fragen beantwortet und Übungsaufgaben gemeinsam besprochen und gelöst, sowie Miniprojekte in Angriff genommen.
**Dabei wird vorausgesetzt, dass die jeweils genannten Vorlesungsvideos bereits bekannt sind!**

**Vorlesung**: Videos, freie Zeiteinteilung. Das Vorlesungsvideo muss aber **vor** der entsprechenden Kontaktzeit gesehen worden sein!\\
**Kontaktzeiten**: jeweils **Donnerstags 08:30-10:00** per Big Blue Button. Den Zugangslink und Passwort erhalten Sie nach Anmeldung im LSF.\\
**Material**: [Skript-Entwurf](aas20/skript.pdf)\\
**Prüfungen**: Es werden nur mündliche Prüfungen angeboten. Es ist kein Leistungsnachweis notwendig zur Prüfungsanmeldung. Prüfungstermine stehen noch nicht fest. Es ist vorgesehen, Präsenzprüfungen durchzuführen.

Zur Teilnahme an den Sitzungen am Donnerstag 08:30 - 10:00 Uhr ist ein BigBlueButton-Zugangslink und ggf. ein Passwort erforderlich. Sie erhalten dies vom Veranstalter per email nach Ihrer Anmeldung im LSF.

| Do 23.04. | **Videos (werden vorausgesetzt!):**<br/>  01. [Einführung, Definitionen und Begriffe](https://www.youtube.com/watch?v=OzhP9uLP24g);<br/> 02. [naiver Algorithmus zur exakten Mustersuche](https://www.youtube.com/watch?v=RhGC23lfY2U).<br/> **Aufgaben:** [Blatt 1](aas20/01). |
| Do 30.04. | **Videos:**<br/> 03. [Exakte Mustersuche mit nichtdeterministischen endlichen Automaten, Shift-And-Algorithmus](https://www.youtube.com/watch?v=7xt6ZtwSyyg). <br/> **Aufgaben:** [Blatt 2](aas20/02). |
| Do 07.05. | **Videos:**<br/> 04. [Exakte Mustersuche mit deterministischen endlichen Automaten, Knuth-Morris-Pratt-Algorithmus](https://www.youtube.com/watch?v=WDDj1DrjnoY).<br/> **Aufgaben:** [Blatt 3](aas20/03). |
| Do 14.05. | **Videos:**<br/> 05. [Exakte Musterusche mit sublinearen Algorithmen, Horspool-Algorithmus und BNDM]().<br/> **Aufgaben:** [Blatt 4](aas20/04). |
| Do 21.05. | **Videos:** Algorithmen für die exakte Mustersuche mit Mengen von Mustern; verallgemeinerter Shift-And-Algorithmus, Aho-Corasick-Algorithmus. |
| Do 28.05. | **Videos:** Suche nach erweiterten Mustern, Verallgemeinerungen des Shift-And-Algorithmus; O-Notation, Bitoperationen, population count, Rank-Datenstruktur auf Bitarrays |
| Do 04.06. | **Videos:** Volltext-Indexdatenstrukturen: Suffixbäume, Algorithmus von Ukkonen, Anwendungen |
| Do 11.06. | **Videos:** Volltext-Indexdatenstrukturen: Suffixarrays, SAIS-Algorithmus, Anwendungen |
| Do 18.06. | **Videos:** Burrows-Wheeler-Transformation (BWT), Backward Search |
| Do 25.06. | **Videos:** Rank-Datenstruktur auf Bitarrays, FM-Index, Waveletbäume | 
| Do 02.07. | **Videos:** Distanzmaße zwischen Strings, Fehlertolerante Mustersuche, Four-Russians-Trick |
| Do 09.07. | **Videos:** Sequenzalignment |
| Do 16.07. | **Videos:** Erweiterungen zum Sequenzalignment |

---

## Inhalt (Vorlesungskommentar)

Das folgende Problem ist aus den Einführungsvorlesungen bekannt: Gegeben ist ein Text T und ein Muster P. Liste alle Positionen in T auf, an denen P vorkommt.

Von diesem Problem gibt es viele Varianten: Statt aus einem einzelnen String kann P aus einer Menge von Strings bestehen, oder in impliziter Form gegeben sein, etwa durch einen regulären Ausdruck, oder eine sogenannte position weight matrix, oder auch durch eine kontextfreie Grammatik. Zudem suchen wir unter Umständen auch nach approximativen Vorkommen im Text (z.B. Meier vs. Mayer). Vielleicht wollen wir auch nur wissen, ob P überhaupt vorkommt, oder auch nur, wie oft (ohne alle Positionen aufzulisten).

Auch die Frage nach der Statistik der Anzahl der Vorkommen ist von Interesse: Angenommen, wir beobachten ein bestimmtes Muster siebzehn mal in einem bestimmten Text: Ist das überraschend oft, oder lässt sich das durch puren Zufall erklären?

Die biologische Sequenzanalyse hat sich aus den Gebiet des pattern matching entwickelt, das in den 70er Jahren vor allem von theoretischen Informatikern bearbeitet wurde. Hier ist in den letzten 20 Jahren eine Fülle von (sowohl sehr einfachen als auch sehr komplizierten) Algorithmen entstanden, und es stellt sich heraus, dass die Algorithmen, “die man so kennt”, in der Praxis häufig langsam sind.

In der Vorlesung werden wir Varianten des Pattern Matching Problems ausführlich behandeln und sowohl klassische als auch die zur Zeit in der Praxis schnellsten Algorithmen kennen lernen. Es geht sowohl um on-line Algorithmen (bei denen der Text vorher nicht bekannt sein muss) als auch um Index-basierte Verfahren (bei denen vorher ein Index des Textes erstellt wird). Index-basierte Verfahren sind heute sowohl bei der Analyse von Biosequenzen wichtig, als auch für web-basierte Suchmaschinen wie Google oder Bing ein essentieller Bestandteil des Kerngeschäfts.

In letzter Zeit nimmt die Bedeutung komprimierter Text-Inidizes stetig zu. Hierzu werden wir die wichtigsten Grundlagen kennen lernen und vor allem die zentrale Rolle der Burrows-Wheeler Transformation herausarbeiten.

Dem ersten Teil der Vorlesung liegt das Buch **Flexible Pattern Matching in Strings** von Gonzalo Navarro und Mathieu Raffinot zu Grunde. Es wird ergänzt durch Übersichtsartikel aus der Originalliteratur, die ich in der Vorlesung angeben werde. Zur Vorlesung wird ein Skript zur Verfügung gestellt.

Die Vorlesung wird von praktischen und theoretischen Übungsaufgaben begleitet, deren Bearbeitung wichtig für ein richtiges Verständnis des Stoffs ist. Im Anschluss an diese Vorlesung besteht bei Begabung und Interesse die Möglichkeit, in diesem Bereich eine Abschlussarbeit zu schreiben.

### Literatur

Gonzalo Navarro, Mathieu Raffinot\\
**Flexible Pattern Matching in Strings**\\
Cambridge University Press\\
ISBN: 0-521-03993-2

Dan Gusfield\\
**Algorithms on Strings, Trees and Sequences**\\
Cambridge University Press\\
ISBN: 0-521-58519-8

David Sankoff und Joseph P. Kruskal\\
**Time Warps, String Edits, and Macromolecules**\\
University of Chicago Press\\
ISBN: 1-575-86217-4\\
(Taschenbuchausgabe von 2000 des 1983 erschienenen Originals)

Weitere Originalliteratur (wissenschaftliche Aufsätze, “paper”), die im Lauf der Vorlesung bekannt gegeben wird.

---

## Prüfungsleistungen

* Bachelor-Wahlmodul (2V+1Ü; 4 LP); erweiterter Umfang für Studierende der RUB (5 CP)
* mündliche Prüfung von 20-30 Minuten Dauer oder Klausur von 90 Minuten Dauer
* Die genaue Prüfungsform wird abhängig von der Teilnehmerzahl kurz nach Vorlesungsbeginn festgelegt.
* Vordruck für die Prüfungsanmeldung ausfüllen, bei Frau Jankord (OH14 / R2.39) einen Termin/Uhrzeit geben lassen, von Prof. Rahmann oder Frau Jankord unterschreiben lassen; wird von Frau Jankord zur Prüfungsverwaltung geschickt.
* Bei Fragen wenden Sie sich bitte per e-mail an den Veranstalter.


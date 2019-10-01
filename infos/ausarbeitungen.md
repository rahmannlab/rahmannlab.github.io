---
layout: basic
linktext: Ausarbeitungen / Write-ups
description: Hinweise zu Ausarbeitungen
who: Bachelor- und Masterstudierende
order: 16
---

# Hinweise zu Ausarbeitungen

Bevor Sie eine Ausarbeitung zu einem Proseminar oder Seminar bei mir abgeben, stellen Sie bitte sicher, dass Sie alle Hinweise auf dieser Seite gelesen und befolgt haben.

<b>Ihre Abgabe muss von folgender Erklärung begleitet werden:</b>
> Ich habe die Hinweise zu Seminar-Ausarbeitungen auf [URL] vom [Datum] gelesen, verstanden, und in meiner Ausarbeitung beachtet.

Bei Abschlussarbeiten (Bachelor, Master) sind jeweils besondere Formalitäten zu beachten. Bitte lesen Sie dazu frühzeitig die Prüfungsordnungen!

## Wissenschaftliches Schreiben

Seminararbeiten und Abschlussarbeiten sind wissenschaftliche Arbeiten, an die es besondere formale und inhaltliche Anforderungen gibt.
Im Rahmen eines Proseminars haben Sie normalerweise zum ersten Mal Kontakt mit einer wissenschaftlichen Ausarbeitung.
Im Rahmen eines (Haupt)seminars können Sie diese Form weiter einüben.
Bei einer Abschlussarbeit erwarte ich, dass Sie mit den Anforderungen vertraut sind. Zum Nachschlagen sind hier einige Links aufgeführt.

* [The Science of Scientific Writing](https://cseweb.ucsd.edu/~swanson/papers/science-of-writing.pdf)


## Titelseite

Die Titelseite muss folgende Informationen enthalten:
* Name des Seminars (z.B. Aktuelle Themen der Bioinformatik)
* Semester, in dem Sie das Seminar belegt haben (z.B. Sommersemester 2019)
* An welchem Institut, mindestens, an welcher Uni? (z.B. Fakultät für Informatik, Lehrstuhl XI, TU Dortmund)
* optional: bei wem? (z.B. bei Prof. Rahmann)
* Titel Ihrer Ausarbeitung
* Ihr Name (Sie müssen <b>nicht</b> Ihre Matrikelnummer auf der Titelseite angeben, wenn Sie Datenschutz-Bedenken haben. In dem Fall muessen Sie mir Ihre Matrikelnummer separat mitteilen, etwa in einer e-mail.)
* Datum der Abgabe
* Wenn Sie im Seminar einen bestimmten wissenschaftlichen Artikel vorstellen, dann: Angaben zu diesem Artikel (Autoren, Titel, Details zur Veröffentlichung wie im Literaturverzeichnis)
* optional: eine Kurzzusammenfassung (evtl in Kombination mit dem obigen Punkt)
* Da Sie die Arbeit als Privatperson schreiben, gehören auf die Titelseite aus meiner Sicht <b>keine Logos</b> der Universität. Das Rektorat der TU Dortmund ist allerdings damit einverstanden, dass das TU-Dortmund-Logo verwendet wird.

## Gliederung

* Bei kurzen Ausarbeitungen (bis ca. 20 Seiten) ist ein Inhaltsverzeichnis <b>nicht erforderlich</b>.
* Insbesondere fast schon lächerlich sind Abbildungs- und Tabellenverzeichnis bei einer Arbeit unter 100 Seiten (es sei denn, die Arbeit besteht fast ausschließlich aus Tabellen und Abbildungen).
* Im Normalfall beginnt eine wissenschaftliche Ausarbeitung mit einem Abschnitt &#8220;Einleitung&#8221; oder &#8220;Introduction&#8221;.
* Eine Arbeit endet i.d.R. mit einer kritischen Diskussion; evtl. noch gefolgt von einer kurzen Zusammenfassung.
* Nach dem letzten Satz folgt das Literaturverzeichnis; im Bedarfsfall dahinter noch Anhänge.
* Wer A sagt, muss auch B sagen: Wenn es also einen Abschnitt <i>n</i>.1 gibt, muss es mindestens auch einen Abschnitt <i>n</i>.2 geben. Ansonsten brauchen Sie den ja ersten Unterabschnitt nicht! Ein Abschnitt muss keine Unterabschnitte haben.
* Stellen Sie sicher, dass die Überschrift eines Abschnitts zum Inhalt passt.
* So ist es in Ordnung:
~~~
1 Einleitung
    (Überblick über die einzelnen Unterabschnitte des ersten Kapitels)
    1.1 Die DNA-Struktur
        (Hier folgt Text zur DNA-Struktur)
    1.2 DNA-Strukturvorhersage
        (Hier Text zur Problematik der DNA-Strukturvorhersage)
    1.3 Formale Problemstellung
        (Hier geben Sie die formale Problemstellung an, die im weitern Verlauf der Arbeit untersucht wird. Jeder vernünftige Mensch erwartet jetzt selbstverständlich, dass das untersuchte Problem etwas mit DNA-Strukturvorhersage zu tun hat.)
2 Statistische Modellierung
    (hier folgen viele weitere Abschnitte und Unterabschnitte)…
...
6 Diskussion
(7 Zusammenfassung)
Literaturverzeichnis
~~~


### LaTeX-Hinweise

Um ein gutes Schriftbild, eine konsistente Nummerierung und korrekte Referenzierungen innerhalb des Dokuments zu erreichen, wird dringend empfohlen, für die Ausarbeitung LaTeX zu verwenden.
Insbesondere lasse ich die Ausrede: &#8220;Ich konnte die Formel nicht korrekt darstellen, weil meine Textverarbeitung das nicht kann&#8221; nicht gelten.
Nutzen Sie also ggf. die Gelegenheit, LaTeX zu lernen oder ihre Kenntnisse zu erweitern. LaTeX selbst hat ein paar Fallstricke; daher hier einige Hinweise.

* Die Ausarbeitung erfolgt mit dem Schriftsatzsystem LaTeX. Sie müssen Ihr Kapitel in ein Versionskontrollsystem (git repository) einchecken. URL, Benutzernamen und Passwort erfahren Sie bei der Vorbesprechung oder beim ersten Termin. Dort finden Sie auch ein Beispielkapitel.
* Beachten Sie unter der angegebenen URL unbedingt die README-Datei.
* Achtung! LaTeX erfordert ggf. eine längere Einarbeitungszeit. Machen Sie sich daher frühzeitig mit den grundlegenden Befehlen und Funktionen vertraut. Dabei hilft Ihnen eine Beispiel-Vorlage.
* Wenn Sie diese Hinweise nicht verstehen, schauen Sie in ein LaTeX-Handbuch bzw. in eine Internet-basierte LaTeX-Hilfe.
* Wenn Sie im Text manuelle Zeilenumbrüche verwenden, machen Sie etwas falsch. Es sollte (außerhalb von center- und table-Umgebungen) fast nie nötig sein, &#8220;\\&#8221; zu verwenden.
* Benutzen Sie zur Textauszeichnung nicht direkt Befehle wie \textit, \textbf, sondern definieren Sie logische Makros, die Ausdrücken, was Sie wollen. Sollen z.B. alle Fremdwörter und neu definierten Begriffe kursiv erscheinen, definieren Sie zwei getrennte Makros, etwa \newcommand{\fremdwort}[1]{\textit{#1}} und analog für \neudefiniert. Damit können Sie das Erscheinungsbild getrennt anpassen.
* Verwenden Sie für große Abbildungen und Tafeln unbedingt die vorgesehenen Umgebungen figure und table, vorzugsweise mit Parameter \[t!\] (für top = oben auf der Seite). Versuchen Sie nicht, diese direkt in den Text zu setzen; damit bekommen Sie grausige Seitenumbrüche.
* Mathematik (Formeln, Gleichungen, etc.) kommen in eine Mathe-Umgebung, entweder $&#8230;$ im Text, oder \[ &#8230; \] für abgesetzte Formeln. Das gilt auch für einzeln genannte Variablen. Beispiel: &#8220;Sei $x$ ein $n$-dimensionaler Vektor&#8221; wird dann dargestellt als Sei _x_ ein _n_-dimensionaler Vektor. Vergisst man die $-Zeichen, werden die Variablen fälschlicherweise nicht kursiv dargestellt.
* Auch abgesetzte Formeln oder Gleichungen (ob nun mit Nummer oder ohne) sind normalerweise Bestandteil von Sätzen im Text; entsprechend ist die Interpunktion anzupassen. Lassen Sie eine Formel nicht einfach im &#8220;leeren Raum&#8221; schweben! Korrektes Beispiel:
  Die Anzahl der Wörter der Länge _q_ einer Sequenz _s_ der Länge _n_ beträgt
<div style="text-align: center;">
      <i>Q<sub>s</sub></i> = <i>n</i> &#8211; <i>q</i> + 1.
</div>

* Beachten Sie den Punkt am Ende des Satzes. Beachten Sie, dass vor der Formel kein Satzzeichen steht; der Satz geht mit der Formel einfach weiter. 
* Wenn Sie eine Variable einführen, tun Sie es an der richtigen Stelle! Angenommen, Sie wollen die Länge einer Sequenz _s_ mit _L<sub>s</sub>_ bezeichnen.
Falsch: Die Länge der Sequenz _L<sub>s</sub>_ lässt sich wie folgt berechnen: &#8230;
Richtig: Die Länge _L<sub>s</sub>_ der Sequenz _s_ berechnet sich als _L<sub>s</sub>_ = &#8230;
* LaTeX hat für viele mathematische Operationen (wie Maximum) vordefinierte Befehle (wie \max). Achten Sie darauf, diese auch zu verwenden. Insbesondere wird max nicht kursiv geschrieben. Dasselbe gilt für bekannte Funktionen, wie log, exp, sin, und so weiter, die man mit \log, \exp, \sin bekommt.
* Es gilt also: Variablen werden kursiv geschrieben (dies tut die Mathe-Umgebung), Operatoren und spezielle Funktionsnamen nicht. Bei der Verwendung von Indexen kommt es darauf an, ob der Index selbst eine Variable oder einfach ein Name ist. Beispiel: _x<sub>i</sub>_ ist das _i_-te Element von _x_ (kursiv), aber: die Driftzeit _t_<sub>D</sub> und die Retentionszeit _t_<sub>R</sub> (D und R stehen für Drift und Retention). Hier ist innerhalb der Mathe-Umgebung mit \text{} oder zur Not mit \mbox{} zu arbeiten.


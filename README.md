# Sicherheitsrichtlinien & Basis-Setup

Herzlich willkommen! Dieses Repository bündelt alle wichtigen Sicherheitsrichtlinien und bricht das oft komplexe Thema so herunter, dass auch Programmier-Lehrlinge und Einsteiger ohne Vorkenntnisse sofort durchsteigen.

Weil herkömmliche Repository-Anleitungen oft zu technisch geschrieben sind oder mit unklaren Beispielen mehr Fragen aufwerfen als sie beantworten, setzt dieses Projekt auf maximale Klarheit, echtes Verständnis und Schritt-für-Schritt-Anleitungen auf Augenhöhe.

Darüber hinaus haben wir dieses Repository mit dem offiziellen GitHub Docs-Projekt verknüpft und erweitert, um direkten Zugriff auf die vollständigen, öffentlichen Dokumentationen von GitHub zu bieten. So hast du alle offiziellen Anleitungen, Erklärungen und Workflows direkt an einem Ort gesammelt.

---

## 1. GitHub-Account absichern (Das Fundament)

Bevor du mit diesem Repository arbeitest oder eigene Projekte startest, sichern wir deinen GitHub-Account ab:

### Sicheres Passwort erstellen
* **Passwort-Manager nutzen:** Verwende einen Passwort-Manager, um ein langes, zufälliges und einzigartiges Passwort zu generieren (mindestens 16 Zeichen mit einer Mischung aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen).
* **Keine Wiederverwendung:** Nutze dieses Passwort ausschließlich für GitHub und nirgendwo sonst.

### Zwei-Faktor-Authentifizierung (2FA) aktivieren
Die Zwei-Faktor-Authentifizierung schützt dein Konto selbst dann, wenn dein Passwort in falsche Hände gerät.
1. Logge dich bei GitHub ein und klicke oben rechts auf dein Profilbild.
2. Gehe in die **Security settings** (Sicherheitseinstellungen).
3. Scrolle zum Bereich **Two-factor authentication** und klicke auf *Enable two-factor authentication*.
4. Wähle eine Authentifizierungs-App (z. B. Google Authenticator, Aegis oder Bitwarden Authenticator) und scanne den QR-Code mit deinem Smartphone.
5. Gib den generierten 6-stelligen Code ein, um die Einrichtung abzuschließen.

### Wiederherstellungs-E-Mail eintragen
Stelle sicher, dass eine aktuelle und erreichbare E-Mail-Adresse hinterlegt ist, falls du den Zugriff auf deine primäre Adresse verlierst.
1. Gehe in die GitHub **Email Settings**.
2. Füge deine primäre und eine alternative Wiederherstellungs-E-Mail-Adresse hinzu und bestätige diese über den Link in der Bestätigungsmail.

### Wiederherstellungscodes (Recovery Codes) erstellen und speichern
Falls du dein Smartphone verlierst und keinen Zugriff mehr auf deine Authentifizierungs-App hast, sind diese Codes deine einzige Rettung.
1. Gehe zu den Sicherheitseinstellungen.
2. Suche den Bereich für deine **2FA-Wiederherstellungscodes** und klicke auf *View recovery codes* (bzw. generiere sie neu).
3. **Wichtig:** Lade die Codes als Textdatei herunter oder drucke sie aus. Bewahre sie an einem sicheren Ort auf (niemals unverschlüsselt in der Cloud oder im Projekt-Repository speichern!).
> **Der absolute Worst-Case-Tipp:** Schreib dir am besten 3 dieser Codes zusätzlich auf einen physischen Zettel und verstaue ihn sicher an einem Ort, den du immer erreichen kannst (zum Beispiel im Geldbeutel oder in einem sicheren Dokumentenordner zu Hause). Wenn der Ernstfall eintritt und das Handy kaputtgeht, bist du ohne physischen Notfallcode komplett ausgesperrt.

### Passkey einrichten und speichern
Passkeys ermöglichen dir eine passwortfreie und hochsichere Anmeldung (z. B. über den Fingerabdruck auf deinem Smartphone, Windows Hello oder einen physischen Sicherheitsschlüssel wie YubiKey).
1. Gehe zu den Sicherheitseinstellungen.
2. Suche den Bereich **Passkeys** und klicke auf *Add a passkey*.
3. Folge den Anweisungen deines Betriebssystems oder Browsers, um den Passkey zu registrieren und auf deinem Gerät zu speichern.

---

## 2. Vorbereitung (Lokales Terminal)

Da du mit Git und Repositories arbeiten wirst, richten wir die grundlegende Umgebung auf deinem Rechner ein, damit du bereit für den ersten Klon (`git clone`) bist.

1. **Git Bash oder PowerShell öffnen:** Starte dein Terminal auf deinem Lenovo ThinkPad in deinem Workspace-Ordner.
2. **Prüfen, ob Git bereit ist:**
   ```bash
   git --version

---

## 3. Offizielle GitHub Open-Source-Dokumentation

Dieses Repository ist eng mit den offiziellen Open-Source-Dokumentationen von GitHub verknüpft, um direkten Zugriff auf alle standardisierten Anleitungen zu haben:

* **Offizielles GitHub Docs Repository:** [github.com/github/docs](https://github.com/github/docs) – Hier findest du den vollständigen Quellcode und die Markdown-Dateien, mit denen GitHub seine offizielle Hilfe betreibt.
* **Öffentliche GitHub Hilfe:** [docs.github.com](https://docs.github.com) – Die Live-Ansicht für alle Anleitungen zu Workflows, Sicherheitsfeatures und Account-Einstellungen.

---

## 4. Struktur der Dokumentation

Hier definieren wir die Ablage für spezifische Anleitungen:
* `/docs` – Lokale Ablage für eigene Schritt-für-Schritt-Anleitungen und Sicherheits-Workflows.
* Offizielle externe Referenzen (wie [GitHub Docs](https://docs.github.com)) für standardisierte Prozesse.

# I. Steps file - Comment ca marche ?

## I. Lancement de LanguageTool en serveur LOCAL

### ÉTAPE 1 — Installer Java (obligatoire)

Pour ce projet, il est necessaire d'installer et d'avoir la version 17 de java

Vérifier :

```bash
java -version
```

### ÉTAPE 2 — Télécharger LanguageTool MANUELLEMENT

Depuis le navigateur:
👉 [https://languagetool.org/download/](https://languagetool.org/download/)

Télécharge :

```
LanguageTool-5.7.zip
```

Puis :

```bash
unzip LanguageTool-5.7.zip
cd LanguageTool-5.7
```

## ÉTAPE 3 — Lancer le serveur LanguageTool

```bash
java -cp languagetool-server.jar org.languagetool.server.HTTPServer --port 8081
```

Resultat attendu:

```
Starting LanguageTool HTTP server on port 8081
```

## II. Lancement de l'API fastAPI

faire la configuration suivante

```bash
# acceder au repertoire backend
cd backend

# activer l'environement virtuelle
python -m venv venv
source venv/bin/activate

# insaller les dependances via le fichier requirements.txt
pip install -r requirement.txt
```

puis lancer le server a partir de cette commande

```bash
uvicon app.main:app --reload
```

## III. Lancement de l'interface dans le navigateur

pour cella, il suffit de ce placer dans le repertoire `frontend`
puis lancer la commande suivante ou double cliquer sur le fichier `index.html`

```bash
firefox index.html
```

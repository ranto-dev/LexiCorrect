# 📦 Installation OFFLINE du Frontend React + Three.js

## 📁 Structure des dossiers

```
votre-projet/
│
├── index_offline.html          # Votre fichier principal
│
└── libs/                        # Dossier des bibliothèques
    ├── react.production.min.js
    ├── react-dom.production.min.js
    ├── babel.min.js
    ├── three.min.js
    └── axios.min.js
```

---

## 🔽 Téléchargement des bibliothèques

### Méthode 1 : Téléchargement manuel (RECOMMANDÉ)

Téléchargez ces fichiers et placez-les dans le dossier `libs/` :

#### 1️⃣ React (18.2.0)
**Fichier:** `react.production.min.js`
```
https://unpkg.com/react@18/umd/react.production.min.js
```
- Ouvrez ce lien dans votre navigateur
- Clic droit → "Enregistrer sous..."
- Nommez: `react.production.min.js`
- Placez dans: `libs/`

#### 2️⃣ React DOM (18.2.0)
**Fichier:** `react-dom.production.min.js`
```
https://unpkg.com/react-dom@18/umd/react-dom.production.min.js
```
- Même procédure
- Nommez: `react-dom.production.min.js`

#### 3️⃣ Babel Standalone
**Fichier:** `babel.min.js`
```
https://unpkg.com/@babel/standalone/babel.min.js
```
- Téléchargez
- Nommez: `babel.min.js`

#### 4️⃣ Three.js (0.159.0)
**Fichier:** `three.min.js`
```
https://unpkg.com/three@0.159.0/build/three.min.js
```
- Téléchargez
- Nommez: `three.min.js`

#### 5️⃣ Axios
**Fichier:** `axios.min.js`
```
https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js
```
- Téléchargez
- Nommez: `axios.min.js`

---

### Méthode 2 : Script automatique (Windows)

Créez un fichier `telecharger_libs.bat` :

```batch
@echo off
echo ========================================
echo Telechargement des bibliotheques...
echo ========================================

mkdir libs 2>nul

echo [1/5] Telechargement de React...
curl -o libs/react.production.min.js https://unpkg.com/react@18/umd/react.production.min.js

echo [2/5] Telechargement de React DOM...
curl -o libs/react-dom.production.min.js https://unpkg.com/react-dom@18/umd/react-dom.production.min.js

echo [3/5] Telechargement de Babel...
curl -o libs/babel.min.js https://unpkg.com/@babel/standalone/babel.min.js

echo [4/5] Telechargement de Three.js...
curl -o libs/three.min.js https://unpkg.com/three@0.159.0/build/three.min.js

echo [5/5] Telechargement de Axios...
curl -o libs/axios.min.js https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js

echo.
echo ========================================
echo Telechargement termine !
echo ========================================
pause
```

Double-cliquez sur `telecharger_libs.bat` pour lancer le téléchargement.

---

### Méthode 3 : Script automatique (Mac/Linux)

Créez un fichier `telecharger_libs.sh` :

```bash
#!/bin/bash

echo "========================================"
echo "Téléchargement des bibliothèques..."
echo "========================================"

mkdir -p libs

echo "[1/5] Téléchargement de React..."
curl -o libs/react.production.min.js https://unpkg.com/react@18/umd/react.production.min.js

echo "[2/5] Téléchargement de React DOM..."
curl -o libs/react-dom.production.min.js https://unpkg.com/react-dom@18/umd/react-dom.production.min.js

echo "[3/5] Téléchargement de Babel..."
curl -o libs/babel.min.js https://unpkg.com/@babel/standalone/babel.min.js

echo "[4/5] Téléchargement de Three.js..."
curl -o libs/three.min.js https://unpkg.com/three@0.159.0/build/three.min.js

echo "[5/5] Téléchargement de Axios..."
curl -o libs/axios.min.js https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js

echo ""
echo "========================================"
echo "Téléchargement terminé !"
echo "========================================"
```

Rendez-le exécutable et lancez-le :
```bash
chmod +x telecharger_libs.sh
./telecharger_libs.sh
```

---

### Méthode 4 : Python (multiplateforme)

Créez un fichier `telecharger_libs.py` :

```python
import urllib.request
import os

print("=" * 50)
print("Téléchargement des bibliothèques...")
print("=" * 50)

# Créer le dossier libs
os.makedirs('libs', exist_ok=True)

libs = {
    'react.production.min.js': 'https://unpkg.com/react@18/umd/react.production.min.js',
    'react-dom.production.min.js': 'https://unpkg.com/react-dom@18/umd/react-dom.production.min.js',
    'babel.min.js': 'https://unpkg.com/@babel/standalone/babel.min.js',
    'three.min.js': 'https://unpkg.com/three@0.159.0/build/three.min.js',
    'axios.min.js': 'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'
}

for i, (filename, url) in enumerate(libs.items(), 1):
    print(f"[{i}/{len(libs)}] Téléchargement de {filename}...")
    urllib.request.urlretrieve(url, f'libs/{filename}')
    print(f"    ✓ {filename} téléchargé")

print("\n" + "=" * 50)
print("Téléchargement terminé !")
print("=" * 50)
```

Lancez avec :
```bash
python telecharger_libs.py
```

---

## ✅ Vérification de l'installation

Après téléchargement, votre structure devrait ressembler à :

```
votre-projet/
│
├── index_offline.html
│
└── libs/
    ├── react.production.min.js      (≈ 6 KB)
    ├── react-dom.production.min.js  (≈ 130 KB)
    ├── babel.min.js                 (≈ 2.5 MB)
    ├── three.min.js                 (≈ 600 KB)
    └── axios.min.js                 (≈ 15 KB)
```

**Taille totale : environ 3.3 MB**

---

## 🚀 Utilisation

### Étape 1 : Vérifier la structure
```
votre-projet/
├── index_offline.html
└── libs/
    └── (5 fichiers .js)
```

### Étape 2 : Configurer l'API
Ouvrez `index_offline.html` et cherchez la ligne (environ ligne 650) :
```javascript
const API_URL = 'http://localhost:8000/api/corriger';
```
Modifiez selon votre backend FastAPI.

### Étape 3 : Lancer
**Option 1 : Double-clic**
- Double-cliquez sur `index_offline.html`
- S'ouvre dans votre navigateur

**Option 2 : Serveur local**
```bash
# Dans le dossier du projet
python -m http.server 8080

# Puis ouvrez : http://localhost:8080/index_offline.html
```

### Étape 4 : Démarrer le backend
```bash
# Assurez-vous que votre backend FastAPI est lancé
uvicorn main:app --reload --port 8000
```

---

## 🧪 Test sans backend

Pour tester l'interface SANS backend :

1. Ouvrez `index_offline.html`
2. Entrez du texte
3. Cliquez sur "Corriger"
4. Vous verrez un message d'erreur (normal, pas de backend)
5. Les animations 3D doivent fonctionner !

---

## 🐛 Dépannage

### Problème : Les fichiers ne se chargent pas

**Erreur dans la console :**
```
Failed to load resource: net::ERR_FILE_NOT_FOUND
```

**Solutions :**
1. Vérifiez que le dossier `libs/` existe
2. Vérifiez que les 5 fichiers sont présents
3. Vérifiez les noms des fichiers (pas d'espace, pas de majuscules)
4. Utilisez un serveur local au lieu d'ouvrir directement le fichier

### Problème : Three.js ne fonctionne pas

**Solutions :**
1. Vérifiez que `three.min.js` est bien téléchargé
2. Ouvrez la console (F12) et regardez les erreurs
3. Essayez avec un navigateur moderne (Chrome, Firefox, Edge)

### Problème : Babel ne compile pas le JSX

**Solutions :**
1. Vérifiez que `babel.min.js` est présent
2. Utilisez un serveur local (pas de double-clic direct)
3. Vérifiez que le type du script est `text/babel`

---

## 📦 Package complet

Si vous voulez tout distribuer :

1. Créez un dossier `correcteur-ia-3d/`
2. Mettez dedans :
   - `index_offline.html`
   - Dossier `libs/` avec les 5 fichiers
   - `README.md` (ce fichier)
3. Compressez en `.zip`
4. Distribuez !

Les utilisateurs n'auront qu'à :
- Décompresser
- Ouvrir `index_offline.html`
- (Avoir leur backend lancé)

---

## 🎓 Avantages de la version offline

✅ **Aucune dépendance internet** pour le frontend  
✅ **Fonctionne partout** (même sans wifi)  
✅ **Parfait pour démo** en classe  
✅ **Pas de latence** de chargement des CDN  
✅ **Toujours la même version** (pas de mises à jour surprises)  

---

## 📊 Comparaison Online vs Offline

| Critère | Online (CDN) | Offline (Local) |
|---------|--------------|-----------------|
| **Internet requis** | ✅ Oui | ❌ Non |
| **Vitesse 1er chargement** | Lent | Rapide |
| **Fiabilité** | Dépend du réseau | 100% |
| **Taille sur disque** | 0 MB | 3.3 MB |
| **Setup initial** | Facile | Moyen |
| **Pour démo** | Risqué | ✅ Parfait |

---

## 🎯 Checklist finale

Avant votre présentation vendredi :

- [ ] Dossier `libs/` créé
- [ ] 5 fichiers JS téléchargés (3.3 MB total)
- [ ] `index_offline.html` présent
- [ ] URL API configurée dans le code
- [ ] Test effectué : animations 3D fonctionnent
- [ ] Backend FastAPI prêt et testé
- [ ] Test complet de bout en bout effectué

---

**Votre frontend est maintenant 100% OFFLINE et prêt pour la démo ! 🎉**

Bon courage pour vendredi ! 🚀

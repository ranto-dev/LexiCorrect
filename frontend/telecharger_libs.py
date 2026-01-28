#!/usr/bin/env python3
"""
Script de téléchargement automatique des bibliothèques
pour le Correcteur Orthographique IA 3D (version offline)
"""

import urllib.request
import os
import sys

def telecharger_fichier(url, destination):
    """Télécharge un fichier depuis une URL"""
    try:
        print(f"   Téléchargement depuis: {url}")
        urllib.request.urlretrieve(url, destination)
        taille = os.path.getsize(destination) / 1024  # Taille en KB
        print(f"   ✓ Téléchargé avec succès ({taille:.1f} KB)")
        return True
    except Exception as e:
        print(f"   ✗ Erreur: {e}")
        return False

def main():
    print("=" * 70)
    print("   TÉLÉCHARGEMENT DES BIBLIOTHÈQUES POUR FRONTEND REACT + THREE.JS")
    print("=" * 70)
    print()
    
    # Créer le dossier libs s'il n'existe pas
    if not os.path.exists('libs'):
        os.makedirs('libs')
        print("✓ Dossier 'libs/' créé")
    else:
        print("✓ Dossier 'libs/' existe déjà")
    
    print()
    
    # Liste des bibliothèques à télécharger
    bibliotheques = {
        'react.production.min.js': 'https://unpkg.com/react@18/umd/react.production.min.js',
        'react-dom.production.min.js': 'https://unpkg.com/react-dom@18/umd/react-dom.production.min.js',
        'babel.min.js': 'https://unpkg.com/@babel/standalone/babel.min.js',
        'three.min.js': 'https://unpkg.com/three@0.159.0/build/three.min.js',
        'axios.min.js': 'https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'
    }
    
    total = len(bibliotheques)
    succes = 0
    
    for i, (filename, url) in enumerate(bibliotheques.items(), 1):
        print(f"[{i}/{total}] {filename}")
        destination = os.path.join('libs', filename)
        
        if telecharger_fichier(url, destination):
            succes += 1
        
        print()
    
    print("=" * 70)
    if succes == total:
        print(f"✓ SUCCÈS ! Toutes les bibliothèques ont été téléchargées ({succes}/{total})")
        print()
        print("Votre structure de fichiers :")
        print("votre-projet/")
        print("├── index_offline.html")
        print("└── libs/")
        for filename in bibliotheques.keys():
            chemin = os.path.join('libs', filename)
            if os.path.exists(chemin):
                taille = os.path.getsize(chemin) / 1024
                print(f"    ├── {filename} ({taille:.1f} KB)")
        print()
        print("Prochaines étapes :")
        print("1. Ouvrez index_offline.html dans votre navigateur")
        print("2. Vérifiez que les animations 3D fonctionnent")
        print("3. Configurez l'URL de votre API dans le fichier HTML")
        print("4. Lancez votre backend FastAPI")
        print("5. Testez la correction de texte !")
    else:
        print(f"⚠ ATTENTION ! Seulement {succes}/{total} bibliothèques téléchargées")
        print("Veuillez vérifier votre connexion internet et réessayer.")
    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nTéléchargement annulé par l'utilisateur.")
        sys.exit(1)
    except Exception as e:
        print(f"\n\nErreur inattendue : {e}")
        sys.exit(1)

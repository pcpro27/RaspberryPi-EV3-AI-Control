# Raspberry Pi + LEGO EV3 avec IA

## Description
Ce projet utilise un Raspberry Pi pour détecter des objets via une caméra et envoyer des commandes à un LEGO EV3 via Bluetooth. Le Raspberry Pi agit comme le "cerveau" et l'EV3 comme les "muscles".

## Prérequis
- Raspberry Pi avec caméra
- LEGO Mindstorms EV3 avec ev3dev installé
- Modèle IA (ex: YOLOv4-tiny) dans le dossier `model/`

## Configuration
1. **Raspberry Pi** :
   - Installez les dépendances : `pip3 install -r requirements.txt`
   - Remplacez `ev3_mac_address` dans `object_detection.py` par l'adresse MAC de votre EV3.

2. **EV3** :
   - Flashez la brique avec [ev3dev](https://www.ev3dev.org/).
   - Exécutez `main.py` pour démarrer la réception Bluetooth.

## Exécution
1. Lancez `object_detection.py` sur le Raspberry Pi.
2. Appuyez sur le bouton central de l'EV3 pour démarrer la connexion.

## Personnalisation
- Adaptez la logique de détection dans `object_detection.py`.
- Modifiez les commandes et actions dans `main.py`.
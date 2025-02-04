## Mini-Projet : Communication MQTT avec Traces PCAP

Ce projet met en place une communication entre un producteur et un consommateur via MQTT en utilisant un broker Mosquitto.
Le producteur lit un fichier de traces PCAP et envoie les paquets au broker, tandis que le consommateur les reçoit et affiche leur contenu.

## 🛠 Prérequis

Python 3

Mosquitto (Broker MQTT)

Bibliothèques Python : pip install paho-mqtt scapy

Fichier de traces : etsi-its-cam-unsecured.pcapng

## 🚀 Installation de Mosquitto (Windows)

Télécharger Mosquitto : https://mosquitto.org/download/

Installer et activer le service : net start mosquitto

Vérifier l'installation : mosquitto -v

## 📌 Exécution

1️⃣ Lancer Mosquitto : mosquitto -v

2️⃣ Démarrer le consommateur : python consumer.py

3️⃣ Exécuter le producteur : python producer.py

Le consommateur affichera les paquets reçus !





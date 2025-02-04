import paho.mqtt.client as mqtt
from scapy.all import Raw

BROKER = "localhost"
TOPIC = "cam/traces"

def on_message(client, userdata, message):
    packet_data = message.payload  # Récupérer les données brutes
    print(f"Paquet reçu : {packet_data[:50]}...")  # Afficher une partie des données

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, 1883, 60)
client.subscribe(TOPIC)

print("En attente des paquets...")
client.loop_forever()

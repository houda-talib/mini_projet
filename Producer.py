import paho.mqtt.client as mqtt
from scapy.all import rdpcap

BROKER = "localhost"
TOPIC = "cam/traces"

# Charger le fichier PCAP
packets = rdpcap("etsi-its-cam-unsecured.pcapng")

# Configurer le client MQTT
client = mqtt.Client()
client.connect(BROKER, 1883, 60)

for pkt in packets:
    raw_data = bytes(pkt)  # Convertir le paquet en bytes
    client.publish(TOPIC, raw_data)

print("Transmission terminée")
client.disconnect()

from scapy.all import *
import time

# Paquete spoofeado enviado a un NetCat escuchando en el puerto 2000 de UDP > nc -luk 2000
A = "192.168.0.16" # spoofed source IP address
B = "192.168.0.24" # destination IP address
C = RandShort() # source port
D = 2000 # destination port
payload = "Spoofing IP {}".format(A) # packet payload

while True:
    spoofed_packet = IP(src=A, dst=B) / UDP(sport=C, dport=D) / payload
    send(spoofed_packet)
    time.sleep(5)


# Traceroute de paquete spoofeado
# ans,unans=sr(IP(src="192.168.0.16", dst="192.168.0.24",ttl=(1,10))/ICMP())
# ans.summary( lambda(s,r) : r.sprintf("%IP.src%"))
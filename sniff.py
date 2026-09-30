from scapy.all import sniff
from parser import process_packet

def main():
    print("[*] Starting packet sniffer...")
    sniff(filter="ip", prn=process_packet, store=False)

if __name__ == "__main__":
    main()
import sys
import os

from scapy.all import sniff

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.logging_config import logger

def packet_callback(packet, log):
    if log:
        logger.info(packet)

    print(packet)

def start_capture(interface='eth0', log=False):
    def callback(packet):
        packet_callback(packet, log)

    sniff(iface=interface, prn=callback, store=False)

import sys
import os
import csv

from scapy.all import sniff

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config.logging_config import general_logger, IDS_logger

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)

def packet_callback(packet, log, IDS):
    if not IDS:
        if log:
            general_logger.info(packet)
        print(packet.summary())
    else:
        ensure_directory('csv_files')
        csv_path = os.path.join('csv_files', 'data.csv')

        try: 
            with open(csv_path, 'a', newline='') as data_file:
                write = csv.writer(data_file)
                write.writerow([str(packet)])
        except Exception as e:
                IDS_logger.error(f"Error writing to file: {e}")


def start_capture(interface='eth0', log=False, IDS=False):
    def callback(packet):
        packet_callback(packet, log, IDS)

    try:
        sniff(iface=interface, prn=callback, store=False)
    except Exception as e:
        IDS_logger.error(f"Error in sniffing packets: {e}")

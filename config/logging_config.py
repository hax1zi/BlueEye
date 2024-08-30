import logging
import logging.handlers

def setup_logging():
    general_logger = logging.getLogger()
    general_logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handle = logging.StreamHandler()
    console_handle.setLevel(logging.DEBUG)
    console_handle.setFormatter(formatter)
    general_logger.addHandler(console_handle)

    sniff_file_handler = logging.handlers.RotatingFileHandler(
        'logs/general.log', maxBytes=10**6, backupCount=5)
    sniff_file_handler.setLevel(logging.INFO)
    sniff_file_handler.setFormatter(formatter)
    general_logger.addHandler(sniff_file_handler)

    IDS_file_handler = logging.handlers.RotatingFileHandler(
        'logs/IDS.log', maxBytes=10**6, backupCount=5)
    IDS_file_handler.setLevel(logging.INFO)
    IDS_file_handler.setFormatter(formatter)

    IDS_logger = logging.getLogger('IDS')
    IDS_logger.setLevel(logging.INFO)
    IDS_logger.addHandler(IDS_file_handler)

    return general_logger, IDS_logger

general_logger, IDS_logger = setup_logging()
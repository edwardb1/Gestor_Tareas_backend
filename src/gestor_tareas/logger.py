import logging
import os
import sys

def configurar_logger():
    """
    Configuracion de logger de Python cocn buenas practicas
    """
    logger = logging.getLogger("gestorApp")
    logger.setLevel(logging.DEBUG)

    if logger.hasHandlers():
        logger.handlers.clear()

    formato_simple = logging.Formatter(
        '%(asctime)s | %(levelname)-8s | %(filename)s:(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formato_simple)

    logger.addHandler(console_handler)

    if not os.path.exists("logs"):
        os.makedirs("logs")

    file_handler = logging.FileHandler("logs/app_nariva.log", encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formato_simple)

    logger.addHandler(file_handler)

    return logger

log = configurar_logger()
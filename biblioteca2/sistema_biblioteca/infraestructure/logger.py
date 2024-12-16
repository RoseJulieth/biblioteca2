import logging

# Configuración del Logger
logging.basicConfig(
    filename='logs/errors.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Función para registrar errores
def log_error(mensaje):
    logging.error(mensaje)

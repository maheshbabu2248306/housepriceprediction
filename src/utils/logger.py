import os
import logging
from datetime import datetime

log_folder = os.path.join(os.getcwd(), "logs")
os.makedirs(log_folder, exist_ok=True)
file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

log_file = os.path.join(log_folder, file_name+'.log')

fmt = "%(asctime)s - %(module)s - %(levelname)s - line no: %(lineno)s - %(message)s"

logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format=fmt,
)



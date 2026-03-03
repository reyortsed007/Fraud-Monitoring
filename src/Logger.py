import logging
import os
from datetime import datetime

Log_file = f"{datetime.now().strftime('%Y-%m-%d')}.log"
logs_path = os.path.join(os.getcwd(), 'logs', Log_file) 
os.makedirs(logs_path,exist_ok=True)

Log_file_path = os.path.join(logs_path, Log_file)

logging.basicConfig(
    filename=Log_file_path,
    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,

)

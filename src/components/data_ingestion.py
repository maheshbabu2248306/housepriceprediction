import os
import os
from src.utils.logger import logging
from src.utils.utils import make_dir, save_artifacts
from ensure import ensure_annotations
import typing
from pathlib import Path
from src.entity_config.entity_config import DataIngestionConfig
import pandas as pd
import numpy as np


class DataIngestion:
    
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    

    def create_artifacts(self):
        try:
            make_dir(folder_name='Artifacts', parent_location=True)
        except OSError as e:
            logging.error('error in creating artifacts folder function')
        finally:
            logging.critical('completed creating artifacts folder function')


    def ingestion(self):
        try:
            logging.info("Data Ingestion Started")
            raw_data = pd.read_excel(io=Path(self.config.raw_data_path), engine= "openpyxl")
            save_artifacts(object = raw_data, file_name='raw_data', file_type='csv')
        except Exception as e:
            logging.error(f'Error occured while ingesting the data: {e}')
        finally:
            logging.critical('Completed ingestion function')
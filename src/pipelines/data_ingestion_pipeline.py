import os
import pandas as pd
import numpy  as np
from src.utils.logger import logging
from src.config.configuration import Configuration
import typing 
from src.components.data_ingestion import DataIngestion



class DataIngestionPipeline:
    def __init__(self):
        print('started data ingestion pipeline..!!')
        
    def main(self):
        try:
            logging.warning("Data Ingestion Pipeline Started")
            config = Configuration()
            data_ingestion_config = config.data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.create_artifacts()
            data_ingestion.ingestion()
        except Exception as e:
            logging.error(e)

if __name__ == '__main__':

    logging.info('starting data pipeline module..!!')
    pipeline = DataIngestionPipeline()
    pipeline.main()

import os
import sys 
from pathlib import Path
from src.utils.logger import logging
from sklearn.ensemble import RandomForestRegressor
from src.utils.utils import save_artifacts, load_pipeline
import pandas as pd
from sklearn.model_selection import train_test_split


class ModelTraining:
    def __init__(self, config):
        self.config = config
        self.train_data = None
        self.test_data = None
        self.train_features = None
        self.train_target = None
        self.test_features = None
        self.test_target = None

    def run_pipeline(self):
        try:
            logging.warning("Model Training Started")
            
            self.split_data()

            self.train_features = self.train_data.drop(columns=['price'])
            self.train_target = self.train_data['price']

            self.test_features = self.test_data.drop(columns=['price'])
            self.test_target = self.test_data['price']

            logging.critical(f'train features shape: {self.train_features.shape}, train target shape: {self.train_target.shape}')
            logging.critical(f'test features shape: {self.test_features.shape}, test target shape: {self.test_target.shape}')
            
            model = RandomForestRegressor()

            model.fit(self.train_features, self.train_target)

            save_artifacts(object=model, file_name='model', file_type='joblib')

        except Exception as e:
            logging.error(f'Error at model training run pipeline: {e}')

    def split_data(self):
        try:
            logging.info("Data Splitting Started")
            data = pd.read_csv(self.config.cleaned_data_path)
            
            self.train_data, self.test_data = train_test_split(data, test_size=self.config.test_size, random_state=10)

            save_artifacts(object = self.train_data, file_name='train_data', file_type='csv')
            save_artifacts(object = self.test_data, file_name='test_data', file_type='csv')

            logging.info("Data Splitting Completed")

        except Exception as e:
            logging.error(f'Error at splitting the data: {e}')
import os 
import sys
from src.utils.logger import logging
from src.utils.utils import load_pipeline, save_artifacts
from src.config.configuration import ModelPredictionConfig
import pandas as pd
from sklearn.metrics import r2_score, mean_squared_error as mse, mean_absolute_error as mae
class ModelPrediction:
    def __init__(self, config:ModelPredictionConfig=None):
        self.config = config
        self.model = None
        self.test_data = None
        self.test_features = None
        self.test_target = None
        self.predictions = None

    def run_pipeline(self):
        try:
            logging.info("Model Prediction Started")
            self.test_data = pd.read_csv(self.config.test_data_path)
            self.model = load_pipeline(pipeline_name='model')
            self.test_features = self.test_data.drop(columns=['price'])
            self.test_target = self.test_data['price']

            predictions_array = self.model.predict(self.test_features)
            self.predictions = pd.Series(predictions_array, name='predictions')
            save_artifacts(object=self.predictions, file_name='predictions', file_type='csv')
            # print(prediction_dataframe)

            logging.info("Model Prediction Completed")

        except Exception as e:
            logging.error(f'Error at model prediction run pipeline: {e}')


    def get_results(self):
        try:
            
            logging.info("Getting results")

            r2_ = r2_score(self.test_target, self.predictions)
            mse_score = mse(self.test_target, self.predictions)
            mae_score = mae(self.test_target, self.predictions)

            logging.critical(f'r2_score: {r2_}, mse_score: {mse_score}, mae_score: {mae_score}')
            
        except Exception as e:
            logging.error(f'Error at getting results: {e}')

    @staticmethod
    def make_predictions(data=None):
        try:
            logging.info("Making predictions started")
            # print('received data: ' , data)
            model = load_pipeline(pipeline_name='model')
            new_predictions = model.predict(data)

            logging.critical(f'new predictions: {new_predictions[0]}')
            return new_predictions
        except Exception as e:
            logging.error(f'Error at making predictions: {e}')
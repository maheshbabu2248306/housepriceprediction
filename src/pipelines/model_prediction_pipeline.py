import os
import sys
from src.utils.logger import logging
from src.config.configuration import Configuration
from src.components.model_prediction import ModelPrediction
import pandas as pd
import numpy as np


class ModelPredictionPipeline:
    def __init__(self):
        print('started model predictions pipeline..!!')

    def main(self):
        try:
            logging.info("Model Prediction Pipeline Started")
            config = Configuration()
            model_prediction_config = config.model_prediction_config()
            model_prediction = ModelPrediction(config=model_prediction_config)
            model_prediction.run_pipeline()
            values = [-122.369,8500.0,3.0,0.2337482070975801,7.0,1300.0,98146.0,47.5063]
            values_array = np.array(values).reshape(1,8)
            temp_series = pd.DataFrame(values_array, columns=['long','total_area','room_bed', 'sight','quality', 'ceil_measure','zipcode', 'lat'])
            # print(type(temp_series), len(temp_series))
            result = model_prediction.make_predictions(temp_series)
            logging.critical(f'from result value: {result}')
            model_prediction.get_results()
            logging.info('Model Prediction Pipeline Completed')
        except Exception as e:
            logging.error(f'Error at model prediction run pipeline: {e}')
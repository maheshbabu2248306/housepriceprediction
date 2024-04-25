import os
import sys
from src.utils.logger import logging
from src.config.configuration import Configuration
from pathlib import Path
from src.components.model_training import ModelTraining


class ModelTrainingPipeline:

    def __init__(self):
        print('started model training pipeline..!!')


    def main(self):
        try:
            logging.info("Model Creation Pipeline Started")
            config = Configuration()
            model_training_config = config.model_training_config()
            model_training = ModelTraining(config=model_training_config)
            model_training.run_pipeline()
        except Exception as e:
            logging.error(f'Error at model training run pipeline: {e}')
import os
import sys
from src.utils.logger import logging
from dataclasses import dataclass
from src.entity_config.entity_config import DataIngestionConfig, DataPreparationConfig, ModelTrainingConfig, ModelPredictionConfig
import yaml
import typing
from ensure import ensure_annotations
from pathlib import Path

class Configuration:
    def __init__(self):
        try:
            with open( 'src/config/config.yaml', 'r') as stream:  
                self.configuration = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            logging.error(f'error in loading yaml file: {exc}')

    @ensure_annotations
    def data_ingestion_config(self) -> DataIngestionConfig:
        try:
            ingestion_params = self.configuration['data_ingestion']
            # keys = ingestion_params.keys()
            ingestion_config = DataIngestionConfig(raw_data_path=ingestion_params['raw_data_path'])
            return ingestion_config
        except Exception as e:
            logging.error(f'Error at data ingestion config: {sys.exc_info()}')

    @ensure_annotations
    def data_preparation_config(self) -> DataPreparationConfig:
        try:
            preparation_params = self.configuration['data_preparation']
            #keys = preparation_params.keys()
            preparation_config = DataPreparationConfig(
                raw_data_path = preparation_params['raw_data'],
                pipeline_name = preparation_params['pipeline_name']
            )
            return preparation_config
        except Exception as e:
            logging.error(f'Error at data preparation config: {sys.exc_info()}')

    @ensure_annotations
    def model_training_config(self) -> ModelTrainingConfig:
        try:
            model_training_params = self.configuration['model_training']
            model_training_config = ModelTrainingConfig(
            cleaned_data_path = model_training_params['cleaned_data_path'],
            test_size = model_training_params['test_size'])

            return model_training_config

        except:
            logging.error(f'Error at model training config: {sys.exc_info()}')

    @ensure_annotations
    def model_prediction_config(self) -> ModelPredictionConfig:
        try:
            model_prediction_params = self.configuration['model_prediction']
            model_prediction_config = ModelPredictionConfig(
            test_data_path = model_prediction_params['test_data_path'])
            return model_prediction_config

        except:
            logging.error(f'Error at model prediction config: {sys.exc_info()}')
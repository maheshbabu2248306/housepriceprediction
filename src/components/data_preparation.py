import os
import sys
from src.utils.logger import logging
from src.config.configuration import Configuration
import pandas as pd
import numpy as np
from pathlib import Path
from ensure import ensure_annotations
import typing
from src.components.transformers import handling_categorical, handling_numerical
from typing import List
from sklearn.preprocessing import FunctionTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.utils.utils import load_pipeline, save_artifacts


class DataPreparation:

    

    def __init__(self, config: Configuration):
        self.config = config
        self.data = None
        self.features = None
        self.target = None
        self.categorical_columns = None
        self.numerical_columns = None
        self.required_columns = None
        
    def create_pipeline(self):
        try:
            logging.critical("Data Preparation Started")
            self.data = pd.read_csv(self.config.raw_data_path)
            
            # considering only required columns from the experiment notebook
            self.required_columns = ['room_bed', 'sight','quality', 'ceil_measure','zipcode', 'lat','long','total_area','price']
            self.data = self.data[self.required_columns]

            self.features = self.data.drop(columns=['price'])
            self.target = self.data['price']

            self.categorical_columns = self.features.select_dtypes(include=['object']).columns.tolist()
            self.numerical_columns = self.features.select_dtypes(exclude=['object']).columns.tolist()
            
            logging.warning(f'categorical columns: {self.categorical_columns}')
            logging.warning(f'numerical columns: {self.numerical_columns}')
            # creating pipeline

            categorical_transformer = FunctionTransformer(handling_categorical)
            numerical_transformer = FunctionTransformer(handling_numerical)

            preprocessor = ColumnTransformer(
                transformers=[
                    ('categorical', categorical_transformer, self.categorical_columns),
                    ('numerical', numerical_transformer, self.numerical_columns)
                ])

            preparation_pipeline = Pipeline(steps=[
                ('preprocessor', preprocessor)
                ])

            # store_pipeline
            # save_pipeline( self.config.pipeline_name , preparation_pipeline)
            save_artifacts(object=preparation_pipeline, file_name=self.config.pipeline_name, file_type='joblib')
            logging.info("Data Preparation Completed")
            """print('\n\n\n')
            new_data = preparation_pipeline.fit_transform(features)
            columns_list = categorical_columns + numerical_columns
            new_data = pd.DataFrame(new_data, columns=columns_list)
            
"""
            # print('after processor pipeline:\n\n ', new_data.info())

        except Exception as e:
            logging.error(f'Error at create pipeline function: {e}')


    def run_pipeline(self):
        try:
            preparation_pipeline = load_pipeline(self.config.pipeline_name)
            logging.info("Data Preparation Pipeline Started")
            # print(type(self.features))
            data_array = preparation_pipeline.fit_transform(self.features)
            new_columns = self.categorical_columns + self.numerical_columns
            
            new_features = pd.DataFrame(data=data_array, columns=new_columns)
            
            cleaned_data = pd.concat([new_features, self.target], axis=1)
            save_artifacts(object = cleaned_data, file_name='cleaned_data', file_type='csv')
            logging.info("Data Preparation Pipeline Completed")
        except Exception as e:
            logging.error(f'Error at run pipeline function: {e}')
import os 
import sys
from src.utils.logger import logging
from ensure import ensure_annotations
import typing
from typing import Optional, Union
from pathlib import Path
import pandas as pd
import types
import sklearn.pipeline
import joblib

@ensure_annotations
def make_dir(folder_name: str, parent_location: bool , current_location: Path = Path(os.getcwd())):
    try:
        if parent_location:
            folder = os.path.join(os.getcwd(), folder_name)
        else:
            folder = os.path.join(current_location, folder_name)
        os.makedirs(folder, exist_ok=True)
        
    except Exception as e: 
        logging.warning('Exception occured while creating directory: ')
        


    
def save_artifacts(object: Union[pd.DataFrame, sklearn.pipeline.Pipeline], file_name: str, file_type: str):
    try:
        if file_type == 'csv':
            file = os.path.join('Artifacts', file_name+'.csv')
            object.to_csv(file, index=False)
            logging.critical(f'{file_name} is stored in artifacts folder')
        elif file_type == 'joblib':
            joblib.dump(object, os.path.join('Artifacts', file_name+'.joblib'))
            logging.critical(f'{file_name} is stored in artifacts folder')
    except Exception as e:
        logging.error('Error while storing the data in artifacts folder: ', e)

"""@ensure_annotations
def save_pipeline(pipeline_name:str, pipeline: sklearn.pipeline.Pipeline):
    try:
        joblib.dump(pipeline, os.path.join('Artifacts', pipeline_name+'.joblib'))
        logging.critical(f'{pipeline_name} is stored in artifacts folder')
    except Exception as e:
        logging.error('Error while storing the folder in artifacts folder')"""


@ensure_annotations
def load_pipeline(pipeline_name: str):
    try:
        return joblib.load(os.path.join('Artifacts', pipeline_name+'.joblib')) 
    except Exception as e:
        logging.error('Error while loading the folder in artifacts folder')
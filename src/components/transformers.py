import os
import sys
from src.utils.logger import logging
from sklearn.preprocessing import FunctionTransformer
import typing
from typing import List, Iterator
from ensure import ensure_annotations
import pandas as pd
import numpy as np
from numpy.typing import NDArray




def handling_categorical(data: pd.DataFrame) -> pd.DataFrame:
    
    try:
        logging.warning(f'Handling categorical data: {data.columns.tolist()}')
        def is_float(value):
            try:
                float(value)
                return True
            except:
                return False

        for col in data.columns.tolist():
            # data[col][~data[col].apply(np.isreal)] = 0
            data.loc[~data[col].apply(is_float), col] = 0
            # data[col][~data[col].apply(is_float)] = 0
            data[col] = data[col].fillna(value=0)
            data[col] = data[col].astype('float64')
            data[col] = data[col].replace(0, data[col].mean())
            
            
        # print('\n\n\n\nfrom categorical transformer:\n\n ', data)

        return data

    except Exception as e:
        logging.error('error in handling categorical function: ', e)



def handling_numerical(data:pd.DataFrame) -> NDArray[np.float64]:
    try:
        logging.warning(f'Handling numerical data: {data.columns.tolist()}')
        for col in data.columns.tolist():
            data.loc[~data[col].apply(np.isreal), col] = 0
            # data[col][~data[col].apply(np.isreal)] = 0
            data[col] = data[col].fillna(value=0)
            data[col] = data[col].replace(0, data[col].mean())
        return data
    except Exception as e:
        logging.error('error in handling numerical function: ', e)
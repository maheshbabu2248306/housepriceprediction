import os
from src.utils.logger import logging
from dataclasses import dataclass
from pathlib import Path
import typing
from typing import List, Iterator
from sklearn.pipeline import Pipeline

@dataclass
class DataIngestionConfig:
    raw_data_path: Path 


@dataclass
class DataPreparationConfig:
    raw_data_path: Path
    pipeline_name: str
    

@dataclass
class ModelTrainingConfig:
    cleaned_data_path: Path
    test_size: float

@dataclass
class ModelPredictionConfig:
    test_data_path: Path

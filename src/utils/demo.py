from ensure import ensure_annotations
import os
import types
import pandas as pd
import numpy as np 
import joblib
from typing import Union
from ensure import ensure_annotations


def func(a: Union[int, float], b: int) -> float:
    return a + b

print(func(10.3, 23))
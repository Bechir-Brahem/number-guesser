"""
Machine learning model using a singleton design pattern
huge performance gain 
"""
import os.path
from pathlib import Path

import joblib

from pages.classes.ml_models.ModelSingletonMeta import ModelSingletonMeta


class MlModel(metaclass=ModelSingletonMeta):
    def __init__(self):
        self.model = joblib.load(os.path.join(Path(__file__).resolve().parent, 'rf_v2.pkl'))

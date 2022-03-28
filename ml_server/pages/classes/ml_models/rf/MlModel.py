"""
Machine learning model using a singleton design pattern
huge performance gain 
"""
import os.path
from pathlib import Path

import joblib

from pages.classes.ml_models.ModelSingletonMeta import ModelSingletonMeta


class MlModel(metaclass=ModelSingletonMeta):
    """
    metaclass singleton.
    must define:
     - model attribute
     - model_name attribute
     - predict method
    """

    def __init__(self):
        self.full_name = 'random forests'
        self.model_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        path = os.path.join(Path(__file__).resolve().parent, self.model_name + '.pkl')
        self.model = joblib.load(path)

    def predict(self, digit):
        return self.model.predict([digit])

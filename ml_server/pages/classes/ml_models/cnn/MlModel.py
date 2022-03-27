"""
Machine learning model using a singleton design pattern
huge performance gain 
"""
import os.path
from pathlib import Path
import tensorflow.keras as keras

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
        self.model_name = os.path.dirname(os.path.realpath(__file__))
        self.model = keras.models.load_model(os.path.join(Path(__file__).resolve().parent, self.model_name))

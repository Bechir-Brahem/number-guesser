"""
Machine learning model using a singleton design pattern
huge performance gain 
"""
import os.path
from pathlib import Path

import keras
import numpy as np

from pages.classes.ml_models.ModelDL import ModelDL
from pages.classes.ml_models.ModelSingletonMeta import ModelSingletonMeta


class MlModel(ModelDL,metaclass=ModelSingletonMeta):
    """
    metaclass singleton.
    must define:
     - model attribute
     - model_name attribute
     - predict method
    """

    def __init__(self):
        self.full_name='CNN'
        self.model_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.model = keras.models.load_model(os.path.join(Path(__file__).resolve().parent, self.model_name+'.h5'))



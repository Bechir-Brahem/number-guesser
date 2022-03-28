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


class MCDropout(keras.layers.Dropout):
    def call(self, inputs):
        return super().call(inputs, training=True)


class MlModel(ModelDL,metaclass=ModelSingletonMeta):
    """
    metaclass singleton.
    must define:
     - model attribute
     - model_name attribute
     - predict method
    """

    def __init__(self):
        self.full_name = 'CNN with MC dropout'
        self.model_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.model = keras.models.load_model(os.path.join(Path(__file__).resolve().parent, self.model_name + '.h5'),
                                             custom_objects={"MCDropout": MCDropout}
                                             )

    # def predict(self, digit):
    #     digit = np.array(digit)
    #     digit = digit.reshape((1, 28, 28, 1))
    #     y_probas = np.stack([self.model(digit) for __ in range(100)])
    #     y_proba = y_probas.mean(axis=0)
    #     ans = np.argmax(y_proba)
    #     return ans

"""
Machine learning model using a singleton design pattern
huge performance gain 
"""
import os.path
from pathlib import Path

import keras

from pages.classes.ml_models.ModelDL import ModelDL
from pages.classes.ml_models.ModelSingletonMeta import ModelSingletonMeta


class MCDropout(keras.layers.Dropout):
    def call(self, inputs):
        return super().call(inputs, training=True)


class MlModel(ModelDL, metaclass=ModelSingletonMeta):
    """
    metaclass singleton.
    must define:
     - model attribute
     - model_name attribute
     - predict method
    """

    def __init__(self):
        self.full_name = 'ANN with MC dropout'
        self.model_name = os.path.basename(os.path.dirname(os.path.realpath(__file__)))
        self.model = keras.models.load_model(os.path.join(Path(__file__).resolve().parent, self.model_name + '.h5'),
                                             custom_objects={"MCDropout": MCDropout}
                                             )


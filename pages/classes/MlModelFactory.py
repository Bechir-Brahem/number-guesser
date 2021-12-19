"""
Machine learning model using a singleton design pattern
huge performance gain
"""
import os
from importlib import import_module
from pathlib import Path

imported_models = {}
first_time = True


def getModel(user_model):
    if user_model in imported_models:
        return imported_models[user_model]

    models_path = os.path.join(Path(__file__).resolve().parent, 'ml_models')
    directory_contents = os.listdir(models_path)
    for item in directory_contents:
        if item != '__pycache__' and os.path.isdir(os.path.join(models_path, item)):
            imported_models[item] = import_module(f'pages.classes.ml_models.{item}.MlModel').MlModel()
    if user_model not in imported_models:
        raise ValueError(f'Model "{user_model}" does not exist')

    return imported_models[user_model]

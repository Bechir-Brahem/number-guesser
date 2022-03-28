"""
- Class following the factory method.
- the getModel receives the model name and returns the specified
  ML model instance
"""
import os
from importlib import import_module
from pathlib import Path

imported_models = {}
first_time = True


def checkExistantModels():
    models_path = os.path.join(Path(__file__).resolve().parent, 'ml_models')
    directory_contents = os.listdir(models_path)
    for item in directory_contents:
        if item != '__pycache__' and os.path.isdir(os.path.join(models_path, item)):
            imported_models[item] = import_module(f'pages.classes.ml_models.{item}.MlModel').MlModel()


def getModel(user_model):
    """
    getModel receives the model name "user_model" then it searches
    in ml_models directory for models with that specific name if not found
    it raises ValueError. This is designed for flexibility. adding a model only
    requires changes in the frontend and do not require restarting the server
    """

    if user_model in imported_models:
        # if the model is already instantiated just return it
        return imported_models[user_model]
    checkExistantModels()
    if user_model not in imported_models:
        raise ValueError(f'Model "{user_model}" does not exist')

    return imported_models[user_model]


def getModelNames():
    checkExistantModels()
    ret = {}
    for name in imported_models.keys():
        ret[name] = imported_models[name].full_name
    return ret

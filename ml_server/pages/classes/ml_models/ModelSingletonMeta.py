class ModelSingletonMeta(type):
    """
    singleton metaclass that returns the attribute model
    in the instance
    """
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__call__(*args, **kwargs)
            cls._instance = instance
        return cls._instance.model

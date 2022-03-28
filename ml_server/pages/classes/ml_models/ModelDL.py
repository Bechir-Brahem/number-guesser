import numpy as np


class ModelDL:
    def predict(self, digit):
        digit = np.array(digit)
        digit = digit.reshape((1, 28, 28, 1))
        y_probas = np.stack([self.model(digit) for __ in range(100)])
        y_proba = y_probas.mean(axis=0)
        ans = np.argmax(y_proba)
        return ans

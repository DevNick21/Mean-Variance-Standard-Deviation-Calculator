import numpy as np


def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers")
    else:
        arr = np.array(list)
        mat = arr.reshape((3, 3))
        calculations = {
            "mean": [mat.mean(0), mat.mean(1),
                     arr.mean()],
            'variance': [mat.var(0), mat.var(1), arr.var()],
            'standard deviation': [mat.std(0), mat.std(1),
                                   arr.std()],
            'max': [mat.max(0), mat.max(1), arr.max(0)],
            'min': [mat.min(0), mat.min(1), arr.min(0)],
            'sum': [mat.sum(0), mat.sum(1), arr.sum(0)]
        }
        return calculations

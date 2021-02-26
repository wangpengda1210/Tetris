import numpy as np


def collect_info(array):
    assert isinstance(array, np.ndarray)
    return f'Shape: {array.shape}; dimensions: {array.ndim}; ' \
           f'length: {len(array)}; size: {array.size}'

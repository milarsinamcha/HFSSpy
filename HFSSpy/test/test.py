import numpy as np
from .sets import HesitantFuzzySoftSet
from .similarities import similarity_chunfeng
from .different measures import symmetric_cross_entropy,relative_entropy

def similarity(set1, set2):
    return 1 - (1 / (4 * np.log(2))) * symmetric_cross_entropy(set1, set2)

# Test data
A1 = [
    [[0.20, 0.32, 0.35], [0.30, 0.40], [0.60], [0.35, 0.45]],
    [[0.30, 0.32], [0.28, 0.40], [0.58, 0.60], [0.35, 0.40]]
]

A = [
    [[0.20, 0.30, 0.50], [0.80, 0.90, 0.95], [0.75, 0.80, 0.90], [0.30, 0.40, 0.45]],
    [[0.40, 0.60, 0.62], [0.76, 0.90], [0.73, 0.78, 0.90], [0.38, 0.60]]
]

# Calculate and print similarity between A and A1
print(similarity(A, A1))

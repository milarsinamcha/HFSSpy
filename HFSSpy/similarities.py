import numpy as np
from . import ifss_hamming_distance, ifss_normalized_hamming_distance, ifss_euclidean_distance, ifss_normalized_euclidean_distance
from .sets import HesitantFuzzySoftSet

def Similarity_nhsnh(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet) -> np.array:
    return 1 - distance_nhsnh(set1,set2)

def Similarity_nhsne(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet) -> np.array:
    return 1 - distance_nhsnh(set1,set2)

def Similarity_nhsnm(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet,q):
    return 1 - distance_nhsnh(set1,set2)
def similarity_chunfeng(set1, set2):
    return 1 - (1 / (4 * np.log(2))) * symmetric_cross_entropy(set1, set2)
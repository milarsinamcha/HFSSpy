import numpy as np
from typing import List, Tuple

class HesitantFuzzySoftSet:
    def __init__(self, sets: List[List[List[float]]]):
        max_length = max(len(inner_list) for sublist in sets for inner_list in sublist)
        padded_sets = []
        for sublist in sets:
            padded_sublist = []
            for inner_list in sublist:
                padded_inner_list = inner_list + [0] * (max_length - len(inner_list))
                padded_sublist.append(padded_inner_list)
            padded_sets.append(padded_sublist)
        self.sets = np.array(padded_sets)

    def __repr__(self):
        return f'HesitantFuzzySoftSet(Sets: {self.sets})'

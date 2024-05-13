def correlation_coefficient(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet):
    if set1.sets.shape != set2.sets.shape:
        raise ValueError("HesitantFuzzySoftSets must have the same shape for calculating correlation coefficient.")

    result_arrays = []
    for set1_list, set2_list in zip(set1.sets, set2.sets):
        result_list = []
        for s1, s2 in zip(set1_list, set2_list):
            s1_sorted = sorted(s1, reverse=True)
            s2_sorted = sorted(s2, reverse=True)
            multiplied = [x * y for x, y in zip(s1_sorted, s2_sorted)]
            nonzero_count = sum(1 for x in multiplied if x != 0)
            if nonzero_count == 0:
                result_list.append(0)
            else:
                result_list.append(sum(multiplied) / nonzero_count)
        result_arrays.append(result_list)

    result_array = np.array(result_arrays)
    total_sum = np.sum(result_array)
    return total_sum


# Example usage
e1 = [
    [[0.2, 0.5, 0.3], [0.3, 0.1, 0.5, 0.7], [0.7, 0.2, 0.6], [0.4, 0.2]],
    [[0.5, 0.3, 0.7, 0.9], [0.4, 0.1, 0.6], [0.4, 0.1, 0.4], [0.6, 0.3, 0.7, 0.1]],
    [[0.4, 0.2, 0.1, 0.6], [0.8, 0.3, 0.5], [0.5, 0.6, 0.4, 0.7], [0.5, 0.6, 0.2]],
    [[0.5, 0.4, 0.0, 0.0], [0.1, 0.6, 0.3, 0.9], [0.5, 0.7, 0.0, 0.0], [0.4, 0.7, 0.3, 0.0]]
]
e2 = [
    [[0.4, 0.3, 0.1, 0.2], [0.5, 0.6, 0.2, 0.0], [0.4, 0.2, 0.7, 0.2], [0.4, 0.3, 0.1, 0.0]],
    [[0.4, 0.5, 0.0, 0.0], [0.3, 0.5, 0.6, 0.1], [0.4, 0.6, 0.1, 0.0], [0.3, 0.6, 0.0, 0.0]],
    [[0.8, 0.4, 0.8, 0.0], [0.4, 0.2, 0.3, 0.0], [0.7, 0.2, 0.4, 0.0], [0.3, 0.5, 0.2, 0.7]],
    [[0.2, 0.5, 0.1, 0.6], [0.5, 0.7, 0.1, 0.1], [0.4, 0.2, 0.7, 0.0], [0.3, 0.1, 0.5, 0.0]]
]
e3 = [
    [[0.4, 0.3], [0.5, 0.4, 0.1], [0.5, 0.3, 0.1], [0.5, 0.2, 0.1]],
    [[0.9, 0.5, 0.4, 0.2], [0.7, 0.3], [0.5, 0.4, 0.2], [0.6, 0.5, 0.2]],
    [[0.7, 0.7, 0.5], [0.6, 0.5, 0.3, 0.2], [0.4, 0.2], [0.6, 0.5, 0.2, 0.1]],
    [[0.5, 0.3, 0.2], [0.6, 0.3], [0.5, 0.5, 0.2, 0.1], [0.9, 0.8, 0.7]]
]
e4 = [
    [[0.5, 0.2, 0.1, 0.5], [0.3, 0.2, 0.1], [0.4, 0.5, 0.3], [0.8, 0.9]],
    [[0.8, 0.7], [0.3, 0.5, 0.6, 0.2], [0.4, 0.3, 0.5, 0.1], [0.4, 0.6, 0.9, 0.3]],
    [[0.3, 0.2, 0.1], [0.7, 0.6], [0.5, 0.3], [0.1, 0.4, 0.2]],
    [[0.4, 0.5, 0.2, 0.5], [0.3, 0.2, 0.1], [0.9, 0.7, 0.9], [0.6, 0.3]]
]

set1 = HesitantFuzzySoftSet(e2)
set2 = HesitantFuzzySoftSet(e4)

result = correlation_coefficient(set1, set2)
print(result)

def relative_entropy(set1, set2):
    m = len(set1)
    n = len(set1[0])
    # Pad set2 with zeros to match the length of inner lists in set1
    max_length = max(len(inner_list) for sublist in set1 for inner_list in sublist)
    for sublist in set2:
        for inner_list in sublist:
            inner_list.extend([0] * (max_length - len(inner_list)))

    relative_entropies = []
    for i in range(m):
        for j in range(n):
            for k in range(len(set1[i][j])):
                if set1[i][j][k] == 0:
                    continue
                entropy = set1[i][j][k] * np.log(2 * set1[i][j][k] / (set1[i][j][k] + set2[i][j][k]))
                entropy += (1 - set1[i][j][k]) * np.log(2 * (1 - set1[i][j][k]) / (2 - set1[i][j][k] - set2[i][j][k]))
                relative_entropies.append(entropy)
    return np.mean(relative_entropies)

def symmetric_cross_entropy(set1, set2):
    # Calculate relative entropy between set1 and set2
    entropy_1_2 = relative_entropy(set1, set2)
    # Calculate relative entropy between set2 and set1
    entropy_2_1 = relative_entropy(set2, set1)
    # Symmetric cross entropy is the sum of relative entropies in both directions
    return entropy_1_2 + entropy_2_1

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

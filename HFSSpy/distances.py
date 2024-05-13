def distance_hsnh(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet):
    if set1.sets.shape != set2.sets.shape:
        raise ValueError("Sets must have the same shape")

    distance = np.zeros(set1.sets.shape)

    sum_array = np.zeros((set1.sets.shape[0], set1.sets.shape[1]))

    for i in range(len(set1.sets)):
        for j in range(len(set1.sets[i])):
            num_elements = len(set1.sets[i][j])
            for k in range(num_elements):
                distance[i][j][k] = abs(set1.sets[i][j][k] - set2.sets[i][j][k])
                sum_array[i][j] += distance[i][j][k]
            # Divide by the number of elements in the array
            sum_array[i][j] /= num_elements
             # Calculate the total number of elements in the result sum_array
    total_elements = np.sum([len(row) for row in sum_array])

    return np.sum(sum_array)/total_elements

def distance_hsne(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet):
    return np.sqrt(distance_hsnh(set1, set2))

def distance_hsnm(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet, q):
    return distance_hsnh(set1, set2) ** q

def distance_nhsnh(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet) -> np.array:
    result_set1 = np.zeros((set1.sets.shape[0], set1.sets.shape[1]), dtype=object)
    result_set2 = np.zeros((set2.sets.shape[0], set2.sets.shape[1]), dtype=object)

    distance = np.zeros(set1.sets.shape)

    sum_array = np.zeros((set1.sets.shape[0], set1.sets.shape[1]))

    for i in range(len(set1.sets)):
        for j in range(len(set1.sets[i])):
            num_elements = len(set1.sets[i][j])
            for k in range(num_elements):
                distance[i][j][k] = abs(set1.sets[i][j][k] - set2.sets[i][j][k])
                sum_array[i][j] += distance[i][j][k]
            # Divide by the number of elements in the array
            sum_array[i][j] /= num_elements

    for i in range(set1.sets.shape[0]):
        for j in range(set1.sets.shape[1]):
            num_elements_set1 = len(set1.sets[i][j])
            mean_set1 = sum(set1.sets[i][j]) / num_elements_set1
            result_set1[i][j] = (np.array(set1.sets[i][j]) - mean_set1) ** 2

            num_elements_set2 = len(set2.sets[i][j])
            mean_set2 = sum(set2.sets[i][j]) / num_elements_set2
            result_set2[i][j] = (np.array(set2.sets[i][j]) - mean_set2) ** 2

    for i in range(result_set1.shape[0]):
        for j in range(result_set1.shape[1]):
            sum_result_set1 = sum(result_set1[i][j])
            num_elements_set1 = len(result_set1[i][j])
            result_set1[i][j] = np.sqrt(sum_result_set1 / num_elements_set1)

            sum_result_set2 = sum(result_set2[i][j])
            num_elements_set2 = len(result_set2[i][j])
            result_set2[i][j] = np.sqrt(sum_result_set2 / num_elements_set2)

    # Subtract corresponding elements from two resulting sets
    for i in range(result_set1.shape[0]):
        for j in range(result_set1.shape[1]):
            result_set1[i][j] -= result_set2[i][j]

    # Sum corresponding elements from sum_array and result_set1
    sum_result = np.zeros(sum_array.shape)
    for i in range(sum_array.shape[0]):
        for j in range(sum_array.shape[1]):
            sum_result[i][j] = sum_array[i][j] + result_set1[i][j]

    # Divide the sum_result by twice the number of total elements in sum_array
    divisor = 2 * np.prod(sum_array.shape)
    final_result = np.sum(sum_result) / divisor

    return final_result

def distance_nhsne(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet) -> np.array:
    return distance_nhsnh(set1,set2)**(1/2)

def distance_nhsnm(set1: HesitantFuzzySoftSet, set2: HesitantFuzzySoftSet, q):
    return distance_nhsnh(set1,set2)**(1/q)
def find_pairs_by_sum(list_values: list, target: int) -> list:
    """
    Finds pairs of integers from a list that sum to a target value

    :param list_values: list
    :param target: int
    :return pairs of numbers : list
    """
    list_values = sorted(list_values)
    pairs = []
    hash_dict = {}
    for value in list_values:
        number_to_find = target - value
        if number_to_find in hash_dict:
            pairs.append([value, number_to_find])
        else:
            hash_dict[value] = True
    return pairs
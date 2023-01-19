# Coding exercise
from src import exercise


if __name__ == '__main__':
    list_values = [1, 9, 5, 0, 20, -4, 12, 16, 7]
    target = 12
    pairs = exercise.find_pairs_by_sum(list_values=list_values, target=target)
    print(pairs)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

r = 300
K = 15000

files = ["H3_a.txt", "H3_c.txt"]


def get_data_from_file(filename):
    with open("./data/" + filename) as file:
        return [int(x) for x in file.read().splitlines()]


def load_data():
    weights = get_data_from_file(files[0])
    costs = get_data_from_file(files[1])
    data = list(map(list, zip(weights, costs)))

    # All data have parameters, if i should use them, or not, and first index
    for index, x in enumerate(data):
        data[index] += (True, index + 1)

    # sort for better search
    data.sort(key=lambda t: t[0])
    return data


def check_min_weight(item):
    if item[3] == True:
        return item[0]
    return False


def main():
    data = load_data()

    # test = [sum(x) for x in zip(*data)]
    sum_of_weights = sum(i for i, _, k, _ in data if k)
    sum_of_costs = sum(j for _, j, k, _ in data if k)

    while sum_of_weights > K and len(data) > r:
        # TODO: vytvor funkciu ako kluc hldania, vzdy prehladavaju, len tie čo maju true
        min_weight = min(data, key=lambda t: check_min_weight(t))
        min_weight_index = data.indexá(min_weight)

        if sum_of_weights - min_weight[0] < K:
            # i have sorted data, that mean, i cant find nothing lower than this values
            break

        print(f'Removing element {min_weight} with minimum weight {min_weight[0]} on index {min_weight_index}')
        data[min_weight_index][2] = False
        sum_of_weights = sum(i for i, _, k, _ in data if k)
        sum_of_costs = sum(j for _, j, k, _ in data if k)
        print(f'Sum of weights is: {sum_of_weights}\n'
              f'Sum_of_costs is: {sum_of_costs}\n'
              f'Number of items in: {len(data)}\n'
              f'HUF is {sum_of_costs}')

    print(f'SOLUTION:\n'
          f'Sum_of_weights is {sum_of_weights}\n'
          f'Sum_of_costs is {sum_of_costs}')

    data.sort(key=lambda t: t[3])
    print(data)


if __name__ == "__main__":
    # execute only if run as a script
    main()

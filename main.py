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


def main():
    data = load_data()

    sum_of_weights = sum(i for i, _, k, _ in data if k)
    sum_of_costs = sum(j for _, j, k, _ in data if k)
    number_of_items = len([k for _, _, k, _ in data if k])
    print(f"UHF on start is: {sum_of_costs}")

    while sum_of_weights > K and number_of_items > r:
        min_weight = min((x for x in data if x[2]), key=lambda x: x[0])
        min_weight_index = data.index(min_weight)

        if sum_of_weights - min_weight[0] < K:
            # i have sorted data, that mean, i cant find nothing lower than this values
            break

        # print(f'Removing element {min_weight} with minimum weight {min_weight[0]} on index {min_weight_index}')
        data[min_weight_index][2] = False
        sum_of_weights -= data[min_weight_index][0]
        sum_of_costs -= data[min_weight_index][1]
        number_of_items -= 1
        print(f'HUF is {sum_of_costs}, removed: {min_weight[0]}/{min_weight[1]}')

    print(f'SOLUTION:\n'
          f'HUF is {sum_of_costs}\n'
          f'Check HUF is {sum(j for _, j, k, _ in data if k)}\n'
          f'Number_of_items is {number_of_items}\n'
          f'Check Number_of_items is {len([k for _, _, k, _ in data if k])}\n'
          f'Sum_of_weights is {sum_of_weights}\n'
          f'Check Sum_of_weights is {sum(i for i, _, k, _ in data if k)}\n'
          f'Sum_of_costs is {sum_of_costs}\n'
          f'Sum_of_costs is {sum(j for _, j, k, _ in data if k)}\n')

    data.sort(key=lambda t: t[3])
    print(data)


if __name__ == "__main__":
    # execute only if run as a script
    main()

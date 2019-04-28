r = 300
K = 15000

files = ["H3_a.txt", "H3_c.txt"]


def get_data_from_file(filename):
    with open("./data/" + filename) as file:
        return [int(x) for x in file.read().splitlines()]


def load_data():
    data = list(map(list, zip(get_data_from_file(files[0]), get_data_from_file(files[1]))))
    print(f'Data load successfully')

    # All data have parameters, if i should use them, or not, and first index
    print(f'Východiskové riešenie --> batoh so všetkými predmetmi.')
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

    print(f"HUF on start is: {sum_of_costs}\n"
          f"Number of items in knapsack is: {number_of_items}\n"
          f"Sum_of_weights in knapsack is: {sum_of_weights}")

    while sum_of_weights > K and number_of_items > r:
        min_weight = min((x for x in data if x[2]), key=lambda x: x[0])
        min_weight_index = data.index(min_weight)

        # i have sorted data, that mean, i cant find nothing lower than this values
        if sum_of_weights - min_weight[0] < K:
            break

        data[min_weight_index][2] = False
        sum_of_weights -= data[min_weight_index][0]
        sum_of_costs -= data[min_weight_index][1]
        number_of_items -= 1
        # print(f'HUF is {sum_of_costs}, removed: {min_weight[0]}/{min_weight[1]}')

    data.sort(key=lambda t: t[3])

    check_solution(data, sum_of_weights, sum_of_costs, number_of_items)

    print(f'\nSOLUTION:\n'
          f'HUF is: {sum_of_costs}\n'
          f'Number of items in knapsack is: {number_of_items}\n'
          f'Sum of_weights in knapsack is: {sum_of_weights}\n'
          f'Sum of costs in knapsack is: {sum_of_costs}\n')

    # TODO write into file
    with open("solution.txt", "w") as outfile:
        outfile.writelines(list("%s\n" % item for item in data))


def check_solution(data, sum_of_weights, sum_of_costs, number_of_items):
    if sum(i for i, _, k, _ in data if k) != sum_of_weights:
        raise Exception("Check values for sum of weights in knapsack do not match!")
    if sum(j for _, j, k, _ in data if k) != sum_of_costs:
        raise Exception("Check values for sum of costs in knapsack do not match!")
    if len([k for _, _, k, _ in data if k]) != number_of_items:
        raise Exception("Check values for number of items in knapsack do not match!")


if __name__ == "__main__":
    # execute only if run as a script
    main()

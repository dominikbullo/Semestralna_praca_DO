r = 300
K = 15000

files = ["H3_a.txt", "H3_c.txt"]


def get_data_from_file(filename):
    with open("./data/" + filename) as file:
        return [int(x) for x in file.read().splitlines()]


def load_data():
    weights = get_data_from_file(files[0])
    costs = get_data_from_file(files[1])
    data = list(zip(weights, costs))
    data.sort(key=lambda t: t[0])
    return data


def main():
    data = load_data()

    # test = [sum(x) for x in zip(*data)]
    sum_of_weights = sum(i for i, _ in data)
    sum_of_costs = sum(j for _, j in data)

    while sum_of_weights > K and len(data) > r:
        min_weight = min(data, key=lambda t: t[0])
        min_weight_index = data.index(min_weight)

        if sum_of_weights - min_weight[0] < K:
            # i have sorted data, that mean, i cant find nothing lower than this values
            break

        print(f'Removing element {min_weight} with minimum weight {min_weight[0]} on index {min_weight_index}')
        # TODO: tu nebude remove, ale označím si to ako predmet odstranený z batohu
        data.pop(min_weight_index)
        sum_of_weights = sum(i for i, _ in data)
        sum_of_costs = sum(j for _, j in data)
        print(f'Sum of weights is: {sum_of_weights}\n'
              f'Sum_of_costs is: {sum_of_costs}\n'
              f'Number of items in: {len(data)}\n'
              f'HUF is {sum_of_costs}')

    # TODO: rohodovanie o tom, ktorý zoberie a ktorý nie
    # TODO: naspať do poradia!
    # TODO: určiť x
    # TODO: ypísať do súboru!
    
    print(f'SOLUTION:\n'
          f'Sum_of_weights is {sum_of_weights}\n'
          f'Sum_of_costs is {sum_of_costs}')


if __name__ == "__main__":
    # execute only if run as a script
    main()

with open("./data/H3_a.txt") as weights_file:
    weights = [int(x) for x in weights_file.read().splitlines()]
with open("./data/H3_c.txt") as costs_file:
    costs = [int(x) for x in costs_file.read().splitlines()]

data = list(zip(weights, costs))
data.sort(key=lambda tup: tup[0])

n = 500
r = 300
K = 15000

sum_of_weights = sum(i for i, _ in data)
sum_of_costs = sum(j for _, j in data)


def find_min_weight_index(start_value):
    temp_min = min(data[start_value:], key=lambda t: t[0])
    if sum_of_weights - temp_min[0] < K:
        find_min_weight_index(min_weight_index)
    return data.index(temp_min)


while sum_of_weights > K and len(data) > r:
    min_weight_index = find_min_weight_index(None)
    print(f'Removing element with minimum weight {data[min_weight_index]} on index {min_weight_index}')
    data.pop(min_weight_index)
    sum_of_weights = sum(i for i, _ in data)
    sum_of_costs = sum(j for _, j in data)
    print(f'Sum_of_weights is {sum_of_weights} and Sum_of_costs is {sum_of_costs}')
    print(f'Number of items in: {len(data)}')
    print(f'HUF is {sum_of_costs}')

print(len(data))
# print(data)

print(sum_of_weights)
print(sum_of_costs)

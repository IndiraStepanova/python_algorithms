def fractional_knapsack(capacity, vals_and_weights):
    order = [(v / w, w) for v, w in vals_and_weights]
    order.sort(reverse=True)
    
    acc = 0
    for v_per_w, w in order:
        if w < capacity:
            acc += v_per_w * w
            capacity -= w
        else:
            acc += v_per_w * capacity
            break
    return acc


with open('C:\_src\pyhon_courses\python_algorithms\input_knapsack.txt', 'r') as sample:
    reader = (tuple(map(int, line.split())) for line in sample)
    n, capacity = next(reader)
    vals_and_weights = list(reader)
    opt_value = fractional_knapsack(capacity, vals_and_weights)
    print("{:.3f}".format(opt_value))

def tests():
    assert fractional_knapsack(0, [(60, 20)]) == 0.0
    assert fractional_knapsack(25, [(60, 20)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (0, 100)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 60.0 + 5.00
    assert fractional_knapsack(50, [(60, 20), (100, 50), (120, 30)]) == 180.0


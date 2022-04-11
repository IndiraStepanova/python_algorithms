knapsack = []
n, capacity = map(int, input().split())
for i in range(1, n + 1):
    el_cost, el_vol = map(int, input().split())
    v_per_w = el_cost/el_vol
    knapsack.append([v_per_w, el_vol])
knapsack.sort(reverse=True)
acc = 0
for v_per_w, el_vol in knapsack:
    if el_vol < capacity:
        acc += v_per_w * el_vol
        capacity -= el_vol
    else:
        acc += v_per_w * capacity
        break
    
print("{:.3f}".format(acc))
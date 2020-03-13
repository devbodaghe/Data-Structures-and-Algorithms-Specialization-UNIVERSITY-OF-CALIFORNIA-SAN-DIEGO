# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    prices_per_weights=[]
    for i in range(len(weights)):
        prices_per_weights.append(prices[i]/weights[i])
    all=list(zip(prices,prices_per_weights,weights))
    all.sort(key=lambda x: x[1],reverse=True)
    i=0
    total=0
    while capacity:
        price,ppw,w=all[i]
        if w<capacity:
            total+=price
            capacity-=w
        else:
            total+=ppw*capacity
            capacity=0
        i+=1
    return total

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

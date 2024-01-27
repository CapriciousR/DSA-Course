from sys import stdin


def optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    per_w_val = {}
    for i in range(n):
        per_w_val[(values[i]/weights[i])] = i
        values[i] = (values[i]/weights[i])
    
    values.sort(reverse=True)
    
    i = 0
    
    while capacity > 0 and i < n:

        a = min(capacity, weights[per_w_val[values[0]]])

        value += a * values[0]

        capacity -= a

        values.pop(0)
        
        i += 1
        
    return value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))

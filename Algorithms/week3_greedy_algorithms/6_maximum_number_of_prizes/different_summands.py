def optimal_summands(n):
    summands = []
    # write your code here
    i = 0
    while n > 0:
        i += 1
        n -= i
        if n <= i:
            summands.append(n+i)
            break
        summands.append(i)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)

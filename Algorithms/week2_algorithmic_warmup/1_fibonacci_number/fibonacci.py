def fibonacci_number(n):
    if n <= 1:
        return n
    fib_arr = [0,1]
    for i in range(2,n+1):
        fib_arr.append(fib_arr[i-1] + fib_arr[i-2])

    return fib_arr[-1]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))

def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    numbers.sort()
    max_product = numbers[-1] * numbers[-2]

    return max_product


if __name__ == '__main__':
    _ = int(input())
    input_numbers = list(map(int, input().split()))
    print(max_pairwise_product(input_numbers))

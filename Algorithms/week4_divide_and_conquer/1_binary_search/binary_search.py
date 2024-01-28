def binary_search(keys, query):
    # write your code here
    def bin_search(K: list[int], x: int, low: int, high: int):
        mid = low + (high-low)//2
        if low > high:
            return -1
        if K[mid] == x:
            return mid
        if K[mid] < x:
            return bin_search(K, x, mid+1, high)
        if K[mid] > x:
            return bin_search(K, x, low, mid-1)
    

    return (bin_search(keys, q, 0, len(keys)-1))

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

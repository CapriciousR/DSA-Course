
def binary_search(keys, query):
    def bin_search(K, x, low, high):
        if low > high:
            return -1
        if K[low] == x:
            return low
        mid = low + (high - low) // 2
        if K[mid] == x:
            if K[mid] == K[mid-1]:
                return bin_search(K, x, low, mid-1)
            else:
                return mid
        elif K[mid] > x:
            return bin_search(K, x, low, mid - 1)
        elif K[mid] < x:
            return bin_search(K, x, mid + 1, high)
    
    return bin_search(keys, query, 0, len(keys) - 1)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')

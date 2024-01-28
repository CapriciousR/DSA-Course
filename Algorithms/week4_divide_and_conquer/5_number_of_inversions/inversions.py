
def inversions_naive(a):
    number_of_inversions = 0
    def merge_sort(array):
        if len(array) == 1:
            return array, 0
        left, cnt1 = merge_sort(array[:len(array)//2])
        right, cnt2 = merge_sort(array[len(array)//2:])
        
        i = 0
        j = 0
        k = 0
        cnt = cnt1+cnt2
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                array[k] = right[j]
                j += 1
                cnt += len(left)-i
                k += 1
                continue
            array[k] = left[i]
            i += 1
            k += 1
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            
        return array, cnt
        
    arr, cnt = merge_sort(a)
    return cnt


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(inversions_naive(elements))

def majority_element_naive(elements):
    counts = {}
    
    for element in elements:
        if element in counts:
            counts[element] += 1
        else:
            counts[element] = 1
            
    thres = len(elements)/2

    for value in counts.values():
        if value > thres:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))

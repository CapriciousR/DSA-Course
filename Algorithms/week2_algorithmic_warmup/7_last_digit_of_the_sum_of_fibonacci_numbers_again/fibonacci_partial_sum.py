# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):

    previous = 0
    current  = 1
    pis_cnt = 0
    pis_list = [0,1]

    for i in range(60):

        previous, current = current, (previous + current)%10
        pis_list.append(current)
        pis_cnt += 1
        
        if previous == 0 and current == 1:
            break
        
    from_sum = pis_list[(from_+1)%pis_cnt]-1
    if from_sum < 0:
        from_sum += 10
    to_sum = pis_list[(to+2)%pis_cnt]-1
    if to_sum < 0:
        to_sum += 10
    # print(from_sum, to_sum)
    # print(pis_list)
    
    if to_sum < from_sum:
        to_sum += 10
    
    return abs(to_sum-from_sum)
        

if __name__ == '__main__':
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum_naive(from_, to))

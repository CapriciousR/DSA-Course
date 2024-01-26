def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    previous, current = 0, 1
    pis_list = [0,1]
    pis_cnt = 60

    for _ in range(60):
        previous, current = current, (previous + current)%10
        pis_list.append(current)
        
    curr = pis_list[(n)%pis_cnt]
    prev = pis_list[(n-1)%pis_cnt]
    
    sum = curr * (curr+prev)
    
    return sum%10 

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))

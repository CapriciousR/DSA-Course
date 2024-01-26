def fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    current = 1
    previous = 0
    pisano_cnt = 0
    
    if m >= n:
        for _ in range(n-1):
            previous, current = current, (previous+current) % m
            
        return current
    
    fib_list = [0,1]
        
    for i in range(2,6*m+1):
        previous, current = current, (previous+current)%m
        fib_list.append(current)
        pisano_cnt += 1
        
        if previous == 0 and current == 1:
            break
    print(pisano_cnt)    
    return fib_list[n%pisano_cnt]

if __name__ == '__main__':
    n, m = map(int, input().split())
    print(fibonacci_huge_naive(n, m))

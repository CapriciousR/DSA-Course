def fibonacci_sum(n):
    if n <= 1:
        return n

    previous, current = 0, 1
    pis_list = [0,1]
    pis_cnt = 0

    for i in range(60):
        previous, current = current, (previous + current) % 10
        pis_list.append(current)
        pis_cnt += 1
        
        if previous == 0 and current == 1:
            break
        
    res = pis_list[(n+2)%pis_cnt]-1
    if res<0:
        res+=10
    return res

        



if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))

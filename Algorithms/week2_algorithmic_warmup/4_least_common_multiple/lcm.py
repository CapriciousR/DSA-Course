def gcd(a, b):
    if b == 0:
        return a
    
    if b > a:
        return gcd(b,a)
    
    return gcd(b,a%b)

def lcm(a, b):
    
    lcm = int((a*b)/gcd(a,b))
    
    return lcm
    


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))
    


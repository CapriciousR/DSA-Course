from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    trav_dist = 0
    refills = 0
    i = 0

    while trav_dist < distance:
        while i < len(stops):
            if stops[i] > tank + trav_dist:
                trav_dist = stops[i-1] 
                refills += 1
            if stops[i] > tank + trav_dist:
                return -1
            i+=1 
            
        if distance > tank + trav_dist:
            trav_dist = stops[-1]
            refills += 1
        if distance > tank + trav_dist:
            return -1
        
        return refills
            
                
            
    return -1


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))

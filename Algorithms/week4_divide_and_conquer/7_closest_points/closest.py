from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def brute_force(points):
    min_dist = float('inf')
    for i in range(len(points)):
        for j in range(i+1,len(points)):
            min_dist = min(distance_squared(points[i], points[j]), min_dist)
    return min_dist

def strip_closest(points, d):
    sorted_y = sorted(points, key= lambda point: point.y)
    min_dist = d
    for i in range(len(sorted_y)-1):
        for j in range(i+1, min(i+7,len(sorted_y))):
            min_dist = min(min_dist, distance_squared(sorted_y[i], sorted_y[j]))
    return min_dist


def min_dist_recurs(points):
    if len(points) <= 3:
        return brute_force(points)
    mid = (len(points)-1)//2
    midpt = points[mid]
    
    d1 = min_dist_recurs(points[:mid+1])
    d2 = min_dist_recurs(points[mid+1:])
    
    d = min(d1, d2)
    
    strip = []
    
    for i in range(len(points)):
        if abs(points[i].x - points[mid].x) < sqrt(d):
            strip.append(points[i])
    
    return min(d, strip_closest(strip, d))
    
    

def minimum_distance_squared(points):
    sorted_pts = sorted(points, key= lambda point: point.x)
    
    return min_dist_recurs(sorted_pts)


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))

from sys import stdin
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    # write your code here
    
    sorted_segments = sorted(segments, key=lambda p : p.end)
    
    for i in range(n):
        if i == 0:
            points.append(sorted_segments[i].end)
        if sorted_segments[i].start > points[-1]:
            points.append(sorted_segments[i].end)
    
    return points


if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)

from sys import stdin


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    start_label, point_label, end_label = 0,1,2
    point_cnts = [0]*len(points)
    point_map = {}
    
    combined = []
    
    for s in starts:
        combined.append((s, start_label))
    for e in ends:
        combined.append((e, end_label))
    for i,p in enumerate(points):
        combined.append((p, point_label))
        if p not in point_map:
            point_map[p] = [i]
        else:
            point_map[p].append(i)
            
    sorted_array = sorted(combined, key = lambda x: (x[0], x[1]))
    
    count = 0
    
    for item in sorted_array:
        if item[1] == start_label:
            count += 1
        elif item[1] == end_label:
            count -= 1
        elif item[1] == point_label:
            indices = point_map[item[0]]
            for index in indices:
                point_cnts[index] = count
        
    return point_cnts
                


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_naive(input_starts, input_ends, input_points)
    print(*output_count)

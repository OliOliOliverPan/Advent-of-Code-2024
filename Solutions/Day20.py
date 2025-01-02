def find_path(route_map, row, col, start_x,start_y,end_x,end_y):
    route = None
    visited = set()

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    queue = [([(start_x,start_y)],(start_x,start_y))]
    visited.add((start_x,start_y))

    while queue:
        path, (cx,cy) = queue.pop(0)

        if (cx,cy) == (end_x,end_y):
            route = path
            break

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<row and 0<=ny<col and route_map[nx][ny] != '#' and (nx,ny) not in visited:
                queue.append((path+[(nx,ny)], (nx,ny)))
                visited.add(((nx,ny)))

    return route, len(route)



def day20Q1(route_map):
    row = len(route_map)
    col = len(route_map[0])

    start_x, start_y = None, None
    end_x, end_y = None, None
    for i in range(row):
        for j in range(col):
            if route_map[i][j] == 'S':
                start_x, start_y = i,j
            elif route_map[i][j] == 'E':
                end_x, end_y = i,j
    
    route_no_cheat, total_time_no_cheat = find_path(route_map, row, col, start_x, start_y,end_x, end_y)

    total_ways = 0
    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    for point_x, point_y in route_no_cheat:
        for dx1,dy1 in directions:
            for dx2, dy2 in directions:
                next_x, next_y = point_x + dx1 +dx2, point_y + dy1 + dy2
                if not (0 <= next_x < row and 0 <= next_y < col) or route_map[next_x][next_y] == '#':
                    continue
                else:
                    remaining_time = total_time_no_cheat - route_no_cheat.index((next_x,next_y))
                    if route_no_cheat.index((point_x,point_y)) + 2 + remaining_time <= total_time_no_cheat - 100:
                        total_ways += 1
    
    return total_ways



    


def day20Q2(route_map):

    row = len(route_map)
    col = len(route_map[0])

    start_x, start_y = None, None
    for i in range(row):
        for j in range(col):
            if route_map[i][j] == 'S':
                start_x, start_y = i, j
        else:
            continue
        break
            
    
    dists = [[-1 for _ in range(col)] for _ in range(row)]
    cx, cy = start_x, start_y
    dists[cx][cy] = 0
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while route_map[cx][cy] != 'E':
        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if nx <0 or ny < 0 or nx>=row or ny >= col:
                continue
            if route_map[nx][ny] == '#':
                continue
            if dists[nx][ny] != -1: 
                continue
            dists[nx][ny] = dists[cx][cy] + 1
            cx, cy = nx, ny
    
    total_ways = 0

    for cx in range(row):
        for cy in range(col):
            if route_map[cx][cy] == '#': 
                continue
            for radius in range(2,21):
                for dx in range(radius+1):
                    dy = radius-dx
                    for nx, ny in {(cx+dx, cy+dy),(cx+dx, cy-dy), (cx-dx, cy+dy), (cx-dx, cy-dy)}:
                        if nx <0 or ny<0 or nx>=row or ny>=col:
                            continue
                        if route_map[nx][ny] == '#': 
                            continue
                        if dists[nx][ny] - dists[cx][cy] >= 100+radius:
                            total_ways += 1 


    return total_ways








if __name__ == "__main__":
    route_map = []

    with open("Inputs/Day20Input.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("#") and len(line) > 0:  
            route_map.append(list(line))
    

    result_part_one = day20Q1(route_map)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day20Q2(route_map)
    print("Result for part two: "+str(result_part_two))
def find_paths(route_map, row, col, start_x,start_y,end_x,end_y):
    paths = []
    visited = set()

    directions = [(-1,0),(0,1),(1,0),(0,-1)]

    queue = [([(start_x,start_y)],(start_x,start_y))]
    visited.add((start_x,start_y))

    while queue:
        path, (cx,cy) = queue.pop(0)

        if (cx,cy) == (end_x,end_y):
            paths.append(path)
            continue

        for dx, dy in directions:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<row and 0<=ny<col and route_map[nx][ny] != '#' and (nx,ny) not in visited:
                queue.append((path+[(nx,ny)], (nx,ny)))
                visited.add(((nx,ny)))
    
    return paths




def day18Q1(corrupted_locations):
    row, col = 71, 71
    route_map = [['.' for _ in range(row)] for _ in range(col)]

    start_x, start_y = 0,0
    end_x, end_y = 70,70

    for corrupted_location in corrupted_locations:
        x,y  = corrupted_location
        route_map[x][y] = '#'

    paths = find_paths(route_map, row, col, start_x, start_y, end_x, end_y)
    
    min_step = min([len(path) - 1  for path in paths]) # exclude starting point

    return min_step














def day18Q2():

    row, col = 71, 71
    route_map = [['.' for _ in range(row)] for _ in range(col)]
    start_x, start_y = 0,0
    end_x, end_y = 70,70

    count = 0

    while True:
        corrupted_locations = []
        with open('Inputs/Day18Input.txt', 'r') as file:
            for i, line in enumerate(file):
                if i >= count:  
                    break
                x, y = map(int, line.strip().split(',')) 
                corrupted_locations.append((x, y))



        for corrupted_location in corrupted_locations:
            x,y  = corrupted_location
            route_map[x][y] = '#'
        
        paths = find_paths(route_map, row, col, start_x, start_y, end_x, end_y)

        if paths == []:
            first_byte = corrupted_locations[-1]
            return "{0},{1}".format(first_byte[0],first_byte[1])
        count += 1


    







if __name__ == "__main__":
    corrupted_coordinates = []
    with open('Inputs/Day18Input.txt', 'r') as file:
        for i, line in enumerate(file):
            if i >= 1024:  
                break
            x, y = map(int, line.strip().split(',')) 
            corrupted_coordinates.append((x, y))
    

    result_part_one = day18Q1(corrupted_coordinates)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day18Q2()
    print("Result for part two: "+str(result_part_two))

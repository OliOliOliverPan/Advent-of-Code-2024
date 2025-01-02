def day10Q1(route_map):
    all_paths = []
    starting_points = []

    row = len(route_map)
    col = len(route_map[0])

    for i in range(row):
        for j in range(col):
            if route_map[i][j] == 0:
                starting_points.append((i, j))
 
    while starting_points:
        x, y = starting_points.pop(0)
        queue = [([(x, y)], (x, y))]
        visited = set()
        visited.add((x, y))

        while queue:
            path, (cx, cy) = queue.pop(0)
            current_height = route_map[cx][cy]

            if current_height == 9:
                all_paths.append(path)  
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < row and 0 <= ny < col and (nx, ny) not in visited:
                    if route_map[nx][ny] == current_height + 1:
                        queue.append((path + [(nx, ny)], (nx, ny)))
                        visited.add((nx, ny))

    return len(all_paths)










def day10Q2(route_map):
    all_paths = []
    starting_points = []

    row = len(route_map)
    col = len(route_map[0])

    for i in range(row):
        for j in range(col):
            if route_map[i][j] == 0:
                starting_points.append((i, j))

    while starting_points:
        x, y = starting_points.pop(0)
        queue = [([(x, y)], (x, y))]

        while queue:
            path, (cx, cy) = queue.pop(0)
            current_height = route_map[cx][cy]

            if current_height == 9:
                all_paths.append(path)  
                continue

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < row and 0 <= ny < col:
                    if route_map[nx][ny] == current_height + 1:
                        queue.append((path + [(nx, ny)], (nx, ny)))

    return len(all_paths)

        






if __name__ == "__main__":
    all_rows = []

    with open("Inputs/Day10Input.txt", "r") as file:
        for line in file:
            
            row = list(map(int, line.strip()))  
            all_rows.append(row)

    result_part_one = day10Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day10Q2(all_rows)
    print("Result for part two: "+str(result_part_two))




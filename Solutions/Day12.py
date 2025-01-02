def compute_area(garden_map,row, col, x,y):
    plant = garden_map[x][y]

    queue = []
    queue.append((x,y))

    visited = set()
    visited.add((x,y))
    
    while queue:
        cx, cy = queue.pop(0)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = cx + dx, cy + dy

            if 0 <= nx < row and 0 <= ny < col and (nx,ny) not in visited and garden_map[nx][ny] == plant:
                queue.append((nx,ny))
                visited.add((nx,ny))

    return list(visited), len(visited)



def compute_perimeter(plants):
    total_perimeter = len(plants) * 4

    while plants:
        cx, cy = plants.pop(0)
        for dx, dy in[(-1,0), (1,0), (0,-1),(0,1)]:
            if (cx+dx,cy+dy) in plants:
                total_perimeter -= 2
        
    return total_perimeter



def day12Q1(garden_map):
    total_price = 0

    row = len(garden_map)
    col = len(garden_map[0])

    global_visited = [[False for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if not global_visited[i][j]:
                areas,total_area = compute_area(garden_map,row,col, i,j)
                for (vx,vy) in areas:
                    global_visited[vx][vy] = True
                total_perimeter = compute_perimeter(areas)
                total_price += total_area * total_perimeter

    return total_price








from collections import defaultdict, deque

def day12Q2(garden_map):
    DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    rows = len(garden_map)
    cols = len(garden_map[0])

    visited = set()
    total_price = 0

    for i in range(rows):
        for j in range(cols):
            if (i, j) in visited:
                continue

            queue = deque([(i, j)])
            current_area = 0

            # A dictionary that maps each direction to the set of outer boundary cells surrounding the current area
            direction_details = defaultdict(set)

            while queue:
                cx, cy = queue.popleft()
                if (cx, cy) in visited:
                    continue
                visited.add((cx, cy))
                current_area += 1

                for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nx, ny = cx + dx, cy + dy

                    if 0 <= nx < rows and 0 <= ny < cols and garden_map[nx][ny] == garden_map[cx][cy]:
                        queue.append((nx, ny))
                        
                    if not (0 <= nx < rows and 0 <= ny < cols) or garden_map[nx][ny] != garden_map[cx][cy]:
                        if (dx, dy) not in direction_details:
                            direction_details[(dx, dy)] = set()
                        direction_details[(dx, dy)].add((cx, cy))

            area_sides = 0
            for dir, contours in direction_details.items():
                visited_side = set()
                for x1, y1 in contours:
                    if (x1, y1) not in visited_side:
                        area_sides += 1
                        q = deque([(x1, y1)])
                        while q:
                            x, y = q.popleft()
                            if (x, y) in visited_side:
                                continue
                            visited_side.add((x, y))
                            for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                                xn, yn = x + dx, y + dy  # (xn, yn) is a neighboring cell of (x, y) that's in the same direction as (x,y)
                                if (xn, yn) in contours:
                                    # Traverse all cells that belong to the same connected boundary segment as (x, y).
                                    # These cells will be added to visited_side to avoid duplicate counting.
                                    # Adding these cells to the queue won't increase area_sides because they belong
                                    # to the same side as (x,y).
                                    q.append((xn,yn))

            total_price += current_area * area_sides

    return total_price







if __name__ == "__main__":
    all_rows = []

    with open("Inputs/Day12Input.txt", "r") as file:
        for line in file:
            
            row = list(map(str, line.strip()))  
            all_rows.append(row)
    
    result_part_one = day12Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day12Q2(all_rows)
    print("Result for part two: "+str(result_part_two))
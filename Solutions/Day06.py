def day06Q1(lists):
    

    row = len(lists)
    col = len(lists[0])

    directions = ['up','right', 'down','left']

    visited = [[False for _ in range(col)] for _ in range(row)]

    start_x = -1
    start_y = -1
    for i in range(row):
        for j in range(col):
            if lists[i][j] == "^":
                start_x = i
                start_y = j
                break
    
    current_direction = 0

    total_places = 1 # take starting point into account
    visited[start_x][start_y] = True

    while 0 <= start_x < row and 0 <= start_y<col:
        if lists[start_x][start_y] == '#':
             if directions[current_direction] == "up":
                start_x += 1
             elif directions[current_direction] == "right":
                start_y -= 1
             elif directions[current_direction] == "down":
                start_x -= 1
             elif directions[current_direction] == "left":
                start_y += 1 
             current_direction = (current_direction + 1) % len(directions)
             continue

        elif lists[start_x][start_y] == "." and not visited[start_x][start_y]:
            total_places += 1
            visited[start_x][start_y] = True

        if directions[current_direction] == "up":
            start_x -= 1
        elif directions[current_direction] == "right":
            start_y += 1
        elif directions[current_direction] == "down":
            start_x += 1
        elif directions[current_direction] == "left":
            start_y -= 1
    
    return total_places













# objective: find all points where a obstacle can be set such that the guard will stuck in a loop
# constraints:
 # 1) can't put an obstacle at the starting point of the guard
 # 2) need to go over all points in the map, put an obstacle and check if this will make the guard stuck in a loop
def day06Q2(lists):
    row = len(lists)
    col = len(lists[0])

    # define movements of four directions: up, right, down, left
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    # finding starting point
    start_x, start_y = -1, -1
    for i in range(row):
        for j in range(col):
            if lists[i][j] == "^":
                start_x, start_y = i, j
                break

    def is_in_loop(grid, x, y):
        """determine whether having entered a loop or not"""
        visited = [[False for _ in range(col)] for _ in range(row)]
        current_direction = 0  # initial direction
        path = set()  # used for checking loops
        while 0 <= x < row and 0 <= y < col:
            # if the current point has been visited, it means we have entered a loop
            if (x, y, current_direction) in path:
                return True
            path.add((x, y, current_direction))
            
            # move back to the previous step when encountering obstacle
            if grid[x][y] == '#':
                x -= dx[current_direction]
                y -= dy[current_direction]
                current_direction = (current_direction + 1) % 4
                continue

            visited[x][y] = True

            x += dx[current_direction]
            y += dy[current_direction]

        return False

    valid_positions = 0

    for i in range(row):
        for j in range(col):
            # we don't put obstacle at starting point
            if (i == start_x and j == start_y) or lists[i][j] != '.':
                continue

            # temporarily set obstacle
            lists[i][j] = '#'

            # check if we have entered a loop
            if is_in_loop(lists, start_x, start_y):
                valid_positions += 1

            # remove the obstacle
            lists[i][j] = '.'

    return valid_positions
        









if __name__ == "__main__":
    
    all_rows = []

    with open("Inputs/Day06Input.txt", "r") as file:
        for line in file:
            
            row = list(map(str, line.split()))  
            all_rows.append(row)
    all_rows = [list(row[0]) for  row in all_rows]
    
    result_part_one = day06Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day06Q2(all_rows)
    print("Result for part two: "+str(result_part_two))
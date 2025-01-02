def day15Q1(route_map, moves):
    actions = {'^':(-1,0),'>':(0,1), 'v':(1,0), '<':(0,-1)}

    x,y = 0,0
    row = len(route_map)
    col = len(route_map[0])
    for i in range(row):
        for j in range(col):
            if route_map[i][j] == '@':
                x,y = i,j
                break
    
    for move in moves:
        dx,dy = actions[move]
        if route_map[x+dx][y+dy] == "#":
            continue
        elif route_map[x+dx][y+dy] == "O":
            temp_x,temp_y = x+dx, y+dy
            while route_map[temp_x+dx][temp_y+dy] == "O":
                temp_x, temp_y = temp_x + dx, temp_y+dy
            if route_map[temp_x+dx][temp_y+dy] == '#':
                continue
            elif route_map[temp_x+dx][temp_y+dy] == '.':
                while (temp_x, temp_y) != (x,y):
                    route_map[temp_x+dx][temp_y+dy] = "O"
                    route_map[temp_x][temp_y] = '.'
                    temp_x, temp_y = temp_x - dx, temp_y - dy

                route_map[x+dx][y+dy] = '@'
                route_map[x][y] = '.'
                x,y = x+dx, y+dy
    
        elif route_map[x+dx][y+dy] == '.':
            route_map[x+dx][y+dy] = '@'
            route_map[x][y] = '.'
            x, y = x+dx, y+dy
        
    total_coordinates = 0
    for i in range(row):
        for j in range(col):
            if route_map[i][j] == "O":
                total_coordinates += (100 * i + j)
    
    return total_coordinates








def construct_large_map(route_map):
    large_map = []
    for i in range(len(route_map)):
        nrow = []
        for j in range(len(route_map[0])):
            if route_map[i][j] == '#':
                nrow.append("#")
                nrow.append("#")
            elif route_map[i][j] == '.':
                nrow.append(".")
                nrow.append(".")    
            elif route_map[i][j] == 'O':
                nrow.append("[")
                nrow.append("]")
            elif route_map[i][j] == '@':
                nrow.append("@")
                nrow.append(".")
        large_map.append(nrow)

    return large_map




def day15Q2(large_map, moves):
    actions = {'^':(-1,0),'>':(0,1), 'v':(1,0), '<':(0,-1)}

    x,y = 0,0
    row, col = len(large_map), len(large_map[0])
    for i in range(row):
        for j in range(col):
            if large_map[i][j] == '@':
                x,y = i,j
                break
    
    for move in moves:
        dx,dy = actions[move]
        coordinates_to_move = [(x,y)]

        i = 0
        cant_move = False
        while i < len(coordinates_to_move):
            cx, cy = coordinates_to_move[i]
            nx, ny = cx+dx, cy+dy
            if large_map[nx][ny] in "[]":
                if (nx,ny) not in coordinates_to_move:
                    coordinates_to_move.append((nx,ny))
                if large_map[nx][ny] == "[":
                    if (nx,ny+1) not in coordinates_to_move:
                        coordinates_to_move.append((nx,ny+1)) # append the corresponding "]" of the "[" at (nx, ny)
                if large_map[nx][ny] == "]":
                    if (nx,ny-1) not in coordinates_to_move:
                        coordinates_to_move.append((nx,ny-1)) # append the corresponding "[" of the "]" at (nx, ny)
            elif large_map[nx][ny] == "#":
                cant_move = True
                break
            i+=1
        if cant_move:
            continue
    
        new_large_map = [[large_map[i][j] for j in range(col)] for i in range(row)]

        for cx, cy in coordinates_to_move:
            new_large_map[cx][cy] = "."
        for cx,cy in coordinates_to_move:
            new_large_map[cx+dx][cy+dy] = large_map[cx][cy]

        large_map = new_large_map

        x+=dx
        y+=dy
    
    total_coordinates = 0
    for i in range(row):
        for j in range(col):
            if large_map[i][j] == "[":
                total_coordinates += (100 * i + j)
    
    return total_coordinates
    




    
import copy
if __name__ == "__main__":
    route_map = []
    moves = []

    with open("Inputs/Day15Input.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("#") and len(line) > 0:  
            route_map.append(list(line))
        elif line: 
            moves.append(line)

    moves = list("".join(moves))

    route_map_q1 = copy.deepcopy(route_map)
    route_map_q2 = copy.deepcopy(route_map)

    result_part_one = day15Q1(route_map_q1, moves)
    print("Result for part one: "+str(result_part_one))

    large_map = construct_large_map(route_map_q2)
    result_part_two = day15Q2(large_map, moves)
    print("Result for part two: "+str(result_part_two))
    
def day14Q1(positions, velocities):
    row = 103
    col = 101
    global_map = [[0 for _ in range(col)] for _ in range(row)]

    for i, j in positions:
        global_map[i][j] += 1

    for position, velocity in zip(positions, velocities):
        x,y = position
        dx, dy = velocity

        for t in range(100):
            
            global_map[x][y] -= 1
            x = (x+dx) % row
            y = (y+dy) % col
            global_map[x][y] += 1
    
    mid_row, mid_col = row//2, col//2
    quadrant_1 = [global_map[m][:mid_col] for m in range(mid_row)]
    quadrant_1_num = sum(sum(quadrant_1,[]))
    quadrant_2 = [global_map[m][mid_col+1:] for m in range(mid_row)]
    quadrant_2_num = sum(sum(quadrant_2,[]))
    quadrant_3 = [global_map[m][:mid_col] for m in range(mid_row+1, row)]
    quadrant_3_num = sum(sum(quadrant_3,[]))
    quadrant_4 = [global_map[m][mid_col+1:] for m in range(mid_row+1, row)]
    quadrant_4_num = sum(sum(quadrant_4,[]))
    return quadrant_1_num * quadrant_2_num * quadrant_3_num * quadrant_4_num
    







    
# trick of question 2: 
#   The minimum number of seconds required for the robots to arrange themselves into a distinct Christmas tree formation
#   is when each robot occupies a unique position.
def day14Q2(positions, velocities):
    row = 103
    col = 101
    global_map = [[0 for _ in range(col)] for _ in range(row)]

    for i, j in positions:
        global_map[i][j] += 1
    
    t = 1
    while True:
        new_positions = []
        for position, velocity in zip(positions, velocities):
            x,y = position
            dx, dy = velocity
            global_map[x][y] -= 1
            x = (x+dx) % row
            y = (y+dy) % col
            global_map[x][y] += 1
            new_positions.append((x,y))
        
        distinct = len(new_positions) == len(set(new_positions))
        
        if distinct:
            return t
        else:
            positions = new_positions
            t += 1








if __name__=="__main__":

    positions = []
    velocities = []

    with open("Inputs/Day14Input.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                # Parse the position (p) and velocity (v)
                parts = line.split()
                p = parts[0].split("=")[1].strip(",").split(",")
                v = parts[1].split("=")[1].split(",")
                
                # Store position as (p2, p1)
                p2, p1 = int(p[1]), int(p[0])
                positions.append((p2, p1))
                
                # Store velocity as (v2, v1)
                v2, v1 = int(v[1]), int(v[0])
                velocities.append((v2, v1))
    
    result_part_one = day14Q1(positions, velocities)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day14Q2(positions, velocities)
    print("Result for part two: "+str(result_part_two))
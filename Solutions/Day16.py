from collections import deque
import heapq

def day16Q1(route_map):
    row = len(route_map)
    col = len(route_map[0])

    sr, sc = -1, -1  # Start coordinates
    er, ec = -1, -1  # End coordinates

    # Locate the start (S) and end (E) points
    for i in range(row):
        for j in range(col):
            if route_map[i][j] == 'S':
                sr, sc = i, j

    # Define directions
    pq = [(0, sr, sc, 0, 1, [])]  # (cost, r, c, dr, dc, path)
    seen = set()

    while pq:
        cost, r, c, dr, dc, path = heapq.heappop(pq)

        # Skip if the state has already been visited
        if (r, c, dr, dc) in seen:
            continue
        seen.add((r, c, dr, dc))

        # If we reach the end point (E), visualize and return the cost
        if route_map[r][c] == 'E':

            """
            # Create a visualization map
            direction_symbols = {(0, 1): '>', (1, 0): 'v', (0, -1): '<', (-1, 0): '^'}

            path_map = [list(row) for row in route_map]
            for (pr, pc, pdr, pdc) in path:
                if path_map[pr][pc] == '.':
                    path_map[pr][pc] = direction_symbols[(pdr, pdc)]
            path_map[sr][sc] = 'S'
            path_map[er][ec] = 'E'

            
            # Print the visualized path
            for row in path_map:
                print("".join(row))

            """

            return cost

        # Explore all possible moves
        for new_cost, nr, nc, ndr, ndc in [
            (cost + 1, r + dr, c + dc, dr, dc),  # Move forward
            (cost + 1000, r, c, dc, -dr),       # Turn left
            (cost + 1000, r, c, -dc, dr)        # Turn right
        ]:
            # Check bounds and obstacles
            if not (0 <= nr < row and 0 <= nc < col) or route_map[nr][nc] == "#":
                continue
            # Skip if the state has already been visited
            if (nr, nc, ndr, ndc) in seen:
                continue

            # Push the new state into the priority queue, record the path
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc, path + [(r, c, ndr, ndc)]))











def day16Q2(route_map):
    row = len(route_map)
    col = len(route_map[0])

    sr, sc = -1, -1  # Start coordinates
    er, ec = -1, -1  # End coordinates

    # Locate the start (S) and end (E) points
    for i in range(row):
        for j in range(col):
            if route_map[i][j] == 'S':
                sr, sc = i, j
            elif route_map[i][j] == 'E':
                er, ec = i, j

    # Define directions
    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    reverse_directions = {v: k for k, v in directions.items()}  # Reverse mapping for direction symbols

    # Priority queue and data structure initialization
    pq = [(0, sr, sc, 0, 1, '>')]  # (cost, r, c, dr, dc, previous_direction)
    lowest_cost = {(sr, sc, 0, 1): 0}
    backtrack = {}
    best_cost = float("inf")
    end_states = set()

    while pq:
        cost, r, c, dr, dc, prev_dir = heapq.heappop(pq)

        # Skip if the state has a higher cost than the recorded minimum cost
        if cost > lowest_cost.get((r, c, dr, dc), float("inf")):
            continue

        # If we reach the end point (E), record the state
        if route_map[r][c] == "E":
            if cost > best_cost:
                break
            best_cost = cost
            end_states.add((r, c, dr, dc, prev_dir))

        # Explore all possible moves
        for new_cost, nr, nc, ndr, ndc in [
            (cost + 1, r + dr, c + dc, dr, dc),        # Move forward
            (cost + 1000, r, c, dc, -dr),             # Turn left
            (cost + 1000, r, c, -dc, dr)              # Turn right
        ]:
            # Check bounds and obstacles
            if not (0 <= nr < row and 0 <= nc < col) or route_map[nr][nc] == "#":
                continue

            # Update the minimum cost if we find a better path
            lowest = lowest_cost.get((nr, nc, ndr, ndc), float("inf"))
            if new_cost > lowest:
                continue
            if new_cost < lowest:
                backtrack[(nr, nc, ndr, ndc)] = set()
                lowest_cost[(nr, nc, ndr, ndc)] = new_cost

            # Record the path
            backtrack[(nr, nc, ndr, ndc)].add((r, c, dr, dc, reverse_directions[(ndr, ndc)]))
            heapq.heappush(pq, (new_cost, nr, nc, ndr, ndc, reverse_directions[(ndr, ndc)]))

    # Backtrack to find the path
    states = deque(end_states)
    seen = set(end_states)
    unique_arrow_points = set()  # To count unique arrow points
    directions_map = [[None for _ in range(col)] for _ in range(row)]  # To store path directions

    while states:
        key = states.popleft()
        r, c, dr, dc, dir_mark = key

        # Mark the path direction and record unique arrow points
        if (r, c) == (sr, sc):  # Special handling for the start point
            continue
        if route_map[r][c] == '.' or (route_map[r][c] == 'S' and dir_mark != '>'):
            directions_map[r][c] = dir_mark
            unique_arrow_points.add((r, c, dir_mark))  # Record arrow point

        # Add predecessor states
        for last in backtrack.get((r, c, dr, dc), []):
            if last in seen:
                continue
            seen.add(last)
            states.append(last)

    # Special handling for start and end points
    unique_arrow_points.add((sr, sc, 'S'))  # Start point as S
    unique_arrow_points.add((er, ec, 'E'))  # End point as E


    """
    # Print the visualized path

    path_map = [list(row) for row in route_map]
    for r in range(row):
        for c in range(col):
            if directions_map[r][c]:
                path_map[r][c] = directions_map[r][c]
    if directions_map[sr][sc] == '>':
        path_map[sr][sc] = '>'
    else:
        path_map[sr][sc] = 'S'

    print("\nVisualized Path:")
    for row in path_map:
        print("".join(row))

    """

    # Return the count of unique arrow points
    return len(set([(a[0], a[1]) for a in unique_arrow_points]))









if __name__ == "__main__":
    route_map = []

    with open("Inputs/Day16Input.txt", 'r') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        if line.startswith("#") and len(line) > 0:  
            route_map.append(list(line))
        
    result_part_one = day16Q1(route_map)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day16Q2(route_map)
    print("Result for part two: "+str(result_part_two))


        

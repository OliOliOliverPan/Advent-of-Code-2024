def day25Q1(locks, keys):
    row = len(locks[0])
    col = len(locks[0][0])

    pin_heights_locks = [[None] * col for _ in range(len(locks))]
    for k in range(len(locks)):
        
        for i in range(1,row):
            for j in range(col):
                if locks[k][i][j] == '.' and pin_heights_locks[k][j] is None:
                    pin_heights_locks[k][j] = i-1
                if pin_heights_locks[k][j] is not None:
                    continue
    

    pin_heights_keys = [[None] * col for _ in range(len(keys))]
    for k in range(len(keys)):

        for i in range(1,row):
            for j in range(col):
                if keys[k][i][j] == '#' and pin_heights_keys[k][j] is None:
                    pin_heights_keys[k][j] = row - i - 1
                if pin_heights_keys[k][j] is not None:
                    continue
    
    result = 0
    for pin_heights_lock in pin_heights_locks:
        for pin_heights_key in pin_heights_keys:
            
            if any(pin_heights_lock[i] + pin_heights_key[i] > col for i in range(len(pin_heights_lock))):
                continue
            result += 1

    return result







if __name__ == "__main__":
    locks = []
    keys = []

    with open("Inputs/Day25Input.txt", "r") as file:
        data = file.read().strip().split("\n\n")

        for schematic in data:
            nested_list = [list(line) for line in schematic.split("\n")]
            
            top_row = "".join(nested_list[0])
            bottom_row = "".join(nested_list[-1])
            
            if all(i == '#' for i in top_row) and all(i == '.' for i in bottom_row):
                locks.append(nested_list)
            elif all(i == '.' for i in top_row) and all(i == '#' for i in bottom_row):
                keys.append(nested_list)

    result_part_one = day25Q1(locks, keys)
    print("Result for part one: "+str(result_part_one))
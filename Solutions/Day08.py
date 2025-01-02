def day08Q1(lists):
    row = len(lists)
    col = len(lists[0])

    marked = set()

    def is_antenna(x,y):
        return (48<=ord(lists[x][y])<=57) or (65<=ord(lists[x][y])<=90) or (97<=ord(lists[x][y])<=122)

    def find_antinodes(x1,y1,x2,y2):
        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            if y_min - 1 >= 0:
                marked.add((x1,y_min-1))
            if y_max + 1 < col:
                marked.add((x1,y_max+1))

        elif y1 == y2:
            x_min, x_max = min(x1, x2), max(x1, x2)
            if x_min - 1 >= 0:
                marked.add((x_min - 1,y1))
            if x_max + 1 < row:
                marked.add((x_max + 1,y1))
        
        else:

            x_min = min(x1,x2)
            x_max = max(x1,x2)
            y_min = min(y1,y2)
            y_max = max(y1,y2)

            width = y_max - y_min
            height = x_max - x_min

            if (x1 < x2 and y1 < y2) or (x2<x1 and y2<y1):
                
                if y_min - width >= 0 and x_min - height >= 0 :
                    marked.add((x_min-height, y_min-width))
                if y_max + width < col and x_max + height < row:
                    marked.add((x_max+height, y_max + width))
            
            elif (x1 < x2 and y1 >y2) or (x1 > x2 and y1<y2):
                if y_max + width < col and x_min - height >=0:
                    marked.add((x_min - height,y_max + width))
                if y_min - width >= 0 and x_max + height < row:
                    marked.add((x_max + height,y_min - width))

    for i1 in range(row):
        for j1 in range(col):
            if is_antenna(i1,j1):
                for i2 in range(i1, row):
                    start_col = j1 + 1 if i2 == i1 else 0
                    for j2 in range(start_col, col):
                        if is_antenna(i2,j2) and lists[i1][j1] == lists[i2][j2]:
                            find_antinodes(i1,j1,i2,j2)

    return len(marked)









def day08Q2(lists):
    row = len(lists)
    col = len(lists[0])

    marked = set()
    antennas = set()

    def is_antenna(x,y):
        return (48<=ord(lists[x][y])<=57) or (65<=ord(lists[x][y])<=90) or (97<=ord(lists[x][y])<=122)

    def find_antinodes(x1,y1,x2,y2):
        if x1 == x2:
            y_min, y_max = min(y1, y2), max(y1, y2)
            while y_min - 1 >= 0:
                marked.add((x1,y_min-1))
                y_min -= 1
            while y_max + 1 < col:
                marked.add((x1,y_max+1))
                y_max += 1

        elif y1 == y2:
            x_min, x_max = min(x1, x2), max(x1, x2)
            while x_min - 1 >= 0:
                marked.add((x_min - 1,y1))
                x_min -= 1
            while x_max + 1 < row:
                marked.add((x_max + 1,y1))
                x_max += 1
        
        else:

            x_min = min(x1,x2)
            x_max = max(x1,x2)
            y_min = min(y1,y2)
            y_max = max(y1,y2)

            width = y_max - y_min
            height = x_max - x_min

            if (x1 < x2 and y1 < y2) or (x2<x1 and y2<y1):
                
                while y_min - width >= 0 and x_min - height >= 0 :
                    marked.add((x_min-height, y_min-width))
                    y_min -= width
                    x_min -= height
                while y_max + width < col and x_max + height < row:
                    marked.add((x_max+height, y_max + width))
                    y_max += width
                    x_max += height
            
            elif (x1 < x2 and y1 >y2) or (x1 > x2 and y1<y2):

                while y_max + width < col and x_min - height >=0:
                    marked.add((x_min - height,y_max + width))
                    x_min -= height
                    y_max += width
                while y_min - width >= 0 and x_max + height < row:
                    marked.add((x_max + height,y_min - width))
                    x_max += height
                    y_min -= width
            

    for i1 in range(row):
        for j1 in range(col):
            if is_antenna(i1,j1):
                for i2 in range(i1, row):
                    start_col = j1 + 1 if i2 == i1 else 0
                    for j2 in range(start_col, col):
                        if is_antenna(i2,j2) and lists[i1][j1] == lists[i2][j2]:
                            antennas.add((i1,j1))
                            antennas.add((i2,j2))
                            find_antinodes(i1,j1,i2,j2)

    return len(set(list(marked)+list(antennas)))











if __name__ == "__main__":
    
    all_rows = []

    with open("Inputs/Day08Input.txt", "r") as file:
        for line in file:
            
            row = list(map(str, line.split()))  
            all_rows.append(row)
    all_rows = [list(row[0]) for  row in all_rows]

    result_part_one = day08Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day08Q2(all_rows)
    print("Result for part two: "+str(result_part_two))
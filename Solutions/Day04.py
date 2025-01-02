def day04Q1(lists):
    total_count = 0
    for i in range(len(lists)):
        for j in range(len(lists[0])):
            if j <= len(lists[0])-4 and "".join([lists[i][j+k] for k in range(4)]) == "XMAS":
                total_count += 1
            if j >=3 and "".join([lists[i][j-k] for k in range(4)]) == "XMAS":
                total_count += 1
            if i <= len(lists)-4 and "".join(lists[i+k][j] for k in range(4)) == "XMAS":
                total_count += 1
            if i >= 3 and "".join([lists[i-k][j] for k in range(4)]) == "XMAS":
                total_count += 1
            if i>=3 and j >= 3 and "".join([lists[i-k][j-k] for k in range(4)]) == "XMAS":
                total_count += 1
            if i <= len(lists) - 4 and j <= len(lists[0])-4 and "".join([lists[i+k][j+k] for k in range(4)]) == "XMAS":
                total_count += 1
            if i <= len(lists)-4 and j>=3 and "".join([lists[i+k][j-k] for k in range(4)]) == "XMAS":
                total_count += 1
            if i >= 3 and j <= len(lists[0]) - 4 and "".join([lists[i-k][j+k] for k in range(4)]) == "XMAS":
                total_count += 1

    return total_count







def day04Q2(lists):
    total_count = 0
    for i in range(len(lists)-2):
        for j in range(len(lists[0])-2):
            if lists[i][j] == "M" and lists[i][j+2] == "M" and lists[i+1][j+1] == "A" and lists[i+2][j] == "S" and lists[i+2][j+2] == "S":
                total_count += 1
            if lists[i][j] == "S" and lists[i][j+2] == "S" and lists[i+1][j+1] == "A" and lists[i+2][j] == "M" and lists[i+2][j+2] == "M":
                total_count += 1
            if lists[i][j] == "M" and lists[i][j+2] == "S" and lists[i+1][j+1] == "A" and lists[i+2][j] == "M" and lists[i+2][j+2] == "S":
                total_count += 1
            if lists[i][j] == "S" and lists[i][j+2] == "M" and lists[i+1][j+1] == "A" and lists[i+2][j] == "S" and lists[i+2][j+2] == "M":
                total_count += 1
    return total_count










if __name__ == "__main__":
    
    all_rows = []

    with open("Inputs/Day04Input.txt", "r") as file:
        for line in file:
            
            row = list(map(str, line.split()))  
            all_rows.append(row)
    all_rows = [row[0] for row in all_rows]
    
    result_part_one = day04Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day04Q2(all_rows)
    print("Result for part two: "+str(result_part_two))
        
       

                
                
def check_safety(li):
    monotonic =  all(x<y for x,y in zip(li,li[1:])) or all(x>y for x,y in zip(li,li[1:]))

    if monotonic:
        i = 1
        while i < len(li):
            if abs(li[i] - li[i-1]) >=1 and abs(li[i] - li[i-1]) <= 3:
                i += 1
            else:
                break
        return i == len(li)




def day02Q1(lists):
    total_safe = 0
    for li in lists:
        if check_safety(li):
            total_safe += 1
    
    return total_safe





def day02Q2(lists):
    total_safe = 0
    for li in lists:
        for i in range(len(li)):
            temp = li[i]
            del li[i]
            if check_safety(li):
                total_safe += 1
                break
            else:
                li.insert(i,temp)
    return total_safe







if __name__ == "__main__":
    
    all_rows = []

    
    with open("Inputs/Day02Input.txt", "r") as file:
        for line in file:
            
            row = list(map(int, line.split()))  
            all_rows.append(row)
        result_part_one = day02Q1(all_rows)
        print("Result for part one: "+ str(result_part_one))

        result_part_two = day02Q2(all_rows)
        print("Result for part two: "+ str(result_part_two))

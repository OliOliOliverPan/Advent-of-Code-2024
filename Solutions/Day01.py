def day01Q1(li_one, li_two):
    li_one.sort()
    li_two.sort()
    total_distance = sum([abs(li_two[i]-li_one[i]) for i in range(len(li_one))])

    return total_distance




def day01Q2(li_one,li_two):
    similarity = 0
    li_one.sort()
    li_two.sort()

    li_two_pointer = 0
    for num in li_one:
        count = 0
        while li_two_pointer < len(li_two) and li_two[li_two_pointer] <= num:
            if li_two[li_two_pointer] == num:
                count += 1
            li_two_pointer += 1
   
        similarity += num * count
    
    return similarity






if __name__ == "__main__":

    list1 = []
    list2 = []

    with open("Inputs/Day01Input.txt", "r") as file:
        for line in file:
            col1, col2 = map(int, line.split())
            list1.append(col1)
            list2.append(col2)
    
    result_part_one = day01Q1(list1,list2)
    print("Result for part one: "+ str(result_part_one))

    result_part_two = day01Q2(list1, list2)
    print("Result for part two: " + str(result_part_two))


def day07Q1(lists):
    total_sum = 0
    
    for li in lists:
        target = li[0]
        
        def is_possible(target, li):
            def evaluate(idx, current_value):
            
                if idx == len(li):
                    return current_value == target
                
                return (evaluate(idx + 1, current_value + li[idx]) or
                        evaluate(idx + 1, current_value * li[idx]))
            
            
            return evaluate(idx=0, current_value=0)
        
        if is_possible(target, li[1:]):
            total_sum += target
    
    return total_sum









def day07Q2(lists):
    def is_possible(numbers, target):
        def evaluate(index, current_value):
            if index == len(numbers):
                return current_value == target

            current_number = numbers[index]

            # three possible operations: addition, multiplication, concatenation
            return (
                evaluate(index + 1, current_value + current_number) or
                evaluate(index + 1, current_value * current_number) or
                evaluate(index + 1, int(str(current_value) + str(current_number)))
            )

        return evaluate(1, numbers[0])

    total_sum = 0

    for li in lists:
            target = li[0]
            numbers = li[1:]

            if is_possible(numbers, target):
                total_sum += target

    return total_sum











if __name__ == "__main__":
    
    all_rows = []

    with open("Inputs/Day07Input.txt", "r") as data:
        for line in data:
            if line.strip():
                numbers = list(map(int, line.replace(':', '').split()))
                all_rows.append(numbers)

    result_part_one = day07Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day07Q2(all_rows)
    print("Result for part two: "+str(result_part_two))

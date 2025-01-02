def day05Q1(rules, lists):
    middle_number_sum = 0
   
    for li in lists:
        is_valid = True
        for i in range(len(li)-1):
            if f"{li[i]}|{li[i+1]}" not in rules:
                is_valid = False
                break
        if is_valid:
            middle_number_sum += li[len(li)//2]

    return middle_number_sum








def fix_update(li, rules):
    # Initialize a new list with the first element of the input list.
    # This will serve as the "fixed" list we build step by step.
    fixed_li = [li[0]]
    for page in li[1:]:
        inserted = False
        for i in range(len(fixed_li)):
            # Insert the page if it satisfies one of these conditions:
            # 1. The rule explicitly allows fixed_li[i] to come before 'page'
            # 2. There is no rule explicitly requiring 'page' to come before fixed_li[i]
            if f"{fixed_li[i]}|{page}" in rules or f"{page}|{fixed_li[i]}" not in rules:
                fixed_li.insert(i, page) #Insert 'page' at position i
                inserted = True
                break # Exit the loop once the page is inserted
            
        # If the page has not been inserted, append it to the end of the list.
        if not inserted:
            fixed_li.append(page)
    fixed_li.reverse()
    return fixed_li



def day05Q2(rules, lists):
    middle_number_sum = 0
    for li in lists:
        is_valid = True
        for i in range(len(li) - 1):
            if f"{li[i]}|{li[i+1]}" not in rules:
                is_valid = False
                break
        
        if not is_valid:
            li = fix_update(li, rules)
            middle_number_sum += li[len(li) // 2]

    return middle_number_sum









if __name__ == "__main__":
    rules = []
    lists = []

    with open('Inputs/Day05Input.txt', 'r', encoding='utf-8') as file:
        found_blank_line = False

        for line in file:
            stripped_line = line.strip()

            if not found_blank_line:
                if stripped_line == "":
                    found_blank_line = True
                else:
                    rules.append(stripped_line) 
            else:

                if stripped_line:
                    stripped_line = list(map(int, stripped_line.split(',')))
                    lists.append(stripped_line) 

    result_part_one = day05Q1(rules,lists)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day05Q2(rules,lists)
    print("Result for part two: "+str(result_part_two))


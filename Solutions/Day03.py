import regex


def extract_numbers_from_window(input_string,start_idx,end_idx):
    pattern = r"mul\((\d+),(\d+)\)"
    substring = input_string[start_idx:end_idx]
    matches = regex.findall(pattern, substring)

    number_pairs = [(int(a), int(b)) for a,b in matches]

    return number_pairs




def day03Q1(input_string):
    number_pairs = extract_numbers_from_window(input_string,0,len(input_string))
    result = sum([num[0]*num[1] for num in number_pairs])

    return result







def day03Q2(input_string):
    total_sum = 0
    enabled = True
    idx = 0
    length = len(input_string)

    while idx < length:
        if input_string[idx:idx+4] == "do()":
            enabled = True
            idx += len("do()")
            continue

        elif input_string[idx:idx+7] == "don't()":
            enabled = False
            idx += len("don't()")
            continue
            
        if enabled:
            next_dont = input_string.find("don't()",idx)
            end_idx = next_dont
            
            number_pairs = extract_numbers_from_window(input_string,idx, end_idx)
            total_sum += sum([num[0]*num[1] for num in number_pairs])
            idx = end_idx
        else:
            idx += 1
    return total_sum





if __name__ == "__main__":

    with open("Inputs/Day03Input.txt","r") as file:
        content = file.read().replace("\n"," ")
    
    result_part_one = day03Q1(content)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day03Q2(content)
    print("Result for part two: "+str(result_part_two))

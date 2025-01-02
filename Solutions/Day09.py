def day09Q1(nums):
    digit = 0
    is_digit = True
    result = []

    pointer = 0
    while pointer < len(nums):
        cur = int(nums[pointer])

        if is_digit:
            result += [digit] * cur
            digit += 1
            is_digit = False   
        else:
            result += ["."] * cur
            is_digit = True
        pointer += 1
    
    pointer_head = 0
    pointer_tail = len(result) - 1

    while pointer_head < pointer_tail:
        if result[pointer_head] == ".":
            while result[pointer_tail] == ".":
                pointer_tail -= 1
            result[pointer_head], result[pointer_tail] = result[pointer_tail], "."
        pointer_head += 1

    result_list_digit = result[:pointer_tail]

    return sum([i * result_list_digit[i] for i in range(len(result_list_digit))])







    
    
def day09Q2(nums):
    # Parse the input to create a sequence of file blocks and free spaces
    digit = 0  # File ID
    is_digit = True  # Toggle between file length and free space length
    blocks = []  # List representation of the disk layout
    file_starts = []  # List to store the starting indices of each file

    pointer = 0  # Pointer for traversing the input
    while pointer < len(nums):
        cur = int(nums[pointer])  # Current digit in the input
        if is_digit:
            file_starts.append(len(blocks))  # Record the start index of this file
            blocks += [digit] * cur  # Add file blocks to the layout
            digit += 1  # Increment the file ID for the next file
            is_digit = False  # Switch to handling free spaces next
        else:
            blocks += [None] * cur  # Add free space blocks to the layout
            is_digit = True  # Switch to handling file blocks next
        pointer += 1  # Move to the next character in the input

    # Function to find the first gap large enough to fit a file
    def find_first_gap(target_length):
        for idx in range(len(blocks)):
            # Check if the gap starts with enough None values
            if blocks[idx] is None and idx + target_length <= len(blocks):
                if all(blocks[idx + i] is None for i in range(target_length)):
                    return idx  # Return the starting index of the gap
        return None  # Return None if no suitable gap is found

    # Process files in reverse order of their starting positions
    while file_starts:
        idx = file_starts.pop()  # Get the start index of the current file
        file_id = blocks[idx]  # Get the file ID
        end = idx  # Initialize the end index for the file

        # Determine the end index of the file
        while end + 1 < len(blocks) and blocks[end + 1] == file_id:
            end += 1
        length = end - idx + 1  # Calculate the length of the file

        # Find the first available gap large enough to hold the file
        dest = find_first_gap(length)
        if dest is None:
            continue  # If no gap is found, skip to the next file
        if dest < idx:  # Ensure the target position is before the current position
            for i in range(length):
                blocks[dest + i] = file_id  # Move the file to the target position
                blocks[idx + i] = None  # Clear the original position

    # Calculate the checksum based on the final layout
    checksum = 0
    for pos, block in enumerate(blocks):
        if block is not None:  # Skip free space blocks
            checksum += pos * block  # Multiply position by file ID and sum

    return checksum







if __name__ == "__main__":
    with open('Inputs/Day09Input.txt', 'r', encoding='utf-8') as file:
        text = file.readline().strip()

    result_part_one = day09Q1(text)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day09Q2(text)
    print("Result for part two: "+str(result_part_two))



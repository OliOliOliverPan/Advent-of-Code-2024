def day11Q1(stones, blinking=25):

    def blink_once(stones):
        updated_stones = []
        for stone in stones:
            if stone == 0:
                stone += 1
                updated_stones.append(stone)
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                stone_left, stone_right = int(stone_str[:int(len(stone_str)/2)]),int(stone_str[int(len(stone_str)/2):])
                updated_stones.append(stone_left)
                updated_stones.append(stone_right)
                
            else:
                stone = stone * 2024
                updated_stones.append(stone)

        return updated_stones

    for _ in range(blinking):
        stones = blink_once(stones)
    
    return len(stones)







from collections import Counter
def day11Q2(stones, blinking=75):
    stone_counts = Counter(stones)

    for _ in range(blinking):
        new_counts = Counter()
        for stone, count in stone_counts.items():
            if stone == 0:
                new_counts[1] += count
            elif len(str(stone)) % 2 == 0:
                stone_str = str(stone)
                stone_left, stone_right = int(stone_str[:int(len(stone_str)/2)]),int(stone_str[int(len(stone_str)/2):])
                new_counts[stone_left] += count
                new_counts[stone_right] += count
                
            else:
                new_counts[stone * 2024] += count
            stone_counts = new_counts
    return sum(stone_counts.values())









if __name__ == "__main__":

    with open("Inputs/Day11Input.txt", "r") as file:
        for line in file:
            row = list(map(int, line.split(" ")))
    
    result_part_one = day11Q1(row)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day11Q2(row)
    print("Result for part two: "+str(result_part_two))

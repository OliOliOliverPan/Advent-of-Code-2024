def next_secret_number(secret_number):
    procedure_one = ((secret_number * 64) ^ secret_number) % 16777216
    procedure_two =  (((procedure_one) // 32) ^ procedure_one) % 16777216
    procedure_three = ((procedure_two * 2048) ^ procedure_two) % 16777216

    return procedure_three  



def day22Q1(secret_numbers):
    new_secret_numbers = []
    for secret_number in secret_numbers:
        for _ in range(2000):
            secret_number = next_secret_number(secret_number)
        new_secret_numbers.append(secret_number)
    
    return sum(new_secret_numbers)










def generate_price_and_differences(secret_number, steps=2000):
    prices = []
    for _ in range(steps):
        prices.append(secret_number % 10)
        secret_number = next_secret_number(secret_number)

    differences = [(p_next - p) for p, p_next in zip(prices, prices[1:])]
    return prices, differences



def build_diff_map(secret_number, steps=2000):
    prices, differences = generate_price_and_differences(secret_number, steps)
    diff_map = {}
    for i in range(len(differences) - 3):
        single_sequence = (differences[i], differences[i+1], differences[i+2], differences[i+3])
        if single_sequence not in diff_map:
            diff_map[single_sequence] = prices[i+3+1]
    return diff_map



def day22Q2(secret_numbers):
    
    maps = []
    all_single_sequences = set()
    for sn in secret_numbers:
        diff_map = build_diff_map(sn)
        maps.append(diff_map)
        all_single_sequences.update(diff_map.keys())

    total_bananas = []
    for single_sequence in all_single_sequences:
        current_total = 0
        for diff_map in maps:
            if single_sequence in diff_map:
                current_total += diff_map[single_sequence]
        total_bananas.append(current_total)

    return max(total_bananas)

    





if __name__ == "__main__":
    all_rows = []

    with open("Inputs/Day22Input.txt", "r") as file:
        for line in file:       
            row = int(line.strip())
            all_rows.append(row)

    result_part_one = day22Q1(all_rows)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day22Q2(all_rows)
    print("Result for part two: "+str(result_part_two))


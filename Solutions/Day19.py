def day19Q1(towel_patterns, designs):
    results = []

    for design in designs:
        n = len(design)
        dp = [False] * (n+1)
        dp[0] = True # Base case: empty prefix is always achievable

        for i in range(1, n+1):
            for pattern in towel_patterns:
                pattern_len = len(pattern)
                if i>= pattern_len and design[i-pattern_len:i] == pattern:
                    dp[i] = dp[i] or dp[i-pattern_len]

        results.append(dp[n]) # Can the whole design be formed?
    
    return sum(results)







def day19Q2(towel_patterns, designs):
    results = []

    for design in designs:
        n = len(design)
        dp = [0] * (n+1) # dp[i] stores the number of ways to form the first 'i' stripes of the design
        dp[0] = True # Base case: there's one way to form a design of 0 stripe (do nothing)

        for i in range(1, n+1):
            for pattern in towel_patterns:
                pattern_len = len(pattern)
                if i>= pattern_len and design[i-pattern_len:i] == pattern:
                    dp[i] += dp[i-pattern_len]

        results.append(dp[n]) # The number of ways to form the entire design
    
    return sum(results)







if __name__ == "__main__":
    with open("Inputs/Day19Input.txt",'r') as file:
        lines = file.readlines()

    towel_patterns = [pattern.strip() for pattern in lines[0].split(',')]

    designs = [line.strip() for line in lines[1:] if line.strip()]

    result_part_one = day19Q1(towel_patterns,designs)
    print("Result for part one: "+ str(result_part_one))

    result_part_two = day19Q2(towel_patterns, designs)
    print("Result for part two: " + str(result_part_two))


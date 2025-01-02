from collections import deque
from functools import cache
from itertools import product


def compute_seqs(keypad):
    pos = {}
    for r in range((len(keypad))):
        for c in range(len(keypad[r])):
            if keypad[r][c] is not None:
                pos[keypad[r][c]] = (r,c)
    seqs = {}
    for x in pos:
        for y in pos:
            if x==y:
                seqs[(x,y)] = ['A']
                continue
            possibilities = []
            q = deque([(pos[x],"")])
            optimal_length = float('inf')
            while q:
                (r,c), moves = q.popleft()
                for nr,nc,nm in [(r-1,c, '^'),(r+1,c,'v'),(r,c-1,'<'),(r,c+1,'>')]:
                    if nr < 0 or nc < 0 or nr >= len(keypad) or nc >= len(keypad[0]):
                        continue
                    if keypad[nr][nc] is None:
                        continue
                    if keypad[nr][nc] == y:
                        if optimal_length < len(moves+nm):
                            break
                        optimal_length = len(moves+nm)
                        possibilities.append(moves + nm + 'A')
                    else:
                        q.append(((nr,nc), moves +nm))
                else:
                    continue
                break
            seqs[(x,y)] = possibilities
    
    return seqs

def solve(code, keypad):
    seqs = compute_seqs(keypad)
    options = [seqs[(x,y)]for x,y in zip('A'+code, code)]
    
    return ["".join(x) for x in list(product(*options))]





def day21Q1(codes, numeric_keypad, directional_keypad):

    total_complexity = 0

    for code in codes:
        robot1 = solve(code, numeric_keypad)
        next = robot1
        for _ in range(2):
            possible_next = []
            for seq in next:
                possible_next += solve(seq,directional_keypad)
            min_length = min(map(len, possible_next))
            next = [seq for seq in possible_next if len(seq) == min_length]


        shortest_sequence_length = len(next[0])
        complexity = shortest_sequence_length * int(code[:-1])

        total_complexity += complexity

    return total_complexity












        
def day21Q2(code,numeric_keypad,directional_keypad):
    directional_seqs = compute_seqs(directional_keypad)
    directional_lengths = {key: len(value[0]) for key, value in directional_seqs.items()}


    @cache
    def compute_length(seq,depth=25):
        if depth == 1:
            return sum(directional_lengths[(x,y)] for x,y in zip('A'+seq,seq))
        length = 0
        for x,y in zip("A"+seq, seq):
            length += min(compute_length(subseq, depth-1) for subseq in directional_seqs[(x,y)])
        return length

    total_complexity = 0

    for code in codes:
        inputs = solve(code, numeric_keypad)
        length = min(map(compute_length,inputs))
        total_complexity += length * int(code[:-1])

    return total_complexity











if __name__ == "__main__":

    numeric_keypad = [
        ["7","8","9"],
        ["4","5","6"],
        ["1","2","3"],
        [None,"0","A"]
        ]
    
    directional_keypad = [
        [None, "^","A"],
        ["<","v",">"]
    ]

    with open('Inputs/Day21Input.txt', 'r') as file:
        codes = [line.strip() for line in file]
    
    result_part_one = day21Q1(codes,numeric_keypad,directional_keypad)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day21Q2(codes,numeric_keypad, directional_keypad)
    print("Result for part two: "+str(result_part_two))
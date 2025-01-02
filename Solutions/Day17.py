def get_combo_operand(literal_operand,a,b,c):
            if 0 <= literal_operand <=3:
                return literal_operand
            elif literal_operand == 4:
                return a
            elif literal_operand == 5:
                return b
            elif literal_operand == 6:
                return c
            elif literal_operand == 7:
                raise ValueError("combo operand 7 is reserved and will not appear in valid programs")



def run_program(a,b,c,program):

    output = []
     
    i = 0
    while i < len(program):

        opcode = program[i]
        literal_operand = program[i+1]

        if opcode == 0:
            combo_operand = get_combo_operand(literal_operand,a,b,c)
            a //= (2**combo_operand)
        elif opcode == 1:
            b ^= literal_operand
    
        elif opcode == 2:
            combo_operand = get_combo_operand(literal_operand,a,b,c)
            b = combo_operand % 8
    
        elif opcode == 3:
            if a != 0:
                i = literal_operand
                continue
    
        elif opcode == 4:
            b ^= c
        elif opcode == 5:
            combo_operand = get_combo_operand(literal_operand,a,b,c)
            output.append(str(combo_operand % 8))
        elif opcode == 6:
            combo_operand = get_combo_operand(literal_operand,a,b,c)
            b = a // (2**combo_operand)
        elif opcode == 7:
            combo_operand = get_combo_operand(literal_operand,a,b,c)
            c = a // (2**combo_operand)
        
        i += 2
    
    return output



def day17Q1(a, b, c, program):
    result = run_program(a,b,c,program)
    return ",".join(map(str,result))








def day17Q2(target):
    def daySeventeenQ2Solver(target, a_min):
        if target == []:
            return a_min
        for t in range(8):
            a = (a_min << 3) | t
            b = 0
            c = 0
            output = None
            adv3 = False

            for i in range(0, len(program) - 2, 2):
                opcode = program[i]
                literal_operand = program[i + 1]
                if opcode == 0:
                    assert not adv3, "program has multiple ADVs"
                    assert literal_operand == 3, "program has ADV with literal operand other than 3"
                    adv3 = True
                elif opcode == 1:
                    b ^= literal_operand
                elif opcode == 2:
                    b = get_combo_operand(literal_operand, a, b, c) % 8
                elif opcode == 3:
                    raise AssertionError("program has JNZ inside expected loop body")
                elif opcode == 4:
                    b ^= c
                elif opcode == 5:
                    assert output is None, "program has multiple OUTs"
                    output = get_combo_operand(literal_operand, a, b, c) % 8
                elif opcode == 6:
                    b = a >> get_combo_operand(literal_operand, a, b, c)
                elif opcode == 7:
                    c = a >> get_combo_operand(literal_operand, a, b, c)
                
                if output == target[-1]:
                    sub = daySeventeenQ2Solver(target[:-1], a)
                    if sub is None:
                        continue
                    return sub
    
    a_min = 0
    return daySeventeenQ2Solver(target, a_min)








if __name__ == "__main__":
    with open("Inputs/Day17Input.txt", 'r') as file:
        lines = [line.strip() for line in file if line.strip()] 

    register_a = int(lines[0].split(":")[1].strip())
    register_b = int(lines[1].split(":")[1].strip())
    register_c = int(lines[2].split(":")[1].strip())
    
    program_line = lines[3].split(":")[1].strip()
    program = list(map(int, program_line.split(",")))

    result_part_one = day17Q1(register_a,register_b,register_c,program)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day17Q2(program)
    print("Result for part two: "+str(result_part_two))


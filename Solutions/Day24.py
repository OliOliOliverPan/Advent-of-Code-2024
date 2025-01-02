def compute_gate_output(gate, x,y):
    if gate == 'AND':
        return x and y
    elif gate == 'OR':
        return x or y
    elif gate == 'XOR':
        return x ^ y



def day24Q1(inputs, logics):

    wire_names = [input[0] for input in inputs]
    wire_values = [input[1] for input in inputs]
    wires = {
    name: value
    for name, value in zip(wire_names, wire_values)
    }


    while len(logics) > 0:
        to_remove = []
        for target, (op,x,y) in logics.items():
            if x in wires.keys() and y in wires.keys():
                wires[target] = compute_gate_output(op, wires[x], wires[y])
                to_remove.append(target)

        for k in to_remove:
            del logics[k]
            

    z_wires = sorted([(x,y) for (x,y) in wires.items() if x.startswith('z')], key = lambda t: t[0])[::-1]
    result = int("".join([str(z[1]) for z in z_wires]),2)
    return result










def make_wire(char, num):
    return char + str(num).rjust(2, "0")



def verify_z(wire, logics, num):

    if wire not in logics: 
        return False
    op, x, y = logics[wire]
    if op != "XOR": 
        return False
    if num == 0: 
        return sorted([x, y]) == ["x00", "y00"]
    return (verify_intermediate_xor(x, logics, num) and verify_carry_bit(y,logics, num)) or (verify_intermediate_xor(y, logics, num) and verify_carry_bit(x, logics, num))



def verify_intermediate_xor(wire, logics, num):

    if wire not in logics: 
        return False
    op, x, y = logics[wire]
    if op != "XOR": 
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]



def verify_carry_bit(wire, logics, num):
 
    if wire not in logics: 
        return False
    op, x, y = logics[wire]
    if num == 1:
        if op != "AND": 
            return False
        return sorted([x, y]) == ["x00", "y00"]
    if op != "OR": 
        return False
    return (verify_direct_carry(x, logics, num - 1) and verify_recarry(y, logics, num - 1)) or (verify_direct_carry(y, logics, num - 1) and verify_recarry(x, logics, num - 1))



def verify_direct_carry(wire, logics, num):

    if wire not in logics: 
        return False
    op, x, y = logics[wire]
    if op != "AND": 
        return False
    return sorted([x, y]) == [make_wire("x", num), make_wire("y", num)]



def verify_recarry(wire, logics, num):

    if wire not in logics: 
        return False
    op, x, y = logics[wire]
    if op != "AND": 
        return False
    return (verify_intermediate_xor(x, logics,num) and verify_carry_bit(y, logics, num)) or (verify_intermediate_xor(y, logics, num) and verify_carry_bit(x, logics, num))



def verify(logics, num):
    return verify_z(make_wire("z", num), logics, num)



def progress(logics):
    i = 0
    
    while True:
        if not verify(logics,i): 
            break
        i += 1
    
    return i



def day24Q2(logics):
    swaps = []

    for _ in range(4):
        baseline = progress(logics)
        for x in logics:
            for y in logics:
                if x == y: 
                    continue
                logics[x], logics[y] = logics[y], logics[x]
                if progress(logics) > baseline:
                    break
                logics[x], logics[y] = logics[y], logics[x]
            else:
                continue
            break
        swaps += [x, y]

    return ",".join(sorted(swaps))
    






import copy
if __name__ == '__main__':

    input_list = []
    logics = dict()

    with open('Inputs/Day24Input.txt', 'r') as file:
        lines = file.readlines()

    is_logic_section = False

    for line in lines:
        line = line.strip()
        if not line:
            is_logic_section = True
            continue

        if not is_logic_section:
            key, value = line.split(':')
            input_list.append((key.strip(), int(value.strip())))
        else:
            parts = line.split()
            if len(parts) == 5 and parts[3] == '->':
                logics[parts[4]] = (parts[1], parts[0], parts[2])

    logics_copy = copy.deepcopy(logics)


    result_part_one = day24Q1(input_list, logics)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day24Q2(logics_copy)
    print("Result for part two: "+str(result_part_two))
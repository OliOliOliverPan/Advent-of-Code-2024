import numpy as np
from scipy.linalg import solve


def day13Q1(matrices, vectors):
    total_pushes = 0
    for i, (matrix, vector) in enumerate(zip(matrices, vectors)):
        x = solve(matrix, vector).flatten()
        A,B = map(round, x)
        
        if [A * matrix[0][0] + B * matrix[0][1], A * matrix[1][0] + B * matrix[1][1]] == vector.flatten().tolist():
            if A >= 0 and B >= 0 and A <= 100 and B <= 100:
                total_pushes += 3*A+1*B

    return total_pushes








def day13Q2(matrices, vectors):
    total_pushes = 0
    for _, (matrix, vector) in enumerate(zip(matrices, vectors)):
        x = solve(matrix, vector).flatten()
        A,B = map(round, x)
        
        if [A * matrix[0][0] + B * matrix[0][1], A * matrix[1][0] + B * matrix[1][1]] == vector.flatten().tolist():
            if A > 100 and B > 100:
                total_pushes += 3*A+1*B

    return total_pushes








if __name__ == "__main__":
    matrices = []
    vectors = []

    with open('Inputs/Day13Input.txt', 'r') as file:
        lines = [line.strip() for line in file if line.strip()]  # Remove empty lines

    # Iterate through groups of 3 lines
    for i in range(0, len(lines), 3):
        if i + 2 >= len(lines):
            print(f"Skipping incomplete group at index {i}")
            break

        # Parse Button A
        
        button_a_line = lines[i]
        a_coords = button_a_line.split(':')[1].split(',')
        a_x = int(a_coords[0].strip()[2:])  # Extract the number after 'X+'
        a_y = int(a_coords[1].strip()[2:])  # Extract the number after 'Y+'


        # Parse Button B
        
        button_b_line = lines[i + 1]
        b_coords = button_b_line.split(':')[1].split(',')
        b_x = int(b_coords[0].strip()[2:])  # Extract the number after 'X+'
        b_y = int(b_coords[1].strip()[2:])  # Extract the number after 'Y+'
        

        # Parse Prize
        
        prize_line = lines[i + 2]
        prize_coords = prize_line.split(':')[1].split(',')  # Extract after ':'
        prize_x = int(prize_coords[0].strip()[2:])  # Extract the number after 'X='
        prize_y = int(prize_coords[1].strip()[2:])  # Extract the number after 'Y='
        

        # Create matrix and vector
        matrix = np.array([[a_x, b_x], [a_y, b_y]])
        vector = np.array([[prize_x], [prize_y]])

        matrices.append(matrix)
        vectors.append(vector)



    matrices, vectors_q1 = np.array(matrices), np.array(vectors)
    vectors_q2 = vectors_q1 + 10000000000000

    result_part_one = day13Q1(matrices, vectors_q1)
    print("Result for part one: "+str(result_part_one))

    result_part_two = day13Q2(matrices, vectors_q2)
    print("Result for part two: "+str(result_part_two))

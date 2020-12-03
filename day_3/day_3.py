def get_numbers(input_file):
    numbers = []
    with open(input_file, 'r') as input:
        for line in input:
            temp = line.strip()
            numbers.append(temp)
    return numbers

field = get_numbers("input.txt")

def count_trees(slope):
    p, q = slope
    i = 0
    j = 0
    count = 0
    while i < len(field):

        if field[i][j] == '#':
            count += 1

        i += p
        if q == 1:
            j = (j + q) % len(field[0])
        else:
            j = (i * q) % len(field[0])

    return count

result = count_trees((1, 1)) * count_trees((1, 3)) * count_trees((1, 5)) * count_trees((1, 7)) * count_trees((2, 1))

print(result)
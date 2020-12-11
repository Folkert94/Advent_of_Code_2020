def get_numbers(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

data = get_numbers("input.txt")

change = 1
while change == 1:
    change = 0
    new_field = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            current_state = data[i][j]
            adj_occ = 0
            if i - 1 >= 0
                if j - 1 >= 0:
                    if data[i - 1][j - 1] == '#':
                        adj_occ += 1
            if i - 1 >= 0
                if j - 1 >= 0:
                    if data[i - 1][j] == '#':
                        adj_occ += 1
            if i - 1 >= 0
                if j + 1 < len(data[i]):
                    if data[i - 1][j + 1] == '#':

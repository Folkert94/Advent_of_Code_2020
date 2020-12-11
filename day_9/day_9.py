def get_numbers(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            data.append(int(line.strip()))
    return data

data = get_numbers("input.txt")


preamble = 25

i = preamble
while i < len(data) - 1:
    n = data[i + 1]
    numbers = data[i - 25:i]

    

    i += 1
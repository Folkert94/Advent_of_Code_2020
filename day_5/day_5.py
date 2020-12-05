def get_numbers(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            data.append(line.strip())
    return data

data = get_numbers("input.txt")

highest_id = 0

seat_ids = []

for seat in data:
    two_halfs = [[0, 63], [64, 127]]
    i = 0
    while i < 7:
        if seat[i] == 'F':
            temp = two_halfs[0]
            if temp[1] == temp[0]:
                row = temp[0]
            temp_range = ((temp[1] - 1) - temp[0]) / 2 
            two_halfs = [[temp[0], int(temp[0] + temp_range)], [int(temp[0] + temp_range) + 1, temp[1]]] 
        if seat[i] == 'B':
            temp = two_halfs[1]
            if temp[1] == temp[0]:
                row = temp[0]
            temp_range = ((temp[1] - 1) - temp[0]) / 2 
            two_halfs = [[temp[0], int(temp[0] + temp_range)], [int(temp[0] + temp_range) + 1, temp[1]]]
        i += 1
    

    two_halfs = [[0, 3], [4, 7]]
    while i < 10:
        if seat[i] == 'L':
            temp = two_halfs[0]
            if temp[1] == temp[0]:
                column = temp[0]
            temp_range = ((temp[1] - 1) - temp[0]) / 2 
            two_halfs = [[temp[0], int(temp[0] + temp_range)], [int(temp[0] + temp_range) + 1, temp[1]]] 
        if seat[i] == 'R':
            temp = two_halfs[1]
            if temp[1] == temp[0]:
                column = temp[0]
            temp_range = ((temp[1] - 1) - temp[0]) / 2 
            two_halfs = [[temp[0], int(temp[0] + temp_range)], [int(temp[0] + temp_range) + 1, temp[1]]]
        i += 1

    seat_id = (row * 8) + column

    seat_ids.append(seat_id)

    if seat_id > highest_id:
        highest_id = seat_id

for i in range(len(seat_ids)):
    if i not in seat_ids:
        print(i)


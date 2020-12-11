def get_numbers(input_file):
    data = ""
    with open(input_file, 'r') as f:
        data = f.read()
    return data

data = get_numbers("input.txt")
data = data.split("\n\n")

count = 0
for line in data:
    count += len((set(line.replace("\n", ""))))

print(count)

count = 0
for line in data:
    all_items = set(line.replace("\n", ""))
    for item in all_items:
        temp_count = 0
        for questions in line.replace("\n", " ").split():
            if item in questions:
                temp_count += 1
        if temp_count == len(line.replace("\n", " ").split()):
            count += 1
    # print(line.replace("\n", " ").split())

print(count)
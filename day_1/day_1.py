numbers = []
with open("input.txt", 'r') as input:
    for line in input:
        numbers.append(int(line.strip()))

i = 0
while i < len(numbers) - 1:
    j = len(numbers) - 1
    while numbers[j] + numbers[i] != 2020 and j >= 0:
        j -= 1
    if numbers[i] + numbers[j] == 2020:
        print(numbers[i] * numbers[j])
        break
    i += 1

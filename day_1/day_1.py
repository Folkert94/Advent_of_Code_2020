
def get_numbers(input_file):
    numbers = []
    with open(input_file, 'r') as input:
        for line in input:
            numbers.append(int(line.strip()))
    return numbers

def find_two_numbers(result):
    i = 0
    while i < len(numbers) - 1:
        j = len(numbers) - 1
        while numbers[j] + numbers[i] != result and j >= 0:
            j -= 1
        if numbers[i] + numbers[j] == result:
            return numbers[i] * numbers[j]
            break
        i += 1

def find_three_numbers(result):
    i = 0
    while i < len(numbers) - 1:
        j = i + 1
        while j < len(numbers) - 1:
            z = j + 1
            while z < len(numbers) - 1 and numbers[i] + numbers[j] + numbers[z] != result:
                z += 1
            if numbers[i] + numbers[j] + numbers[z] == result:
                return numbers[i] * numbers[j] * numbers[z]
            j += 1
        i += 1

if __name__ == "__main__":
    numbers = get_numbers("input.txt")

    day_1_1 = find_two_numbers(2020)
    print(day_1_1)    
    day_1_2 = find_three_numbers(2020)
    print(day_1_2)


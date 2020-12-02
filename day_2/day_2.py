
def get_numbers(input_file):
    numbers = []
    with open(input_file, 'r') as input:
        for line in input:
            temp = line.strip().split(":")
            policy = temp[0]
            passw = temp[1]
            numbers.append([passw, policy])
    return numbers

def policy_1(input_list):
    counter = 0
    for passw in input_list:
        temp = passw[1].split()
        low, high = temp[0].split("-")
        character = temp[1]
        if passw[0].count(character) >= int(low) and passw[0].count(character) <= int(high):
            counter += 1
    return counter

def policy_2(input_list):
    counter = 0
    for passw in input_list:
        password = passw[0].strip()
        temp = passw[1].split()
        first, second = temp[0].split("-")
        character = temp[1]
        if bool(password[int(first) - 1] == character) != bool(password[int(second) - 1] == character):
            counter += 1
            print(password, first, second, character)
    return counter

if __name__ == "__main__":
    input_list = get_numbers("input.txt")
    counter1 = policy_1(input_list)
    print(counter1)
    counter2 = policy_2(input_list)
    print(counter2)

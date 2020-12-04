import re

def get_numbers(input_file):
    data = ""
    with open(input_file, 'r') as f:
        data = f.read()
    return data

data = get_numbers("input.txt")
data = data.split("\n\n")

fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

count = 0
for line in data:
    all_fields = {}
    for field in line.replace("\n", " ").split():
        temp = field.split(":")
        all_fields[temp[0]] = temp[1]

    if len(all_fields) == 8 or (len(all_fields) == 7 and 'cid' not in all_fields):
        checks = 0
        if len(all_fields['byr']) == 4 and (int(all_fields['byr']) >= 1920 and int(all_fields['byr']) <= 2002):
            checks += 1
        if len(all_fields['iyr']) == 4 and (int(all_fields['iyr']) >= 2010 and int(all_fields['iyr']) <= 2020):
            checks += 1
        if len(all_fields['eyr']) == 4 and (int(all_fields['eyr']) >= 2020 and int(all_fields['eyr']) <= 2030):
            checks += 1
        if re.search("\d{2,}\w{2,}", all_fields['hgt']):
            temp_hgt = re.findall(r'[A-Za-z]+|\d+', all_fields['hgt'])
            if (temp_hgt[1] == 'cm' and (int(temp_hgt[0]) >= 150 and int(temp_hgt[0]) <= 193)) or (temp_hgt[1] == 'in' and (int(temp_hgt[0]) >= 59 and int(temp_hgt[0]) <= 76)):
                checks += 1
        if re.search("[#]\S{6}", all_fields['hcl']):
            checks += 1
        if len(all_fields['ecl']) == 3 and all_fields['ecl'] in eye_color:
            checks += 1
        if re.search("([0-9]{9})", all_fields['pid']) and len(all_fields['pid']) == 9:
            checks += 1
        
        if checks == 7:    
            count += 1
        

print(count)

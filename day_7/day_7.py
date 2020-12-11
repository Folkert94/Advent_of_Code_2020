import itertools

def get_numbers(input_file):
    data = []
    with open(input_file, 'r') as f:
        for line in f:
            data.append(line.replace(",", "").replace(".", "").split())
    return data

bag_dict = {}

rules = get_numbers("input.txt")
for rule in rules:
    temp = {}
    rule.remove("contain")
    while "bags" in rule:
        rule.remove("bags")
    while "bag" in rule:
        rule.remove("bag")
    i = 2 
    while i < len(rule) - 2:
        temp[" ".join([rule[i + 1], rule[i + 2]])] = int(rule[i]) 
        i += 3
    bag_dict[" ".join([rule[0], rule[1]])] = temp

temp_list = []
total_list = []

for bag in bag_dict:
    if "shiny gold" in bag_dict[bag]:
        temp_list.append(bag)

total_list.append(temp_list)

next_list = temp_list

while next_list != []:
    temp_list = []
    for temp_bag in next_list:
        for bag in bag_dict:
            if temp_bag in bag_dict[bag]:
                temp_list.append(bag)
    total_list.append(temp_list)
    next_list = temp_list

print(len(set(list(itertools.chain.from_iterable(total_list)))))

class Leaf():
    def __init__(self, current, parent, next_list):
        self.parent = parent
        self.current = current
        self.next = next_list

    def __repr__(self):
        return "{}, parent: [{}], next: {}".format(self.current, self.parent, self.next)

top_leaf = Leaf('shiny gold', None, ['dull white', 'dark orange'])

items = []
for item in list(bag_dict['shiny gold'].keys()):
    items.append(Leaf(item, top_leaf, list(bag_dict[item].keys())))

i = 0
while i < len(items):
    for item in items[i].next:
        items.append(Leaf(item, items[i], list(bag_dict[item].keys())))
    i += 1
count = 0
for item in items:
    count += bag_dict[item.parent.current][item] * sum(list(bag_dict[item].values()))

print(count)
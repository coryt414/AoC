import string

filename = "Day3_Input.txt"
lower_letters = list(string.ascii_lowercase)
upper_letters = list(string.ascii_uppercase)

priorities = {}

def letters_assignment():
    i = 1

    for item in lower_letters:
        priorities[item] = i
        i += 1
        
    for item in upper_letters:
        priorities[item] = i
        i += 1

def rucksack_review(filename):
    important_items = []
    sum = 0
    with open(filename, 'r') as data:
        i = 1
        for line in data:
            rucksack = line.strip("\n")
            partition1 = []
            partition2 = []
            half = int(len(rucksack)/2)
            partition1 = (rucksack[0:half])
            partition2 = rucksack[half:]
            print(partition1)
            print(partition2)
            trigger = 0
            for item1 in partition1:
                for item2 in partition2:
                    if item1 == item2 and trigger == 0:
                        important_items.append(item1)
                        print(str(i))
                        sum += priorities[item1]
                        trigger = 1
                        i += 1
                        break
            print(sum)

letters_assignment()
rucksack_review(filename)
# print(priorities)
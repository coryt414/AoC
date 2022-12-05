import string

filename = "Day 3\Day3_Input.txt"
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
    i = 0
    with open(filename, 'r') as data:
        three_elf_group = []
        first_elf = []
        second_elf = []
        third_elf = []
        for line in data:
            rucksack = line.strip("\n")
            three_elf_group.append(rucksack)
        for elf in three_elf_group:
            if i % 3 == 0: 
                first_elf.append(elf)
            if i % 3 == 1:
                second_elf.append(elf)
            if i % 3 == 2:
                third_elf.append(elf)
            i += 1
        j = 0
        print(first_elf)
        print(second_elf)
        print(third_elf)

        if j < 100:
            for elf in first_elf:
                trigger = 0
                for item1 in elf:
                    if trigger == 0:
                        for item2 in second_elf[j]:
                            if j < 100:
                                if item1 == item2:
                                    for item3 in third_elf[j]:
                                        if j < 100:
                                            if item2 == item3:
                                                sum += priorities[item1]
                                                
                                                print(j)
                                                print(item1)
                                                print(priorities[item1])
                                                print(sum)
                                                item1 = 0
                                                item2 = 0
                                                item3 == 0
                                                j += 1
                                                trigger = 1;
                                                break


    # for item1 in three_elf_group[i]:
    #     trigger = 0
    #     print(three_elf_group[i])
    #     print(three_elf_group[i+1])
    #     print(three_elf_group[i+2])
    #     for item2 in three_elf_group[i+1]:
    #         if item1 == item2:
    #             for item3 in three_elf_group[i+2]:
    #                 if item2 == item3:
    #                         sum += priorities[item3]
    #                         i += 3
    #                         print(i)
    #                         print(item3)
    #                         trigger = 1
    #                         print(sum)
                                    

                #three_elf_group = []
            #print(len(three_elf_group))
            #print(sum)

letters_assignment()
rucksack_review(filename)
# print(priorities)
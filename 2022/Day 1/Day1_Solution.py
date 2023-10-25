filename = "Day 1\Day1_Input.txt"
elf_totals = []


def elf_calories():
    total_calories = 0
    for line in data:
        if line == "\n":
            elf_totals.append(total_calories)
            total_calories = 0
        else:
            total_calories += int((line.strip()))

with open(filename, 'r') as data:
    elf_calories()
    elf_totals.sort()
    print("Most calories: "+ str(elf_totals[-1]))
    print("Calories from top 3 elves: " + str(sum(elf_totals[-3:])))
    
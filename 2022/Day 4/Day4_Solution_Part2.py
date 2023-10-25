filename = "Day 4\Day4_Input"

elf1 = []
elf2 = []

def data_collection(file):
    with open(file, 'r') as data:
        for line in data:
            tmp_elf1, tmp_elf2 = line.strip().split(',')
            elf1.append(tmp_elf1)
            elf2.append(tmp_elf2)

def elf_compare(elf1_set, elf2_set):
    i = 0
    overlap = 0

    for i in range(len(elf1_set)):
        toggle = 0
        elf1_begin, elf1_end = elf1_set[i].split("-")
        elf2_begin, elf2_end = elf2_set[i].split("-")
        if int(elf1_begin) >= int(elf2_begin):
            if int(elf1_begin) <= int(elf2_end):
                overlap += 1
                toggle = 1
        if int(elf1_end) >= int(elf2_begin) and toggle == 0:
            if int(elf1_end) <= int(elf2_end):
                overlap += 1
                toggle = 1
        if int(elf2_begin) >= int(elf1_begin) and toggle == 0:
            if int(elf2_begin) <= int(elf1_end):
                overlap += 1
                toggle = 1
        if int(elf2_end) >= int(elf1_begin) and toggle == 0:
            if int(elf2_end) <= int(elf1_end):
                overlap += 1
                toggle = 1
        # if ((int(elf2_begin) >= int(elf1_begin) and int(elf1_begin) <= int(elf2_end)) or (int(elf2_begin) >= int(elf1_end) and int(elf1_end) <= int(elf2_end))):
        #     overlap += 1
        #     toggle = 1
        # if (((int(elf1_begin) >= int(elf2_begin) and int(elf2_begin)  <= int(elf1_end)) or (int(elf1_begin) >= int(elf2_end) and int(elf2_end) <= int(elf1_end))) and toggle == 0):
        i += 1

        print(overlap)

data_collection(filename)
elf_compare(elf1, elf2)
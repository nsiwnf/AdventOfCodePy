registers = [0] * 6
duplicates = list()


def bani_5_456_5():
    registers[5] = registers[5] & 456


def eqri_5_72_5():
    if registers[5] == 72:
        registers[5] = 1
        registers[4] = 4
    else:
        registers[5] = 0
        registers[4] = 3


def seti_0_0_4():
    registers[4] = 0


def seti_0_7_5():
    registers[5] = 0


def bori_5_65536_3():
    registers[3] = registers[5] | 65536


def seti_733884_6_5():
    registers[5] = 733884


def bani_3_255_1():
    registers[1] = registers[3] & 255


def addr_5_1_5():
    registers[5] = registers[5] + registers[1]


def bani_5_16777215_5_1():
    registers[5] = registers[5] & 16777215


def muli_5_65899_5():
    registers[5] = registers[5] * 65899


def bani_5_16777215_5_2():
    registers[5] = registers[5] & 16777215


def gtir_256_3_1():
    if 256 > registers[3]:
        registers[1] = 1
    else:
        registers[1] = 0


def addr_1_4_4_1():
    registers[4] = registers[1] + 14


def addi_4_1_4_1():
    registers[4] = 16


def seti_27_8_4():
    registers[4] = 27


def seti_0_6_1():
    registers[1] = 0


def addi_1_1_2():
    registers[2] = registers[1] + 1


def muli_2_256_2():
    registers[2] = registers[2] * 256


def gtrr_2_3_2():
    if registers[2] > registers[3]:
        registers[2] = 1
    else:
        registers[2] = 0


def addr_2_4_4():
    registers[4] = registers[2] + 21


def addi_4_1_4_2():
    registers[4] = 23


def seti_25_4_4():
    registers[4] = 25


def addi_1_1_1():
    registers[1] = registers[1] + 1


def seti_17_8_4():
    registers[4] = 17


def setr_1_7_3():
    registers[3] = registers[1]


def seti_7_0_4():
    registers[4] = 7


def eqrr_5_0_1():
    if registers[5] == registers[0]:
        registers[1] = 1
        registers[4] = 30
    else:
        registers[1] = 0
        registers[4] = 29
    if registers[5] in duplicates:
        print "Part 2: ", duplicates[len(duplicates) - 1]
        registers[4] = 31
    elif len(duplicates) == 0:
        print "Part 1: ", registers[5]
    duplicates.append(registers[5])
    print registers[5]


def seti_5_9_4():
    registers[4] = 5


def switch(ip):
    switch_cases = {
        # 0: seti_123_0_5,
        1: bani_5_456_5,
        2: eqri_5_72_5,
        # 3: addr_5_4_4,
        4: seti_0_0_4,
        5: seti_0_7_5,
        6: bori_5_65536_3,
        7: seti_733884_6_5,
        8: bani_3_255_1,
        9: addr_5_1_5,
        10: bani_5_16777215_5_1,
        11: muli_5_65899_5,
        12: bani_5_16777215_5_2,
        13: gtir_256_3_1,
        14: addr_1_4_4_1,
        15: addi_4_1_4_1,
        16: seti_27_8_4,
        17: seti_0_6_1,
        18: addi_1_1_2,
        19: muli_2_256_2,
        20: gtrr_2_3_2,
        21: addr_2_4_4,
        22: addi_4_1_4_2,
        23: seti_25_4_4,
        24: addi_1_1_1,
        25: seti_17_8_4,
        26: setr_1_7_3,
        27: seti_7_0_4,
        28: eqrr_5_0_1,
        #29: addr_1_4_4_2,
        30: seti_5_9_4
    }
    if ip > 30:
        return True
    else:
        switch_cases[ip]()
        return False


# Part 1: 2884703
# Part 2: 15400966
halted = False
registers[4] = 1
registers[5] = 123
while not halted:
    halted = switch(registers[4])
    registers[4] += 1

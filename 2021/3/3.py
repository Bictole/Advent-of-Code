def import_data():
    data = open('2021/3/input.txt', 'r')
    lines = data.readlines()
    return lines

############### First Exercise ###############    

def power_consumption(lines):

    gamma_rate = ""
    epsilon_rate = ""

    for i in range(len(lines[0])):
        count_0 = 0
        count_1 = 0
        for j in range(len(lines)):
            if i < len(lines[j]) and lines[j][i] == '0':
                count_0 += 1
            elif i < len(lines[j]) and lines[j][i] == '1':
                count_1 += 1

        if i < len(lines[j]) and count_1 > count_0:
            gamma_rate += '1'
            epsilon_rate += '0'
        elif i < len(lines[j]):
            gamma_rate += '0'
            epsilon_rate += '1'

    gamma_rate_decimal = int(gamma_rate,2)
    epsilon_rate_decimal = int(epsilon_rate,2)

    return epsilon_rate_decimal * gamma_rate_decimal

lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"] 
result = power_consumption(lines)
print ("\nThe Result of the first test is :",result)

lines = import_data()
result = power_consumption(lines)
print ("The Result of the first exercise is :",result)
print()

############### Second Exercise ###############    

def oxygen_generator_rating(lines):

    i = 0

    while len(lines) > 1 and i < len(lines[0]):
        count_0 = 0
        count_1 = 0
        for j in range(len(lines)):
            if i < len(lines[j]) and lines[j][i] == '0':
                count_0 += 1
            elif i < len(lines[j]) and lines[j][i] == '1':
                count_1 += 1

        k = 0
        if i < len(lines[j]) and count_1 >= count_0:
            while k < len(lines):
                if k < len(lines) and i < len(lines[k]) and lines[k][i] == '0':
                    lines.pop(k)
                else :
                    k += 1
        elif i < len(lines[j]):
            while k < len(lines):
                if k < len(lines) and i < len(lines[k]) and lines[k][i] == '1':
                    lines.pop(k)
                else:
                    k += 1
        i += 1
    
    oxygen = lines[0]
    oxygen_decimal = int(oxygen,2)

    return oxygen_decimal

def co2_scrubber_rating(lines):
    
    i = 0

    while len(lines) > 1 and i < len(lines[0]):
        count_0 = 0
        count_1 = 0
        for j in range(len(lines)):
            if i < len(lines[j]) and lines[j][i] == '0':
                count_0 += 1
            elif i < len(lines[j]) and lines[j][i] == '1':
                count_1 += 1

        k = 0
        if i < len(lines[j]) and count_0 > count_1:
            while k < len(lines):
                if k < len(lines) and i < len(lines[k]) and lines[k][i] == '0':
                    lines.pop(k)
                else:
                    k += 1
        elif i < len(lines[j]):
            while k < len(lines):
                if k < len(lines) and i < len(lines[k]) and lines[k][i] == '1':
                    lines.pop(k)
                else:
                    k += 1
        i += 1  

    co2 = lines[0]
    co2_decimal = int(co2,2)

    return co2_decimal

def life_support_rating(lines):
    lines_oxy = lines.copy()
    oxygen = oxygen_generator_rating(lines_oxy)
    co2 = co2_scrubber_rating(lines)

    return oxygen * co2

lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "10000", "11001", "00010", "01010"] 
result = life_support_rating(lines)
print ("\nThe Result of the second test is :",result)

lines = import_data()
result = life_support_rating(lines)
print ("The Result of the second exercise is :",result)
print()
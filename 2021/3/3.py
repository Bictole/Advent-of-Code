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

lines = ["00100", "11110", "10110", "10111", "10101", "01111", "00111", "11100", "11001", "10111", "00010", "01010"] 
result = power_consumption(lines)
print ("\nThe Result of the first test is :",result)

lines = import_data()
result = power_consumption(lines)
print ("The Result of the first exercise is :",result)
print()
def import_data():
    data = open('2021/1/input.txt', 'r')
    lines = data.readlines()
    return lines

############### First Exercise ###############

def count_increase(lines):

    result = 0

    for i in range(len(lines) - 1):
        if int(lines[i]) < int(lines[i + 1]):
            result += 1

    return result

lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] 
result = count_increase(lines)
print ("\nThe Result of the first test is :",result)

lines = import_data()
result = count_increase(lines)
print ("The Result of the first exercise is :",result)
print()

############### Second Exercise ###############

def count_three_increase(lines):

    result = 0

    for i in range(len(lines) - 3):
        first = int(lines[i]) + int(lines[i + 1]) + int(lines[i + 2])
        second = int(lines[i + 1]) + int(lines[i + 2]) + int(lines[i + 3])

        if (first < second):
            result += 1

    return result

lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] 
result = count_three_increase(lines)
print ("\nThe Result of the second test is :",result)

lines = import_data()
result = count_three_increase(lines)
print ("The Result of the second exercise is :",result)
print()
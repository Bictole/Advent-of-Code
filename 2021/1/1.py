def import_data():
    data = open('2021/1/input.txt', 'r')
    lines = data.readlines()
    return lines


def count_increase(lines):

    result = 0

    for i in range(len(lines) - 1):
        if int(lines[i]) < int(lines[i + 1]):
            result += 1

    return result



lines = import_data()
result = count_increase(lines)
print ("The Result is :",result)


lines = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263] 
result = count_increase(lines)
print ("The Result is :",result)
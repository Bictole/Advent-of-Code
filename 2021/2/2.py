def import_data():
    data = open('2021/2/input.txt', 'r')
    lines = data.readlines()
    return lines

############### First Exercise ###############

def get_position(lines):

    horizontal_position = 0
    depth_position = 0

    for i in range(len(lines)):
        move = lines[i].split()
        if move[0][0] == 'f':
            horizontal_position += int(move[1])
        elif move[0][0] == 'u':
            depth_position -= int(move[1])
        else:
            depth_position += int(move[1])

    return horizontal_position * depth_position

lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"] 
result = get_position(lines)
print ("\nThe Result of the first test is :",result)

lines = import_data()
result = get_position(lines)
print ("The Result of the first exercise is :",result)
print()

############### Second Exercise ###############

def get_aim_position(lines):

    horizontal_position = 0
    depth_position = 0
    aim = 0

    for i in range(len(lines)):
        move = lines[i].split()
        if move[0][0] == 'f':
            horizontal_position += int(move[1])
            depth_position += (aim * int(move[1]))
        elif move[0][0] == 'u':
            aim -= int(move[1])
        else:
            aim += int(move[1])

    return horizontal_position * depth_position

lines = ["forward 5", "down 5", "forward 8", "up 3", "down 8", "forward 2"] 
result = get_aim_position(lines)
print ("\nThe Result of the second test is :",result)

lines = import_data()
result = get_aim_position(lines)
print ("The Result of the second exercise is :",result)
print()
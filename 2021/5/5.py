def import_data():
    data = open('2021/5/input.txt', 'r')
    lines = data.readlines()
    return lines

def import_test():
    data = open('2021/5/test.txt', 'r')
    lines = data.readlines()
    return lines

############### First Exercise ###############    

class Vector:
    def __init__(Self, firstx, firsty, secx, secy):
        Self.firstx = firstx
        Self.firsty = firsty
        Self.secondx = secx
        Self.secondy = secy


    def print_vec(Self):
        print(Self.firstx, ",", Self.firsty, "  ", Self.secondx, ",", Self.secondy)

def get_coordinates(lines):
    coordinates = []

    for l in lines:
        splitted = l.split()
        splitted.pop(1)
        first = splitted[0].split(',')
        second = splitted[1].split(',')
        firstx = int(first[0])
        firsty = int(first[1])
        secondx = int(second[0])
        secondy = int(second[1])

        vec = Vector(firstx, firsty, secondx, secondy)
        coordinates.append(vec)


    return coordinates

def overlap(lines):
    coordinates = get_coordinates(lines)

    map = [[0 for i in range(1000)] for j in range(1000)]
    
    for c in coordinates:
        if c.firstx == c.secondx:
            if c.firsty < c.secondy:
                for i in range(c.firsty, c.secondy + 1):
                    map[i][c.firstx] += 1
            else:
                for i in range(c.secondy, c.firsty + 1):
                    map[i][c.firstx] += 1
        elif c.firsty == c.secondy:
            if c.firstx < c.secondx:
                for i in range(c.firstx, c.secondx + 1):
                    map[c.firsty][i] += 1
            else:
                for i in range(c.secondx, c.firstx + 1):
                    map[c.firsty][i] += 1

    result = 0

    for m in map:
        for i in range(len(m)):
            if m[i] > 1:
                result += 1

    return result
    

lines = import_test()
result = overlap(lines)
print ("\nThe Result of the first test is :", result)

lines = import_data()
result = overlap(lines)
print ("The Result of the first exercise is :",result)
print()

############### Second Exercise ###############    

def overlap_diag(lines):
    coordinates = get_coordinates(lines)

    map = [[0 for i in range(1000)] for j in range(1000)]
    
    for c in coordinates:
        if abs(c.firstx - c.secondx) == abs(c.firsty - c.secondy):
            if c.firstx < c.secondx:
                if c.firsty < c.secondy:
                    x = c.firstx
                    y = c.firsty
                    for i in range(c.firstx, c.secondx + 1):
                        map[y][x] += 1
                        x += 1
                        y += 1
                else:
                    x = c.firstx
                    y = c.firsty
                    for i in range(c.firstx, c.secondx + 1):
                        map[y][x] += 1
                        x += 1
                        y -= 1
            else:
                if c.firsty < c.secondy:
                    x = c.firstx
                    y = c.firsty
                    for i in range(c.secondx, c.firstx + 1):
                        map[y][x] += 1
                        x -= 1
                        y += 1
                else:
                    x = c.firstx
                    y = c.firsty
                    for i in range(c.secondx, c.firstx + 1):
                        map[y][x] += 1
                        x -= 1
                        y -= 1
        elif c.firstx == c.secondx:
            if c.firsty < c.secondy:
                for i in range(c.firsty, c.secondy + 1):
                    map[i][c.firstx] += 1
            else:
                for i in range(c.secondy, c.firsty + 1):
                    map[i][c.firstx] += 1
        elif c.firsty == c.secondy:
            if c.firstx < c.secondx:
                for i in range(c.firstx, c.secondx + 1):
                    map[c.firsty][i] += 1
            else:
                for i in range(c.secondx, c.firstx + 1):
                    map[c.firsty][i] += 1

    result = 0

    for m in map:
        for i in range(len(m)):
            if m[i] > 1:
                result += 1

    return result

lines = import_test()
result = overlap_diag(lines)
print ("\nThe Result of the second test is :", result)


lines = import_data()
result = overlap_diag(lines)
print ("The Result of the second exercise is :",result)
print()
def import_data():
    data = open('2021/6/input.txt', 'r')
    lines = data.readlines()
    return lines

def import_test():
    data = open('2021/6/test.txt', 'r')
    lines = data.readlines()
    return lines

############### First Exercise ###############    

def lanternfish(lines):
    fishes = lines[0].split(',')

    for i in range(len(fishes)):
        fishes[i] = int(fishes[i])

    days = 80
    now = 0

    #print("Initial State:", fishes)

    while (now < days):
        for i in range(len(fishes)):
            fishes[i] -= 1

        new_fish = 0
        for i in range(len(fishes)):
            if fishes[i] < 0:
                fishes[i] = 6
                new_fish += 1

        for i in range(new_fish):
            fishes.append(8)
                
        now += 1
        #print("After", now, "days:", fishes)

    return len(fishes)

lines = import_test()
result = lanternfish(lines)
print ("\nThe Result of the first test is :", result)

lines = import_data()
result = lanternfish(lines)
print ("The Result of the first exercise is :",result)
print()
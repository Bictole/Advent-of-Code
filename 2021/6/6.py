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
        new_fish = []
        for i in range(len(fishes)):
            fishes[i] -= 1

            if fishes[i] < 0:
                new_fish.append(8)
                fishes[i] = 6

        fishes = fishes + new_fish
                
        now += 1
        #print("After", now, "days")

    return len(fishes)

lines = import_test()
result = lanternfish(lines)
print ("\nThe Result of the first test is :", result)

lines = import_data()
result = lanternfish(lines)
print ("The Result of the first exercise is :",result)
print()

############### Second Exercise ###############    

from collections import Counter

def fast(lines):
    fishes = lines[0].split(',')

    for i in range(len(fishes)):
        fishes[i] = int(fishes[i])

    lifes = dict(Counter(fishes))

    days = 256
    for day in range(1, days+1):
        lifes = {l: (0 if lifes.get(l+1) is None else lifes.get(l+1)) for l in range(-1, 8)}
        
        # make all 8s -1 because we create new fish with 8 after it reaches 0
        lifes[8] = lifes[-1]
        
        # add new lifes to that are exhausted
        lifes[6] += lifes[-1]
        
        # reset exhausted lifes
        lifes[-1] = 0 

    return sum(lifes.values())

lines = import_test()
result = fast(lines)
print ("\nThe Result of the second test is :", result)

lines = import_data()
result = fast(lines)
print ("The Result of the second exercise is :",result)
print()
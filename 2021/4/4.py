def import_data():
    data = open('2021/4/input.txt', 'r')
    lines = data.readlines()
    return lines

def import_test():
    data = open('2021/4/test.txt', 'r')
    lines = data.readlines()
    return lines

############### First Exercise ###############    

def get_numbers(first_line):
    for i in range(len(first_line)):
        first_line[i] = int(first_line[i])

    return first_line

def get_boards(lines):
    all_boards = []
    board = []
    for i in range(2, len(lines)):
        if (lines[i] == '\n'):
            all_boards.append(board)
            board = []
        else:
            current_line = lines[i].split()
            for j in range(len(current_line)):
                current_line[j] = int(current_line[j])
            current_bool = []
            for k in range(len(current_line)):
                current_bool.append((current_line[k], False))
            board.append(current_bool)
    
    all_boards.append(board)
    return all_boards

def print_all(boards):
    print("--------------------------------------")
    for r in boards:
        for i in range(5):
            print(r[i])
        print()
    print("--------------------------------------")

def bingo(lines):
    numbers = get_numbers(lines[0].split(','))
    all_boards = get_boards(lines)
    #print_all(all_boards)

    win = False
    final_board = []
    number = 0

    count = 0
    while not win and count < len(numbers):
        number = numbers[count]
        for board in all_boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if (board[i][j][0] == number):
                        board[i][j] = (number, True)

        for board in all_boards:
            win_row = True
            for i in range(len(board)):
                win_row = True
                for j in range(len(board[i])):
                    if (not board[i][j][1]):
                        win_row = False
                        break
                if win_row:
                    break

            win_col = True
            for i in range(len(board)):
                win_col = True
                for j in range(len(board[i])):
                    if (not board[j][i][1]):
                        win_col = False
                        break
                if win_col:
                    break

            if win_row or win_col:
                win = True
                final_board = board
                break
        
        count += 1
    
    sum = 0

    for i in range(len(final_board)):
        for j in range(len(final_board[i])):
            if not final_board[i][j][1]:
                sum += final_board[i][j][0]

    return sum * number

lines = import_test()
result = bingo(lines)
print ("\nThe Result of the first test is :", result)

lines = import_data()
result = bingo(lines)
print ("The Result of the first exercise is :",result)
print()

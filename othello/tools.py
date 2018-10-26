def board (x,y):
    board = list(list(list()for j in range(x))for i in range(y))
    return board

def arrange (name):
    for count1 in range (len(name)):
        print(name[count1],'\n'*2)
    print('='*200)


def binput (boa):
    board = boa
    for count1 in range(len(board)):
        line = input(str(count1+1)+'行目')

        for count2 in range (len(board[count1])):
            board[count1][count2] = [line[count2]]

    return board

def boardef (boa,li):
    board = boa
    line = str(li)
    for count1 in range(len(board)):
        board[count1] = [line[count1]]

    return board

def printa (arg):
    print(arg,'\n')

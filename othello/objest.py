from tools import arrange


def board ():
    board = [[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],
             [['-'],['-'],['-'],['1'],['0'],['-'],['-'],['-']],[['-'],['-'],['-'],['0'],['1'],['-'],['-'],['-']],[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],
             [['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']],[['-'],['-'],['-'],['-'],['-'],['-'],['-'],['-']]]
    return (board)

#--------------------------------------------------------------------------------------自作関数：オセロボードの定義-----------------------------------------------------------------------------------------------------


def mark (boa):
    board = boa
    for count1 in range(8):
        for count2 in range(8):
            if board[count1][count2] == ['pt'] or board[count1][count2] == ['＃']:
                board[count1][count2] = ['＃']
            elif board[count1][count2] == ['0'] or board[count1][count2] == ['〇'] or  board[count1][count2] == ['00']:
                board[count1][count2] =['〇']
            elif board[count1][count2] ==['1'] or board[count1][count2] == ['●'] or board[count1][count2] ==['11']:
                board[count1][count2] = ['●']
            elif board[count1][count2] == ['-']:
                board[count1][count2] = ['  ']

    return (board)

#------------------------------------------------------------------------------------------自作関数：白黒のマークアップ----------------------------------------------------------------------------------------------------------

def put (boa,x,y,color):
    board = boa
    if color == 'b':
        board[y][x] = ['11']
    elif color == 'w':
        board[y][x] = ['00']

    return (board)

#-----------------------------------------------------------------------------------------------自作関数：駒を置く------------------------------------------------------------------------------------------------------

def tellb (boa):
    board = boa
    for count1 in range(8):
        for count2 in range(8):
            if board[count1][count2] == ['1'] or board[count1][count2] == ['●']:
                if count1 >= 2:
                    if board[count1-1][count2] == ['〇'] or board[count1-1][count2] == ['0']: 
                        if board[count1-2][count2] == ['　'] or board[count1-2][count2] == ['-']:
                            board [count1-2][count2] = ['pt']
                if count1 <= 5:
                    if board[count1+1][count2] == ['〇'] or board[count1+1][count2] == ['0']:
                        if board[count1+2][count2] == ['　'] or board[count1+2][count2] == ['-']:
                            board [count1+2][count2] = ['pt']
                if count2 >= 2:
                    if  board[count1][count2-1] == ['〇'] or board[count1][count2-1] == ['0']:
                        if board[count1][count2-2] == ['　'] or board[count1][count2-2] == ['-']:
                            board [count1][count2-2] = ['pt']
                if count2 <= 5:
                    if board[count1][count2+1] == ['〇'] or board[count1][count2+1] == ['0']:
                        if board[count1][count2+2] == ['　'] or board[count1][count2+2] == ['-']:
                            board [count1][count2+2] = ['pt']
                
    return board

#--------------------------------------------------------------------------------------------自作関数：打点可能セル----------------------------------------------------------------------------------------------------

def action (boa):
    board = boa
    for count1 in range (8):
        for count2 in range (8):
            if board[count1][count2] == ['11']:
                for count3 in range (1,count1):
                    if board[count1-count3][count2] == ['0'] or  board[count1-count3][count2] == ['〇']:
                        if board[count1-count3-1][count2] == ['1'] or board[count1-count3-1][count2] == ['●']:
                            for count4 in range (1,count3+1):
                                board[count1-count4][count2] = ['1']
                        continue
                    else:
                        continue

                for count3 in range (1,count2):
                    if board[count1][count2-count3] == ['0'] or  board[count1][count2-count3] == ['〇']:
                        if board[count1][count2-count3-1] == ['1'] or board[count1][count2-count3-1] == ['●']:
                            for count4 in range (1,count3+1):
                                board[count1][count2-count4] = ['1']
                        continue
                    else:
                        continue

                for count3 in range (1,7-count1):
                    if board[count1+count3][count2] == ['0'] or  board[count1+count3][count2] == ['〇']:
                        if board[count1+count3+1][count2] == ['1'] or board[count1+count3+1][count2] == ['●']:
                            for count4 in range (1,count3+1):
                                board[count1+count4][count2] = ['1']
                        continue
                    else:
                        continue

                for count3 in range (1,7-count2):
                    if board[count1][count2+count3] == ['0'] or  board[count1][count2+count3] == ['〇']:
                        if board[count1][count2+count3+1] == ['1'] or board[count1][count2+count3+1] == ['●']:
                            for count4 in range (1,count3+1):
                                board[count1][count2+count4] = ['1']
                        continue
                    else:
                        continue

                for count3 in range (1,7-count1):
                    for count5 in range (1,7-count2):
                        if board[count1+count3][count2+count5] == ['0'] or  board[count1+count3][count2+count5] == ['〇']:
                            if board[count1+count3+1][count2+count5+1] == ['1'] or board[count1+count3+1][count2+count5+1] == ['●']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1+count4][count2+count6] = ['1']
                            continue
                        else:
                            continue

                for count3 in range (1,count1):
                    for count5 in range (1,count2):
                        if board[count1-count3][count2-count5] == ['0'] or  board[count1-count3][count2-count5] == ['〇']:
                            if board[count1-count3-1][count2-count5-1] == ['1'] or board[count1-count3-1][count2-count5-1] == ['●']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1-count4][count2-count6] = ['1']
                            continue
                        else:
                            continue

                for count3 in range (1,count1):
                    for count5 in range (1,7-count2):
                        if board[count1-count3][count2+count5] == ['0'] or  board[count1-count3][count2+count5] == ['〇']:
                            if board[count1-count3-1][count2+count5+1] == ['1'] or board[count1-count3-1][count2+count5+1] == ['●']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1-count4][count2+count6] = ['1']
                            continue
                        else:
                            continue

                for count3 in range (1,7-count1):
                    for count5 in range (1,count2):
                        if board[count1+count3][count2-count5] == ['0'] or  board[count1+count3][count2-count5] == ['〇']:
                            if board[count1+count3+1][count2-count5-1] == ['1'] or board[count1+count3+1][count2-count5-1] == ['●']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1+count4][count2-count6] = ['1']
                            continue
                        else:
                            continue
                


            elif board[count1][count2] == ['00']:
                for count3 in range (1,count1):
                    if board[count1-count3][count2] == ['1'] or  board[count1-count3][count2] == ['●']:
                        if board[count1-count3-1][count2] == ['0'] or board[count1-count3-1][count2] == ['〇']:
                            for count4 in range (1,count3+1):
                                board[count1-count4][count2] = ['0']
                        continue
                    else:
                        continue

                for count3 in range (1,count2):
                    if board[count1][count2-count3] == ['1'] or  board[count1][count2-count3] == ['●']:
                        if board[count1][count2-count3-1] == ['0'] or board[count1][count2-count3-1] == ['〇']:
                            for count4 in range (1,count3+1):
                                board[count1][count2-count4] = ['0']
                        continue
                    else:
                        continue

                for count3 in range (1,7-count1):
                    if board[count1+count3][count2] == ['1'] or  board[count1+count3][count2] == ['●']:
                        if board[count1+count3+1][count2] == ['0'] or board[count1+count3+1][count2] == ['〇']:
                            for count4 in range (1,count3+1):
                                board[count1+count4][count2] = ['0']
                        continue
                    else:
                        continue

                for count3 in range (1,7-count2):
                    if board[count1][count2+count3] == ['1'] or  board[count1][count2+count3] == ['●']:
                        if board[count1][count2+count3+1] == ['0'] or board[count1][count2+count3+1] == ['〇']:
                            for count4 in range (1,count3+1):
                                board[count1][count2+count4] = ['0']
                        continue
                    else:
                        continue

                for count3 in range (1,7-count1):
                    for count5 in range (1,7-count2):
                        if board[count1+count3][count2+count5] == ['1'] or  board[count1+count3][count2+count5] == ['●']:
                            if board[count1+count3+1][count2+count5+1] == ['0'] or board[count1+count3+1][count2+count5+1] == ['〇']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1+count4][count2+count6] = ['0']
                            continue
                        else:
                            continue

                for count3 in range (1,count1):
                    for count5 in range (1,count2):
                        if board[count1-count3][count2-count5] == ['1'] or  board[count1-count3][count2-count5] == ['●']:
                            if board[count1-count3-1][count2-count5-1] == ['0'] or board[count1-count3-1][count2-count5-1] == ['〇']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1-count4][count2-count6] = ['0']
                            continue
                        else:
                            continue

                for count3 in range (1,count1):
                    for count5 in range (1,7-count2):
                        if board[count1-count3][count2+count5] == ['1'] or  board[count1-count3][count2+count5] == ['●']:
                            if board[count1-count3-1][count2+count5+1] == ['0'] or board[count1-count3-1][count2+count5+1] == ['〇']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1-count4][count2+count6] = ['0']
                            continue
                        else:
                            continue

                for count3 in range (1,7-count1):
                    for count5 in range (1,count2):
                        if board[count1+count3][count2-count5] == ['1'] or  board[count1+count3][count2-count5] == ['●']:
                            if board[count1+count3+1][count2-count5-1] == ['0'] or board[count1+count3+1][count2-count5-1] == ['〇']:
                                for count4 in range (1,count3+1):
                                    for count6 in range(1,count5+1):
                                        board[count1+count4][count2-count6] = ['0']
                            continue
                        else:
                            continue
                

    return board
#---------------------------------------------------------------------------------------------自作関数：白黒の反転------------------------------------------------------------------------------------------------------





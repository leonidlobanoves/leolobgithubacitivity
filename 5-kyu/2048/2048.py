from preloaded import UP, LEFT, DOWN, RIGHT
# from preloaded import TFE   # TFE.UP, TFE.LEFT, ...
​
def update_board(board, direction):
    
    if direction in (0, 2):
        board = [list(x) for x in zip(*board)]
        
    for num, i in enumerate(board):
        if direction in (1, 0):
            board[num] = merge_lines(i)
        else:
            res = i[::-1]
            board[num] = merge_lines(res)[::-1]
​
    
    if direction in (0, 2):
        board = [list(x) for x in zip(*board)]
​
    return board
​
def merge_lines(x):
    l = [i for i in x if i != 0]
    final_l = []
    el = 0
    while el < len(l):
        if el+1 < len(l) and l[el] == l[el+ 1]:
            final_l.append(l[el] + l[el+ 1])
            el+=2
        else:
            final_l.append(l[el])
            el += 1  
    final_l.extend([0 for _ in range(len(x)- len(final_l))])
    return final_l
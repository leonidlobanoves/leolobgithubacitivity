def attacked_squares(board):
    new_board = [['  '] * 8 for _ in range(8)]
    figure = 'W'
    
    directions = {
        'r': [[1, 0],[0, 1],[-1, 0], [0, -1]],
        'b': [[1, 1],[1, -1],[-1, 1], [-1, -1]],
        'q': [[1, 1],[1, -1],[-1, 1], [-1, -1], [1, 0],[0, 1],[-1, 0], [0, -1]],
        'k': [[1, 1],[1, -1],[-1, 1], [-1, -1], [1, 0],[0, 1],[-1, 0], [0, -1]],
        'n': [(2, 1),(1, 2),(-2, 1), (2, -1), (-2, -1), (-1, 2), (1, -2), (-1, -2)],
        'p': [[-1, 1], [-1, -1], [1, 1], [1, -1]]
    }
    
    for num, line in enumerate(board):
        for ind, square in enumerate(line):
            if square.isupper():
                figure = 'W'
            elif square.islower():
                figure = "B"
            else:
                figure = " "
                        
            
            for k, v in directions.items():
                if square.lower() == k:
                    for el in v:
                        stablenum = num
                        stableind = ind
                        stopnext = False
                        while -1 < num + el[0] < 8 and -1 < ind + el[1] < 8:
                            if stopnext:
                                break
                            if board[num+el[0]][ind+el[1]] != ' ' or k in ('k', 'n', 'p'):
                                stopnext = True
​
​
                            if figure == "W":
                                if not (k == 'p' and el[0] > 0):
                                    new_board[num + el[0]][ind + el[1]] = figure + new_board[num + el[0]][ind + el[1]][1]
​
                            if figure == "B":
                                if not (k == 'p' and el[0] < 0):
                                    new_board[num + el[0]][ind + el[1]] = new_board[num + el[0]][ind + el[1]][0] + figure
​
                            num+=el[0]
                            ind +=el[1]
                                
                        num = stablenum
                        ind = stableind
                
    return new_board
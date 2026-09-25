                    stableind = ind
                    stopnext = False
                    while -1 < num + a[0] < 8 and -1 < ind + a[1] < 8:
                        if stopnext:
                            break
                        if board[num+a[0]][ind+a[1]] != ' ':
                            stopnext = True
                        
                        if figure == "W":
                            new_board[num + a[0]][ind + a[1]] = figure + new_board[num + a[0]][ind + a[1]][1]
        
                        if figure == "B":
                            new_board[num + a[0]][ind + a[1]] = new_board[num + a[0]][ind + a[1]][0] + figure
                            
                        num+=a[0]
                        ind +=a[1]
                    num = stablenum
                    ind = stableind
                
            if square.lower() == 'k':
                attack_var = [[1, 1],[1, -1],[-1, 1], [-1, -1], [1, 0],[0, 1],[-1, 0], [0, -1]]
                for a in attack_var:
                    stablenum = num
                    stableind = ind
                    stopnext = False
                    while -1 < num + a[0] < 8 and -1 < ind + a[1] < 8:
                        if stopnext:
                            break
                        if board[num+a[0]][ind+a[1]] != ' ':
                            stopnext = True
                        
                        if figure == "W":
                            new_board[num + a[0]][ind + a[1]] = figure + new_board[num + a[0]][ind + a[1]][1]
        
                        if figure == "B":
                            new_board[num + a[0]][ind + a[1]] = new_board[num + a[0]][ind + a[1]][0] + figure
                            
                        num+=a[0]
                        ind +=a[1]
                        stopnext = True
                    num = stablenum
                    ind = stableind
                    
                    
                
    return new_board
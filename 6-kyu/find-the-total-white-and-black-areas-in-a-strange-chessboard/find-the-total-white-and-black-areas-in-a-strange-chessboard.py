def white_black_areas(cs, rs):
    c_even, c_odd = sum(cs[0::2]), sum(cs[1::2])
    r_even, r_odd = sum(rs[0::2]), sum(rs[1::2])
​
    white = c_even * r_even + c_odd * r_odd
    black = c_even * r_odd + c_odd * r_even
            
            
    return (white, black)
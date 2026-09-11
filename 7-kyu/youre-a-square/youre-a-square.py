import math
​
def is_square(n):   
    if n >= 0 and str(math.sqrt(n)).split(".")[-1] == "0":
        return True
    else:
        return False
​
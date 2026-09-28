import math
def prime(n):
    res = []
    for i in range(2, n+ 1):
        counter = False
        for k in range(2, int(math.sqrt(i))+ 1):  
            if i % k == 0:
                counter = True
                break
        if counter == False:
            res.append(i)
​
        
​
    return res
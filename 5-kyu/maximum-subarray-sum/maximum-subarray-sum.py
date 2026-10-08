def max_sequence(arr):
    smum = 0
    summa_kuska = 0
    for x in arr:
        summa_kuska +=x
        if summa_kuska > smum:
            smum = summa_kuska
        elif summa_kuska < 0:
            summa_kuska = 0
            
    
    return smum
​
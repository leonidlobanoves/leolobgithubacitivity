def identify_bb(bearings, weigh):
    basket = []
    for i, box in enumerate(bearings):
        basket.extend([box] * i)
    
    total_weight = weigh(*basket)
​
    return bearings[total_weight - len(basket) * 10]
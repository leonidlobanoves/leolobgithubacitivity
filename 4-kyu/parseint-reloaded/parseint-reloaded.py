        '0': ["ze"],
        "1": ["on"],
        "2": ["tw"],
        "3": ["th"],
        "4": ["fo"],
        "5": ["fi"],
        "6": ["si"],
        "7": ["se"],
        "8": ["ei"],
        "9": ["ni"],
        "10": ["te"],
        "11": ["el"],
        '100': ['hundred'],
        '1000': ['thous'],
        '1000000': ['million']
    }
    counter = 0
    sristring = string.replace("-", " ").replace("and", '').split(" ")
    mutliplier = 1
    final_string = []
    medium_string = []
    for el, i in enumerate(sristring, start=1):
        for key, value in numbers.items():
            if i in numbers[key]:
                old_multiplier = mutliplier
                mutliplier = int(key)
                if old_multiplier == 1 or mutliplier < old_multiplier:
                    counter += (int("".join(medium_string)) * mutliplier)
                else:
                    counter = counter * mutliplier
                    counter += (int("".join(medium_string)) * mutliplier)  if medium_string != [] else 0
                medium_string = []
            elif i[:2] in numbers[key] and i not in ['thous']:
                if i.endswith("teen") or i.endswith("lve"):
                    key = '1' + key
                elif i.endswith("ty") and el == len(sristring):
                    key = key + '0'
                
                final_string.append(key)
                medium_string.append(key)
​
    counter += int("".join(medium_string)) if medium_string != [] else 0
    print(counter)
    return counter
​
​
​
​
​
​
​
​
def top_3_words(text):
    text = text.replace(',', ' ').replace(';', ' ').replace('.', ' ').replace(':', ' ').replace('/', ' ').replace('_', ' ').replace("!", " ").replace("?", " ").replace("-", " ").lower()
    ser = set(text.split(' '))
    ser.discard('')
    result = []
    counter1 = {'': 0}
    counter2 = {'': 0}
    counter3 = {'': 0}
    text = text.split(' ')
    for i in ser:
        k = text.count(i.lower())
        if text.count(i.lower()) >= list(counter1.values())[0]:
            counter3 = counter2.copy()
            counter2 = counter1.copy()
            counter1.pop(list(counter1.keys())[0])
            counter1[i] = text.count(i)
            
        elif text.count(i.lower()) <= list(counter1.values())[0] and text.count(i.lower()) >= list(counter2.values())[0]:
            counter3 = counter2.copy()
            counter2.pop(list(counter2.keys())[0])
            counter2[i] = text.count(i)
            
        elif text.count(i.lower()) <= list(counter2.values())[0] and text.count(i.lower()) >= list(counter3.values())[0]:
            counter3.pop(list(counter3.keys())[0])
            counter3[i] = text.count(i)
    counter1.update(counter2)
    counter1.update(counter3)
    return [k for k,v in counter1.items() if k != '' and set(list(k)) != {"'"}]
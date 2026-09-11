class RomanNumerals:
    rome_signs = {"M":  1000,
   "CM"   :   900 ,
    "D"   :   500 ,
   "CD"   :   400 ,
    "C"   :   100 ,
   "XC"   :    90 ,
    "L"   :    50 ,
   "XL"   :    40 ,
    "X"   :    10 ,
   "IX"   :     9 ,
    "V"   :     5 ,
   "IV"   :     4 ,
    "I"   :     1}
    
    @staticmethod
    def to_roman(val : int) -> str:
        romnum = RomanNumerals()
        rome_line = []
​
        while val != 0:
            for k, v in romnum.rome_signs.items():
                if v <= val:
                    val -= v
                    rome_line.append(k)
                    break
                else:
                    continue
        return ''.join(rome_line)
​
    @staticmethod
    def from_roman(val : str) -> int:
        romnum = RomanNumerals()
        arab_num = 0
​
        while val != "":
            for k, v in romnum.rome_signs.items():
                if val.startswith(k):
                    val = val.replace(k, "", 1)
                    arab_num += v
                    break
​
        return arab_num
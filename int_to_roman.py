class SolutionIntToRoman:
    def intToRoman(self, num: int) -> str:
        dict_roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I"
        }
        list_roman = []

        for int_num, roman in dict_roman.items():
            while num >= int_num:
                num = num - int_num
                list_roman.append(roman)
        
        return "".join(list_roman)
        
        
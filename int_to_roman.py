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

        for int_num, roman in dict_roman.items(): #percorrer os itens do dict
            while num >= int_num: #enquanto o numero que foi mandando for maior que o numero do dict vai rodar a condição
                num = num - int_num # retirar o valor que virou romano
                list_roman.append(roman) # adiciona a lista o valor romano
        
        return "".join(list_roman) #retorma uma lista com valor convertido
        
        
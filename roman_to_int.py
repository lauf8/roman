class SolutionRomanToInt:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'V': 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        lis_s = list(s)
        tam = len(lis_s) - 1
        list_resul = []
        for x in lis_s:
            for chave, valor in dic.items():
                if chave == x:
                    list_resul.append(valor)
                    continue

        for i in range(tam):
            if i == tam:
                continue
            if list_resul[i] < list_resul[i+1]:
                list_resul[i] = list_resul[i] * -1
        return sum(list_resul)
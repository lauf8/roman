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
        for x in lis_s:# for para percorrer os valores romanos que foram mandados
            for chave, valor in dic.items(): #for para percorrer os itens do dicionário
                if chave == x: #vefica se a chave é igual
                    list_resul.append(valor) # achando a chave adicona o valor a list_resul
                    continue #skipa a linha e vai para o proximo algarismo

        for i in range(tam): #for para fazer as subtrações
            if i == tam: # ignora o ultimo elemento já que ele nunca vai ser subtraido
                continue
            if list_resul[i] < list_resul[i+1]: #faz a verificação se vai acontecer a subtração
                list_resul[i] = list_resul[i] * -1
        return sum(list_resul)
class Ordenator:
    def __init__(self):
        pass
    
    def selecao(self, v, chave):
        cont=0
        for i in range(0, len(v)-1):
            cont+=1
            min_index = i
            for j in range(i + 1, len(v)):
                cont+=1
                if v[j].compara(v[min_index], chave) < 0:
                    min_index = j
                    cont+=1
            x = v[min_index]
            v[min_index] = v[i]
            v[i] = x
            cont+=3
        return cont
    
    def insercao(self, v, chave):
        cont=0
        for i in range(1, len(v)):
            cont+=1
            for j in range(i, 0, -1):
                cont+=1
                if v[j].compara(v[j - 1], chave) < 0:
                    aux = v[j]
                    v[j] = v[j - 1]
                    v[j - 1] = aux
                    cont+=3
        return cont
    


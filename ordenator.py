class Ordenator:
    def __init__(self):
        pass
    
    def selecao(self, v, chave):
        for i in range(0, len(v)-1):
            min_index = i
            for j in range(i + 1, len(v)):
                if v[j].compara(v[min_index], chave) < 0:
                    min_index = j
            x = v[min_index]
            v[min_index] = v[i]
            v[i] = x
        return v
    
    def insercao(self, v, chave):
        for i in range(1, len(v)):
            for j in range(i, 0, -1):
                if v[j].compara(v[j - 1], chave) < 0:
                    aux = v[j]
                    v[j] = v[j - 1]
                    v[j - 1] = aux
        return v
    


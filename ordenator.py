class Ordenator:
    def __init__(self):
        pass
    
    def selecao(self, v, n):
        for i in range(1, n):
            min_index = i
            for j in range(i + 1, n + 1):
                if v[j].compara(v[min_index]) < 0:
                    min_index = j
            x = v[min_index]
            v[min_index] = v[i]
            v[i] = x

        print(v[0].dados_da_musica['track_name'])
        return v
        
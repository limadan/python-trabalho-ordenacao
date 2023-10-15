vetor = ['brena', 'ralf', 'hudson', 'loyane', 'xainer']

def selecao(v):
        for i in range(0, len(v)-1):
            min_index = i
            for j in range(i + 1, len(v)):
                if v[j] < v[min_index]:
                    min_index = j
            x = v[min_index]
            v[min_index] = v[i]
            v[i] = x
        return v
    
def insercao(v):
    for i in range(1, len(v)):
        for j in range(i, 0, -1):
            if v[j] < v[j - 1]:
                aux = v[j]
                v[j] = v[j - 1]
                v[j - 1] = aux
    return v

vetor_insertion = insercao(vetor)
vetor_selecao = selecao(vetor)

print("Insertion Sort:", vetor_insertion)
print("Selection sort:", vetor_selecao)
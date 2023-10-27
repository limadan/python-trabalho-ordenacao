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
    
    def shell_sort(self, v, chave):
        cont=0
        salto = 1
        salto = salto * 2 + 1
        while(salto < len(v)):
             salto = salto * 2 + 1
        salto//=2
        while salto!=1:
            for i in range(salto, len(v)):
                cont+=1
                for j in range(i, 0, -salto):
                    cont+=1
                    if v[j].compara(v[j - salto], chave) < 0:
                        aux = v[j]
                        v[j] = v[j - salto]
                        v[j - salto] = aux
                        cont+=3
            salto//=2
        cont_insercao = self.insercao(v, chave)

        return cont + cont_insercao

    def bubble_sort(self, v, chave):
        cont=0
        for i in range(len(v)):
            cont+=1
            for j in range(i, len(v), 1):
                cont+=1
                if v[j].compara(v[i], chave) < 0:
                    aux = v[j]
                    v[j] = v[i]
                    v[i] = aux
                    cont=+3
        return cont

    def quick_sort(self, v, index_esquerda, index_direita, chave):
        i = index_esquerda
        j = index_direita
        pivo = ((index_direita - index_esquerda )//2) + index_esquerda
        
        
        while i<=j:
            if(v[i].compara(v[pivo], chave) < 0 
                and 
                v[j].compara(v[pivo], chave) > 0):
                i+=1
                j-=1
            elif((v[i].compara(v[pivo], chave) < 0 
                    and 
                    v[j].compara(v[pivo], chave) < 0)):
                i+=1
            elif((v[i].compara(v[pivo], chave) > 0 
                    and 
                    v[j].compara(v[pivo], chave) > 0)):
                j-=1
            else:
                aux = v[i]
                v[i] = v[j]
                v[j] = aux
                i+=1
                j-=1
        
        if(index_direita - index_esquerda + 1 > 3):
            self.quick_sort(v, index_esquerda, j, chave)
            self.quick_sort(v, i, index_direita, chave)
        
        pass

    def heap_sort(self, v, chave):
        pass

    def merge_sort(self, v, chave):
        pass


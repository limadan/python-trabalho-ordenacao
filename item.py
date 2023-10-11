class Item:
    def __init__(self, hash_de_musica):
        self.dados_da_musica = hash_de_musica


    def compara(self, other):
        self_musica = self.dados_da_musica['track_name']
        other_musica = other.dados_da_musica['track_name']
        if(self_musica==other_musica):
            return 0
        for i in range(len(self_musica)):
            if(i==len(other_musica)):
                return 1
            elif self_musica[i]<other_musica[i]:
                return -1
            elif self_musica[i]>other_musica[i]:
                return 1
            elif self_musica[i]==other_musica[i]:
                continue
        return 0

        
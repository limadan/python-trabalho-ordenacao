class Item:
    def __init__(self, hash_de_musica):
        self.dados_da_musica = hash_de_musica


    def compara(self, other):
        string1 = self.dados_da_musica['track_name'].lower()
        string2 = other.dados_da_musica['track_name'].lower()

        if string1 < string2:
            return -1
        elif string2 < string1:
            return 1
        else:
            return 0

        
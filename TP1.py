from item import Item
from ordenator import Ordenator


arquivo = open("spotify-2023.csv", encoding='latin-1')
chaves = arquivo.readline().split(",")
hash_de_musica = {}
Musicas = []
for linha in arquivo:
    tem_mais_de_um_artista = False
    if '"' in linha:
        artistas = linha.split('"')[1]
        linha = linha.replace(artistas, "")
        tem_mais_de_um_artista = True
    dados_da_musica = linha.split(",")
    
    hash_de_musica = {}

    for i in range(24):
        if chaves[i] == "artist(s)_name" and tem_mais_de_um_artista:
            hash_de_musica[chaves[i]] = artistas
            continue
        hash_de_musica[chaves[i]] = dados_da_musica[i].replace('"', '')
    itemArray = Item(hash_de_musica)
    Musicas.append(itemArray)

ordenator = Ordenator()
Musicas = ordenator.selecao(Musicas, len(Musicas)-1)

print(list(x))

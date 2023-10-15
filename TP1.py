from item import Item
from ordenator import Ordenator

def split_dados(linha):
    contador_aspas = 0
    string_dado = ''
    vetor_dados = []

    for i in range(len(linha)):
        if(linha[i]=='"' and contador_aspas==0):
            contador_aspas+=1
        elif(linha[i]=='"' and contador_aspas==1):
            contador_aspas-=1
        elif(linha[i]=="," and contador_aspas==0):
            vetor_dados.append(string_dado)
            string_dado=''
        else:
            string_dado+=linha[i]
    
    return vetor_dados
    

arquivo = open("spotify-2023.csv", encoding='latin-1')
chaves = arquivo.readline().split(",")
hash_de_musica = {}
musicas_desordenadas = []
for linha in arquivo:
    dados_da_musica = split_dados(linha)
    hash_de_musica = {}

    for i in range(23):
        hash_de_musica[chaves[i]] = dados_da_musica[i].replace('"', '')
    itemArray = Item(hash_de_musica)
    musicas_desordenadas.append(itemArray)

ordenator = Ordenator()

musicas_selection_sort_track_name = ordenator.selecao(musicas_desordenadas, 'track_name')
musicas_insertion_sort_track_name = ordenator.insercao(musicas_desordenadas, 'track_name')

musicas_selection_sort_artist_name = ordenator.selecao(musicas_desordenadas, 'artist(s)_name')
musicas_insertion_sort_artist_name = ordenator.insercao(musicas_desordenadas, 'artist(s)_name')

string_ordenado = ""
for i in range(10):
    string_ordenado += musicas_selection_sort_track_name[i].dados_da_musica['track_name']
    string_ordenado+=","

print(string_ordenado)


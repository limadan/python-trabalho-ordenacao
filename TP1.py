from item import Item
from ordenator import Ordenator
import time

def print_elementos(numero_elementos, chave):
    for i in range(numero_elementos):
        print(vetor_musicas[i].dados_da_musica[chave])

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
vetor_musicas = []
for linha in arquivo:
    dados_da_musica = split_dados(linha)
    hash_de_musica = {}

    for i in range(23):
        hash_de_musica[chaves[i]] = dados_da_musica[i].replace('"', '')
    itemArray = Item(hash_de_musica)
    vetor_musicas.append(itemArray)


ordenator = Ordenator()
print("=========Algoritmos de Ordenação==========")
print("Qual opcao voce deseja ordenar?")
print("1 - Nome da musica por seleção")
print("2 - Nome da musica por inserção")
print("3 - Nome do artista por seleção")
print("4 - Nome do artista por inserção")
opcao = int(input("Digite a Opção: "))

start_time = time.time()
numero_operacoes = 0
rotulo_txt = ""
if(opcao==1):
    rotulo_txt = "Nome da musica por seleção"
    numero_operacoes = ordenator.selecao(vetor_musicas, 'track_name')
    print_elementos(len(vetor_musicas),'track_name')
elif(opcao==2):
    rotulo_txt = "Nome da musica por inserção"
    numero_operacoes = ordenator.insercao(vetor_musicas, 'track_name')
    print_elementos(len(vetor_musicas),'track_name')
elif(opcao==3):
    rotulo_txt = "Nome do artista por seleção"
    numero_operacoes = ordenator.selecao(vetor_musicas, 'artist(s)_name')
    print_elementos(len(vetor_musicas),'artist(s)_name')
elif(opcao==4):
    rotulo_txt = "Nome do artista por inserção"
    numero_operacoes = ordenator.insercao(vetor_musicas, 'artist(s)_name')
    print_elementos(len(vetor_musicas),'artist(s)_name')
else:
    print("Entrada não identificada")
end_time = time.time()
tempo_corrido = end_time - start_time

arquivo_saida = "tempo_execucao.txt"

with open(arquivo_saida, "a") as arquivo:
    arquivo.write(f"{rotulo_txt}\nTempo de execução do programa: {tempo_corrido} segundos\nNúmero de operações: {numero_operacoes}\n\n")

print(f"{rotulo_txt}\nTempo de execução do programa: {tempo_corrido} segundos\nNúmero de operações: {numero_operacoes}")
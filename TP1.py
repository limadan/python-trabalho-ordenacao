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
print("3 - Nome da musica por bolha")
print("4 - Nome da musica por shell sort")
print("5 - Nome da musica por quick sort")
print("6 - Nome da musica por heap sort")
print("7 - Nome da musica por merge sort")
print("8 - Nome do artista por seleção")
print("9 - Nome do artista por inserção")
print("10 - Nome do artista por bolha")
print("11 - Nome do artista por shell sort")
print("12 - Nome do artista por quick sort")
print("13 - Nome do artista por heap sort")
print("14 - Nome do artista por merge sort")
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
    rotulo_txt = "Nome da musica por bolha"
    numero_operacoes = ordenator.bubble_sort(vetor_musicas, 'track_name')
    print_elementos(len(vetor_musicas),'track_name')
    pass
elif(opcao==4):
    rotulo_txt = "Nome da musica por shell"
    numero_operacoes = ordenator.shell_sort(vetor_musicas, 'track_name')
    print_elementos(len(vetor_musicas),'track_name')
    pass
elif(opcao==5):
    pass
elif(opcao==6):
    pass
elif(opcao==7):
    pass
elif(opcao==8):
    rotulo_txt = "Nome do artista por seleção"
    numero_operacoes = ordenator.selecao(vetor_musicas, 'artist(s)_name')
    print_elementos(len(vetor_musicas),'artist(s)_name')
    pass
elif(opcao==9):
    rotulo_txt = "Nome do artista por inserção"
    numero_operacoes = ordenator.insercao(vetor_musicas, 'artist(s)_name')
    print_elementos(len(vetor_musicas),'artist(s)_name')
    pass
elif(opcao==10):
    pass
elif(opcao==11):
    pass
elif(opcao==12):
    pass
elif(opcao==13):
    pass
elif(opcao==14):
    pass

else:
    print("Entrada não identificada")
end_time = time.time()
tempo_corrido = end_time - start_time

arquivo_saida = "tempo_execucao.txt"

with open(arquivo_saida, "a") as arquivo:
    arquivo.write(f"{rotulo_txt}\nTempo de execução do programa: {tempo_corrido} segundos\nNúmero de operações: {numero_operacoes}\n\n")

print(f"{rotulo_txt}\nTempo de execução do programa: {tempo_corrido} segundos\nNúmero de operações: {numero_operacoes}")
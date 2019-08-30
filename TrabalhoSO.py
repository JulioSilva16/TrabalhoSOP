import random

memoria = [' '] * 100
opcao = 0
tamanho = 0
letra = ''
tamBuraco = 0
tamBuracoAntigo = 0
lugares = [] * 0
possiveisLugares = [] * 0


for i in range(100):
    if(random.randint(0,11) >= 5):
        memoria[i] = 'x'
    else:
        memoria[i] = ' '
for i in range(0,20):
    print(memoria[i], end="|")
print()
for i in range(20,40):
    print(memoria[i], end="|")
print()
for i in range(40,60):
    print(memoria[i], end="|")
print()
for i in range(60,80):
    print(memoria[i], end="|")
print()
for i in range(80,100):
    print(memoria[i], end="|")
print()
while(opcao != 4):

    print("1 - Pior Escolha")
    print("2 - Sair")
    print("Escolha o algoritmo pelo numero")
    opcao = int(input())
    if (opcao == 2):
        break

    print("Digite o tamanho da informacao")
    tamanho = int(input())
    print("Digite a letra a ser utiliada")
    letra = input()
   
    if(opcao == 1):

        i = 0
        while (i < 100):
            if memoria[i] == ' ':
                tamBuraco = tamBuraco + 1;
                possiveisLugares.append(i)
                if tamBuraco >= tamanho:
                    if tamBuracoAntigo == 0:
                        tamBuracoAntigo = len(possiveisLugares)
                    else:
                        if tamBuracoAntigo < len(possiveisLugares):
                            tamBuracoAntigo = len(possiveisLugares)
                            lugares = possiveisLugares
            else:
                tamBuraco = 0
                possiveisLugares = [] * 0
            i = i + 1
        
        if len(lugares) != 0:
            for i in range(tamanho):
                memoria[lugares[i]] = letra
        
        tamBuracoAntigo = 0
        lugares = [] * 0

    for i in range(0, 20):
        print(memoria[i], end="|")
    print()
    for i in range(20, 40):
        print(memoria[i], end="|")
    print()
    for i in range(40, 60):
        print(memoria[i], end="|")
    print()
    for i in range(60, 80):
        print(memoria[i], end="|")
    print()
    for i in range(80, 100):
        print(memoria[i], end="|")
    print()
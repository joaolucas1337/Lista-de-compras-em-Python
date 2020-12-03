from os import system, name
from time import sleep
import random


def cls():
    # para Windows
    if name == 'nt':
        _ = system('cls')


cls()

print("=" * 61)
print("Ola Mateus, espero que esteja tudo bem com o senhor!\n")
print("Se está aqui é porque precisa de mim, então vamos as compras!")
print("=" * 61)

biqueira = 75
protetor_de_clipe = 20
caixa_de_agulha_9rl = 100
caixa_de_agulha_7rl = 95
caixa_de_agulha_5rl = 95
papel_filme = 15
vaselina = 40
batoque = 40
hectografico = 2
papel_toalha = 6
descarpack = 20
canetas_freehand = 12
luva = 90
lista_compras = []
lista1 = []

while True:
    item_1 = input("\nEste mês o senhor precisará de Biqueira [S/N]?").upper()
    if item_1 == "S":
        lista_compras.append(biqueira)
        lista1.append("Biqueira")
        print("=" * 57)
        print("Certo, a Biqueira foi adicionada em sua lista de compras!")
        print("=" * 57)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()


    item_2 = input("\nEste mês o senhor precisara de Protetor de Clipe [S/N]?").upper()
    if item_2 == "S":
        lista_compras.append(protetor_de_clipe)
        lista1.append("Protetor de Clipe")
        print("=" * 66)
        print("Certo, o Protetor de Clipe foi adicionado em sua lista de compras!")
        print("=" * 66)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()



    item_3 = input("\nEste mês o senhor precisara da Caixa de agulha 9rl [S/N]?").upper()
    if item_3 == "S":
        lista_compras.append(caixa_de_agulha_9rl)
        lista1.append("Caixa de agulha 9rl")
        print("=" * 68)
        print("Certo, a Caixa de agulha 9rl foi adicionada em sua lista de compras!")
        print("=" * 68)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()
    


    item_4 = input("\nEste mês o senhor precisara da Caixa de agulha 7rl [S/N]?").upper()
    if item_4 == "S":
        lista_compras.append(caixa_de_agulha_7rl)
        lista1.append("Caixa de agulha 7rl")
        print("=" * 68)
        print("Certo, a Caixa de agulha 7rl foi adicionada em sua lista de compras!")
        print("=" * 68)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()
    


    item_5 = input("\nEste mês o senhor precisara da Caixa de agulha 5rl [S/N]?").upper()
    if item_5 == "S":
        lista_compras.append(caixa_de_agulha_5rl)
        lista1.append("Caixa de agulha 5rl")
        print("=" * 68)
        print("Certo, a Caixa de agulha 5rl foi adicionada em sua lista de compras!")
        print("=" * 68)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()
    


    item_6 = input("\nEste mês o senhor precisara de Papel filme [S/N]?").upper()
    if item_6 == "S":
        lista_compras.append(papel_filme)
        lista1.append("Papel filme")
        print("=" * 60)
        print("Certo, o Papel filme foi adicionada em sua lista de compras!")
        print("=" * 60)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()



    item_7 = input("\nEste mês o senhor precisara de Vaselina [S/N]?").upper()
    if item_7 == "S":
        lista_compras.append(vaselina)
        lista1.append("Vaselina")
        print("=" * 57)
        print("Certo, a Vaselina foi adicionada em sua lista de compras!")
        print("=" * 57)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()
    


    item_8 = input("\nEste mês o senhor precisara de Batoque [S/N]?").upper()
    if item_8 == "S":
        lista_compras.append(batoque)
        lista1.append("Batoque")
        print("=" * 54)
        print("Certo, Batoque foi adicionado em sua lista de compras!")
        print("=" * 54)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()
    


    item_9 = input("\nEste mês o senhor precisara de Hectografico [S/N]?").upper()
    if item_9 == "S":
        lista_compras.append(hectografico)
        lista1.append("Hectografico")
        print("=" * 70)
        print("Certo, a folha de Hectografico foi adicionado em sua lista de compras!")
        print("=" * 70)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()



    item_10 = input("\nEste mês o senhor precisara de Papel Toalha [S/N]?").upper()
    if item_10 == "S":
        lista_compras.append(papel_toalha)
        lista1.append("Papel Toalha")
        print("=" * 59)
        print("Certo, Papel Toalha foi adicionado em sua lista de compras!")
        print("=" * 59)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()



    item_11 = input("\nEste mês o senhor precisara de Descarpack [S/N]?").upper()
    if item_11 == "S":
        lista_compras.append(descarpack)
        lista1.append("Descarpack")
        print("=" * 68)
        print("Certo, a Caixa de Descarpack foi adicionada em sua lista de compras!")
        print("=" * 68)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()



    item_12 = input("\nEste mês o senhor precisara de Canetas freehand [S/N]?").upper()
    if item_12 == "S":
        lista_compras.append(canetas_freehand)
        lista1.append("Canetas freehand")
        print("=" * 69)
        print("Certo, as Canetas freehand foram adicionadas em sua lista de compras!")
        print("=" * 69)
        sleep(2)
        cls()
    else:
        print("=" * 31)
        print("OK, iremos para o próximo item!")
        print("=" * 31)
        sleep(2)
        cls()



    item_13 = input("\nEste mês o senhor precisara de Luva [S/N]?").upper()
    if item_13 == "S":
        lista_compras.append(luva)
        lista1.append("Luva")
        print("=" * 53)
        print("Certo, a Luva foi adicionada em sua lista de compras!")
        print("Agora iremos para o valor da lista finalizada!")
        print("=" * 53)
        sleep(2.5)
        cls()
    else:
        print("=" * 50)
        print("OK, Agora iremos para o valor da lista finalizada!")
        print("=" * 50)
        sleep(2)
        cls()
    
    print("\nSua lista de compras deste mês é:\n")
    sleep(1)
    print(lista1)
    sleep(1)
    print("\nMateus este mês o senhor gastará R${:.2f} em compras para o seu trabalho!".format(sum(lista_compras)))
    sleep(1)
    print("\nAté a Próxima!")
    sleep(1)
    input("\nFeito por João Lucas 'S0ARES'...")
    sleep(1)
    break



        
    




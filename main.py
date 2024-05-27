'''
Crie um programa que:
- Inserir pessoas na lista;
- Liste o nome de todas as pessoas cadastradas;
- Pesquisar pelo nome de uma pessoa;
- Ordenar a lista por ordem alfabética;
- Atualizar nome;
- Deletar nome da lista;
- Sair do programa
'''
import os
nomes = []
while True:
    nome = input('Informe um nome (quando terminar de inserir, aperte o enter 2x para encerrar e exibir a lista): ')
    if nome != '':
        nomes.append(nome)
        continue
    else:
        break
os.system('cls')
print(f'LISTA DOS NOMES')
nomes.sort()
for nome in nomes:
    print(nome)
print('\nIxi, escreveu errado? Não se preocupa, você pode atualizar!')
while True:
    atualizar = input('Você quer atualizar algum nome (s/n)?')
    if atualizar == 's':
            atualizar = input('Qual nome você você deseja atualizar? ')
            nomes[nomes.index(atualizar)] = input('Informe o novo nome: ')
            break
    elif atualizar == 'n':
            break
print('\nLISTA DOS NOMES')
nomes.sort()
for nome_novo in nomes:
    print(nome_novo)
print('\nSe arrependeu do nome que escreveu? Relaxa, vamos apagá-lo.')
while True:
    apagar = input('Você quer apagar algum nome (s/n)?')
    if apagar == 's':
        apagar = input('Qual nome você quer apagar? ')
        break
    elif apagar == 'n':
        break
os.system('cls')
try:
    nomes.remove(apagar)
    print(f'{'='*20} LISTA DOS NOMES ATUALIZADA {'='*20}')
except:
    print('Não foi possível deletar esse nome.')
for nome_del in nomes:
    print(nome_del)
nome_novo = []
while True:
    lembrar = input('\nLembrou de algum nome (s/n)? ')
    if lembrar == 's':
        break
    elif lembrar == 'n':
       break
while True:
    lembrar = input('Qual o novo nome você deseja adicionar? ')
    if lembrar != '':
        nome_novo.append(lembrar)
        break
    else:
       break
nome_novo.append(nomes)
os.system('cls')
print(f'{'='*20} LISTA FINAL DOS NOMES {'='*20}')
for novo in (nomes):
    print(novo)
print('\nObrigada, até mais!')
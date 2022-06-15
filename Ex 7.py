nomeinverso = []
nome = str.upper(input('Digite seu nome: '))
inome = len(nome) - 1
while inome >= 0:
    nomeinverso.append(nome[inome])
    inome -= 1
print(nomeinverso)



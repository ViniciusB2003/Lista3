idade = []
altura = []
idadeinversa = []
alturainversa = []
for x in range(5):
    idade.append(int(input('Digite a idade: ')))
    altura.append(float(input('Digite a altura da pessoa: ')))
iidade = len(idade)-1
ialtura = len(altura)-1
while (iidade >= 0 ) and (ialtura >= 0):
    idadeinversa.append(idade[iidade])
    iidade -= 1
    alturainversa.append(altura[ialtura])
    ialtura -=1
print(idadeinversa)
print(alturainversa)






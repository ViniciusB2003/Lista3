m = []
mult = 1
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']: ')))
    m.append(linha)

K = float(input('Digite o número a ser multiplicado pela diagonal: '))
mult = (m[0][0]) * (m[1][1]) * (m[2][2]) * K
print('O Resultado da multiplicação da diagonal principal por: ', K, 'é: ', mult)

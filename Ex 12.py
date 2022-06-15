import numpy
l1 = int(input('Digite quantas linhas a primeira matriz terá: '))
c1 = int(input('Digite quantas colunas a primeira matriz terá: '))
l2 = int(input('Digite quantas linhas a segunda matriz terá: '))
c2 = int(input('Digite quantas colunas a segunda matriz terá: '))
m1 = []
m2 = []
m3 = []
if c1 == l2:
    for i in range(l1):
        linha = []
        for j in range(c1):
            linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']: ')))
        m1.append(linha)
    for x in range(l2):
        linha = []
        for y in range(c2):
            linha.append(int(input('Digite o valor de [' + str(x) + ',' + str(y) + ']: ')))
        m2.append(linha)
    m3 = numpy.dot(m1, m2)
    print('Primeira matriz: ')
    for d in m1:
        print(d)
    print('A Segunda matriz: ')
    for s in m2:
        print(s)
    print('Matriz Resultante: ')
    print(m3)
else:
    print('Matrizes não compatíveis para multiplicação')




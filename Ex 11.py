m1 = []
m2 = []
m3 = []
for i in range(2):
    linha = []
    for j in range(2):
        linha.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']: ')))
    m1.append(linha)
for x in range(2):
    linha = []
    for y in range(2):
        linha.append(int(input('Digite o valor de [' + str(x) + ',' + str(y) + ']: ')))
    m2.append(linha)
for a in range(2):
    linha = []
    for b in range(2):
        linha.append((m1[a][b])+(m2[a][b]))
    m3.append(linha)
    print(m3[a])
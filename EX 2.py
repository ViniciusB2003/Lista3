n = []
soma = 0
mult = 1
for x in range(5):
    n.append(int(input('Digite um número: ')))
    soma += n[x]
    mult *= n[x]
print('Os números digitados foram: ', n)
print('A Soma dos números é: ', soma)
print('A Multiplicação dos números é: ', mult)


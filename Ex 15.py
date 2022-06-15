def pn(n1):
    teste = 'C'
    if n1 > 0:
        teste = 'P'
    elif n1 <= 0:
        teste = 'N'
    return teste
n10 = float(input('Digite Um Número: '))
r = pn(n10)
print(r)



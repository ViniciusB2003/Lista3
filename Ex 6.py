A = str(input('Digite uma frase: '))
B = str(input('Digite uma segunda frase: '))
A = str.upper(A)
B = str.upper(B)
if len(A) != len(B):
    print('O Tamanho das frases são diferentes')
else:
    print('O Tamanho ds frases é o mesmo')
if A != B:
    print('As frases são diferentes')
else:
    print('As frases são iguais')
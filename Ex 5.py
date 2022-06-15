a = []
b = []
c = []
for x in range(10):
    a.append(input('Digite um elemento qualquer da 1° Lista: '))
for y in range(10):
    b.append(input('Digite um elemento qualquer da 2° Lista: '))
for z in range(10):
    c.append(a[z])
    for w in range(1):
        c.append(b[z])
print(c)





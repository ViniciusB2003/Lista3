def somaimposto(taxaimposto,custo):
    custo = ((taxaimposto/100) * custo) + custo
    return custo

taxaimposto = float(input('Digite o valor do imposto, em porcentagem: '))
custo = float(input('Digite o valor do produto: '))
vf = somaimposto(taxaimposto,custo)
print(vf)
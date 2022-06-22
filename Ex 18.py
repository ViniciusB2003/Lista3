def data_cal(dia,mes,ano):
    if (dia <= 0 or dia >= 31) or (mes <= 0 or mes > 12) or (ano <= 0):
        return print('NULL')
    if mes == 1:
        mes = 'Janeiro'
    elif mes == 2:
        mes = 'Fevereiro'
    elif mes == 3:
        mes = 'Março'
    elif mes == 4:
        mes = 'Abril'
    elif mes == 5:
        mes = 'Maio:'
    elif mes == 6:
        mes = 'Junho'
    elif mes == 7:
        mes = 'Julho'
    elif mes == 8:
        mes = 'Agosto'
    elif mes == 9:
        mes = 'Setembro'
    elif mes == 10:
        mes = 'Outubro'
    elif mes == 11:
        mes = 'Novembro'
    elif mes == 12:
        mes = 'Dezembro'
    dataf = dia, ' de ', mes, ' de ', ano
    return dataf
D, M, A = input('Digite uma data no formato D/M/A: ').split("/")
D = int(D)
M = int(M)
A = int(A)
datai = data_cal(D, M, A)
print(datai)
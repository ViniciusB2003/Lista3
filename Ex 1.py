naluno = 0.0
media = []
n = 0
for i in range(11):
   naluno = 0
   print('Novo aluno: ')
   for z in range(4):
      naluno += (float(input('Digite a nota do aluno: ')))
   media.append(naluno/4)
for x in media:
   if x >= 7:
      n += 1
print('O número de alunos com nota maior ou igual a 7 é: ', n)



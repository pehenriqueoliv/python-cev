
ficha = []

while True:
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    qc = input('Quer continuar? [S/N] ')
    if qc in 'Nn':
        break

print('=-' * 30)

print(f'{'No.':<4} {"NOME":<10} {"MEDIA":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4} {a[0]:<10} {a[2]:>8}')

print('=-' * 30)

while True:
    opc = int(input('Mostrar notas de qual aluno? [999 interrompe] '))
    print('-' * 30)
    if opc == 999:
        print('Obrigado por utilizar o programa!')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} foram {ficha[opc][1]}')

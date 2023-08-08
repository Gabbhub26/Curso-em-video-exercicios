primeiro = int(input('Primeiro termo da P.A: '))
razao = int(input('Razão da P.A: '))

for c in range(1,11):
    PA = primeiro+((c-1)*razao)
    print(f'{PA}', end = ' ')

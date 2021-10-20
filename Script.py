print('Calculo de aluguel de veículo')
print('Categorias')
print('Cupê = 1')
print('Crossover = 2')
print('Esportivo = 3')
print('Hatch = 4')
print('Jipe = 5')
print('Picape  = 6')
print('Sedan = 7')
print('SUV = 8')
categoria = int(input('Digite o número correspondente a categoria: '))
if categoria == 1:
    valor = 130
    nome = 'Cupê'
elif categoria == 2:
    valor = 50
    nome = 'Crossover'
elif categoria == 3:
    valor = 150
    nome = 'Esportivo'
elif categoria == 4:
    valor = 20
    nome = 'Hatch'
elif categoria == 5:
    valor = 65
    nome = 'Jipe'
elif categoria == 6:
    valor = 90
    nome = 'Picape'
elif categoria == 7:
    valor = 50
    nome = 'Sedan'
elif categoria == 8:
    valor = 120
    nome = 'SUV'    
dias = float(input('Dias alugados: '))
km_inicial = float(input('Km inicial: '))
km_final = float(input('Km final: '))
km_rodado = float(km_final - km_inicial)
valor_km = float(km_rodado * 0.5)
valor_total = float((valor * dias) + valor_km)
print('Modelo: %s' %(nome))
print('Dias alugados: %.0f' %(dias))
print("Km's rodados: %.0f" %(km_rodado))
print('Valor a pagar: R$ %.2f' %(valor_total))

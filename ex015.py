quantDias = int(input('Quantidade de dias do carro alugado: '))
quantKm = int(input('Quantidade de quilômetros: '))
dias = quantDias * 60
km = quantKm * 0.15
print('O total a pagar é R${:.2f}.'.format(dias+km))
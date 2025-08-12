n1 = float(input('Qual a largura da parede? '))
n2 = float(input('Qual a altura da parede? '))
area = n1 * n2
tinta = (n1*n2)/2
print('A área da parede é {:.2f}m². \n A quantidade necessária para pintar a parede é {:.2f} de tinta.'.format(area, tinta))
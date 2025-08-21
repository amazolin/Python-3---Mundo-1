import math
ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

hip = math.sqrt(pow(ca, 2) + pow(co, 2))

print('A hipotenusa do triângulo retângulo é {:.2f}'.format(hip))
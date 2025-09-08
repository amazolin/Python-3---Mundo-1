velocidade = int(input("Qual a velocidade do carro (km/h)? "))
if velocidade > 80:
    print("VOCÊ FOI MULTADO!")
    multa = (velocidade - 80) * 7
    print("O valor da multa é R${:.2f}".format(multa))
else:
    print("Velocidade dentro do limite. Boa viagem!")


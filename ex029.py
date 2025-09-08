velocidade = int(input("Qual a velocidade do carro (km/h)? "))
limite = 80
if velocidade > limite:
    print("VOCÊ FOI MULTADO!")
    multa = (velocidade - limite) * 7
    print("O valor da multa é R${:.2f}".format(multa))
else:
    print("Velocidade dentro do limite. Boa viagem!")


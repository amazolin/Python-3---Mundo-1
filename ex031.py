km = int(input("Qual a distância da viagem (km)? "))

if km <= 200:
    passagem = km * 0.50
else:
    passagem = km * 0.45
print("A distância da sua viagem é {} e o custo a passagem R${:.2f}".format(km, passagem))
salario = float(input("Informe seu salário: "))
if salario >= 1.250:
    aumento = salario + (salario * 0.10)
    print("Seu novo salário é R${:.2f}.".format(aumento))
else:
    aumento = salario = (salario * 0.15)
    print("Seu novo salário é R${:.2f}.".format(aumento))
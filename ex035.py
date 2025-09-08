reta1 = int(input("Digite o comprimeito da primeira reta: "))
reta2 = int(input("Digite o comprimento da segunda reta: "))
reta3 = int(input("Digite o comprimento da terceira reta: "))
if reta1 > reta2+reta3 or reta2 > reta1+reta3 or reta3 > reta1+reta2:
    print("NÃO PODE FORMAR UM TRIÂNGULO.")
else:
    print("É UM TRIÂNGULO!")
import random

print("Tente advinhar o número que o computador escolheu de 1 a 5:")
nComp = random.choice([1,2,3,4,5])
nUsuar = int(input("\nDigite o número:"))
print("O computador escolheu o número {}".format(nComp))
print("Você escolheu {}".format(nUsuar))
if nComp == nUsuar:
    print("VOCÊ VENCEU!")
else:
    print("O COMPUTADOR VENCEU.")
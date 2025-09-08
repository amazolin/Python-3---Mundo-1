import random
from time import sleep
print("Tente advinhar o número que o computador escolheu de 0 a 5: ")
nComp = random.choice([0,1,2,3,4,5]) #Sorteia um número
nUsuar = int(input("\nDigite o número:"))
print("PROCESSANDO...")
sleep(3)
print("O computador escolheu o número {}".format(nComp))
print("Você escolheu {}".format(nUsuar))
if nComp == nUsuar:
    print("VOCÊ VENCEU!")
else:
    print("O COMPUTADOR VENCEU.")
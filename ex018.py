import math

angulo = float(input("Digite o ângulo em graus: "))

# converter para radianos
rad = math.radians(angulo)

# cálculos
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)

# resultado
print(f"Seno: {seno:.2f}")
print(f"Cosseno: {cosseno:.2f}")
print(f"Tangente: {tangente:.2f}")

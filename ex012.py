preco = float(input('Qual o preço do produto? '))
desconto = preco * 5/100
precofinal = preco - desconto
print('O valor do produto com desconto é R${:.2f}'.format(precofinal))

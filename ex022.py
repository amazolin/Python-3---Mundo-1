nome = input('Digite seu nome completo: ')
print('Seu nome em letras maiúsculas: ',nome.upper())
print('Seu nome em letras minúsculas: {}'.format(nome.lower()))

tamanho = len(nome) - nome.count(' ')
print('Seu nome tem ao todo {} letras'.format(tamanho))

primeiroNome = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(primeiroNome[0],len((primeiroNome[0]))))

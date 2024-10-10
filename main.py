import datetime

now = datetime.datetime.now()

nome = input("Digite seu nome: ")

nascimento = int(input("Digite o ano que você nasceu: "))

idade = now.year - nascimento

print(nome + " Seja bem vindo meu nobre. " + "Você tem " + str(idade) + " anos")
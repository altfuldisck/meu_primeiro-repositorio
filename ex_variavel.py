#exercício 1
idade = 18
altura = 1.65
nome = 'Vitória'
estudante = True
type(idade)
type(altura)
type(nome)
type(estudante)
#exercício 2
idade_ex2 = int(input('digite sua idade'))
type(idade_ex2)
print(idade_ex2)
#exercício 3
n1 = int(input())
n2 = int(input())
print(n1 + n2)
#exercício 4
n1 = int(input("Digite um número "))
n2 = int(input("Digite um número "))
n3 = int(input("Digite um número"))
media = (n1 + n2 + n3) / 3
print(f"Média {media:.2f}")
#exercício 5
n1 = float(input("Digite um número "))
n2 = float(input("Digite um número "))
n3 = float(input("Digite um número"))
media = (n1 + n2 + n3) / 3
print(f"Média {media:.2f}")
#exercício 6
nome = input("Digite seu nome completo: ")
print("Nome em maiúsculas:", nome.upper())
primeiro_nome = nome.split()[0]
print("Primeiro nome:", primeiro_nome)
quantidade_letras = len(nome.replace(" ", ""))
print("Quantidade de letras:", quantidade_letras)




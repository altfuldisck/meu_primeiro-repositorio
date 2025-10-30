#exercício 1
frutas = ['maçã','banana','laranja','uva']
#exercício 2
frutas[0]
frutas[-1]
#exercício 3
frutas.append('manga')
frutas = frutas + ['manga']
print(frutas)
#exercício 4
frutas.remove('banana')
print(frutas)
#exercício 5
indice = frutas.index('laranja')
frutas[indice] = 'abacaxi'
print(frutas)
#exercício 6
numeros = list(range(1, 11))
print(numeros)
#exercício 7
soma = sum(numeros)
print(soma)
#exercício 8
maior = max(numeros)
menor = min(numeros)
print(maior)
print(menor)
#exercício 9
numeros_invertidos = list(reversed(numeros))
print(numeros_invertidos)
#exercício 10
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba"]
#exercício 11
sorted(cidades)
print(cidades)
#exercício 12
cidades.append('Porto Alegre')
print(cidades)
#exercício 13
indice_curitiba = cidades.index('Curitiba')
print(indice_curitiba)
#exercício 14
cidades.remove('Rio de Janeiro')
print(cidades)
#exercício 15
lista1 =[1,2,3]
lista2 = [4,5,6]
#exercício 16
lista3 = lista1 + lista2
#exercício 17
print(lista3)
#exercício 18
animais_domesticos = ['cachorro','gato','coelho']
animais_selvagens = ['leão','tigre','urso']
#exercício 19
todos_animais = animais_domesticos + animais_selvagens
#exercício 20
print(todos_animais)
#exercício 21
nomes = ['Ana','Pedro','Maria','João']
#exercício 22
for nome in nomes:
    print(nome) 
#exercício 23
nomes_maiusculos = []
for nome in nomes:
    nomes_maiusculos.append(nome.upper())
print(nomes_maiusculos)
#exercíco 24
numeros = list(range(1,21))
for numero in numeros:
    if numero % 2 == 0:
        print(numero)
#exercício 25
quadrados = []
numeros = [1, 3, 8, 9]
for numero in numeros:
    quadrados.append(numero**2)
print(quadrados)
#exercício 26
palavras = ["python", "java", "c", "javascript"]
for palavra in palavras:
    print(f'{palavra} tem {len(palavra)} letras')
#exercício 27
idades = [12, 18, 25, 40, 60]
for idade in idades:
    if idade >= 18:
        print(f'{idade}: maior de idade')
    else:
        print(f'{idade}: menor de idade')
#exercício 28
notas = [5.5, 7.0, 8.3, 4.9, 6.2]
aprovados = 0
reprovados = 0
for nota in notas:
    if nota >= 7:
        aprovados += 1
    else:
        reprovados += 1
print(f'aprovados:{aprovados}, reprovados:{reprovados}')
#exercício 29
palavras = ["arara", "banana", "radar", "python"]
for palavra in palavras:
    if palavra == palavra[::-1]:
        print(f'{palavra} é um palíndromo')
#exercício 30
compras = ["arroz", "feijão", "batata", "carne"]
for item in compras:
    print(f'preciso comprar:{item}')
#exercício 31
numero = 1 
while numero <= 10:
    print(numero)
    numero += 1
#exercício 32 revisar
while True:
    numero = int(input('digite um numero'))
    if numero == 0:
        break
#exercício 33
soma = 0
numero = 1
while numero <= 100:
    soma += numero
    numero += 1
print('a soma de 1 a 100 é:', soma)
#exercício 34
while True:
    numero = int(input('adivinhe o número'))
    if numero == 7:
        break
    else:
        print('número errado')
#exercício 35
numero = 2
while numero <= 20:
    print(numero)
    numero = numero + 2
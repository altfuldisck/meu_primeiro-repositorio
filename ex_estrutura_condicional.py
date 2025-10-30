#exercício 1
numero = int(input())
if numero % 2 == 0:
    print ('é par')
else:
    print('é impar')

#exercício 2
ap1 = float(input('digite a nota da ap1'))
ap2 = float(input('digite a nota da ap2'))
ac = float(input('digite a nota da ac'))
media = 0.4*ap1 + 0.4*ap2 + 0.2*ac
if media >= 7:
    print('aprovado')
else:
    print('reprovado')

#exercício 3
valor_compra = float(input('digite o valor da compra'))
if valor_compra > 100:
    desconto = valor_compra * 0.10
    valor_final = valor_compra - desconto
else:
    valor_final = valor_compra
print(f'valor final da compra:R${valor_final:.2f}')

#exercício 4
celsius = float(input('digite a temperatura em celsius'))
fahrenheit = (celsius * 9/5) + 32
print(f'{fahrenheit:.2f}°F')

#exercício 5
n1 = int(input('digite o primeiro número'))
n2 = int(input('digite o segundo número'))
if n1 > n2:
    print(f'o maior número é {n1}')
elif n2 > n1:
    print(f'o maior número é {n2}')
else:
    print('os dois são iguais')

#exercício 6
n1 = int(input('digite o primeiro número'))
n2 = int(input('digite o segundo número'))
n3 = int(input('digite o terceiro número'))
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3
print(f'o maior número é {maior}')

#exercício 7
n1 = float(input('digite o primeiro número'))
n2 = float(input('digite o segundo número'))
operação = input('digite a operação desejada(+,-,/,*)')
if operação == '+':
    resultado = n1 + n2
elif operação == '-':
    resultado = n1 - n2
elif operação == '*':
    resultado = n1 * n2
elif operação == '/':
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = 'divisão por zero não existe'
else: 
    resultado = 'operação invalida'
print(f'resultado {resultado:.2f}')

#exercício 8
numeros = input('digite números separados por espaço').split()
numeros = [int(n) for n in numeros]
positivos = negativos = zeros = 0
for numeros in 0:
    if numeros > 0:
        positivos += 1
    elif numeros < 0:
        negativos += 1
    else:
        zeros += 1
print(f'{positivo} positivos, {negativos} negativos, {zeros} zeros')

#exercício 9
ano = int(input('digite o ano'))
if (ano % 4 == 0 and ano % 100 !=0) or (ano % 400 == 0):
    print('ano bissexto')
else:
    print('não é bissexto')

#exercício 10
idade = int(input('digite a idade'))
if idade >= 18 and idade <= 65:
    print('dentro da faixa etária')
else:
    print('fora da faixa etária')

#exercíco 11
usuario = input('tipo de funcionário')
senha = input('digite a senha')
if usuario == 'vitoria' and senha == '1234':
    print('acesso permitido')
else:
    print('acesso negado') 

#exercício 12
idade = int(input('digite a idade'))
if idade < 16:
    print('não vota')
elif idade >= 18 and idade <= 70:
    print('voto obrigatório')
else:
    print('voto optativo')

#exercício 13
numero = int(input('digite um número inteiro'))
if not(numero >= 10 and numero <= 50):
    print('fora do intervalo')
else:
    print('dentro do intervalo')

#exercício 14
nota = float(input())
if nota >= 7:
    print('aprovado')
elif nota < 7 and nota >= 5:
    print('recuperação')
else:
    print('reprovado')
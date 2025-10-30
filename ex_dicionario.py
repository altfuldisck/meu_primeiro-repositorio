#exercício 1
aluno = {
    'nome':'Vitória',
    'idade':18,
    'curso':'economia'
}
print(f'nome: {aluno['nome']}')
print(f'idade: {aluno['idade']}')
print(f'curso: {aluno['curso']}')

#exercício 2
produto = {
    "nome": "Teclado Mecânico",
    "preco": 350.00,
    "estoque": 10
}
produto['marca'] = 'Dell'
produto['preço'] = 320.00
produto['estoque'] -= 2
del produto['marca']
print(produto)

#exercício 3
notas = {
    "Alice": 8.5,
    "Bruno": 7.0,
    "Carla": 9.2,
    "Daniel": 6.8
}
for nome, nota in notas.items():
    print(f'{nome}: {nota}')
media = sum(notas.values())/len(notas)
print(f'média das notas:{media:.2f}')

#exercício 4
numeros = {"a": 10, "b": 20, "c": 30}
soma = sum(numeros.values())
print(f'soma total: {soma}')

#exercício 5
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
    frequencia[item] = frequencia.get(item, 0) + 1
print(frequencia)
#outra forma
lista = ["maçã", "banana", "laranja", "maçã", "banana", "maçã"]
frequencia = {}
for item in lista:
   if item in frequencia:
       frequencia[item] += 1
else: 
       frequencia = 1
print(frequencia)
#exercício 6
produtos = {"caneta": 10, "mochila": 80, "caderno": 45, "notebook": 3000}
filtro={}
for produto, preço in produtos.items():
    if preço>=50:
       filtro[produto]= preço
print(filtro)

#exercicio 7 
tradutor = {
    'door': 'porta',
    'cat': 'gato',
    'drink': 'bebida'
}
palavra = input('digite a palavra em inglês')
if palavra in tradutor:
    print(f'tradução: {tradutor[palavra]}')
else:
    print('palavra não encontrada')

#exercicio 8 
compras = {}
produto = input('digite o produto')
quantidade = int(input('digite a quantidade'))
if produto in compras :
    compras[produto] = compras[produto] + quantidade
else:
    compras[produto] = quantidade
print(produto, '=', compras[produto])

#exercíco 9
turma = {
    "Ana": {"idade": 17, "notas": [8, 9, 7]},
    "Pedro": {"idade": 18, "notas": [6, 7, 8]},
    "Mariana": {"idade": 17, "notas": [9, 10, 8]}
}
turma['vitória']={'idade':18, 'notas':[8, 9, 7]}
for key, value in turma.items():
    media = sum(value['notas'])/len(value['notas'])
    print(key, media)
#exercíco 10 REVISAR
funcionarios = {}

while True:
    opcao = input("Digite [1] para cadastrar, [2] para consultar, [3] para sair: ")

    if opcao == "1":
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = input("Salário: ")
        funcionarios[nome] = {"cargo": cargo, "salario": salario}
        print("Funcionário cadastrado!\n")

    elif opcao == "2":
        nome = input("Nome para consulta: ")
        if nome in funcionarios:
            print(f"Cargo: {funcionarios[nome]['cargo']}")
            print(f"Salário: R$ {funcionarios[nome]['salario']}\n")
        else:
            print("Funcionário não encontrado.\n")

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.\n")






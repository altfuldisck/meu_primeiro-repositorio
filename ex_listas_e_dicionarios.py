#exercício 1
faturamento = [
    {"dia": "segunda", "valor": 1200},
    {"dia": "terça", "valor": 1500},
    {"dia": "quarta", "valor": 900},
    {"dia": "quinta", "valor": 1800},
    {"dia": "sexta", "valor": 2400},
]
total = 0
for dia in faturamento:
    total += dia["valor"]
maior_valor = 0
maior_dia = ""
for dia in faturamento:
    if dia["valor"] > maior_valor:
        maior_valor = dia["valor"]
        maior_dia = dia
#exercício 2
estoque = {
    "notebook": [5, 7, 3],
    "mouse": [20, 25, 18],
    "teclado": [12, 14, 9],
}
totais = {produto: sum(qtd) for produto, qtd in estoque.items()}
menor = min(totais, key=totais.get)

#exercício 3
funcionarios = [
    {"nome": "Ana", "salario": 4500, "departamento": "RH"},
    {"nome": "Carlos", "salario": 7000, "departamento": "TI"},
    {"nome": "Beatriz", "salario": 5200, "departamento": "Financeiro"},
    {"nome": "João", "salario": 4800, "departamento": "TI"},
]
folha_total = 0
for f in funcionarios:
    folha_total += f["salario"]
maior_salario = 0
funcionario_maior = ""
for f in funcionarios:
    if f["salario"] > maior_salario:
        maior_salario = f["salario"]
        funcionario_maior = f["nome"]
salarios_por_departamento = {}
for f in funcionarios:
    depto = f["departamento"]
    if depto not in salarios_por_departamento:
        salarios_por_departamento[depto] = []
    salarios_por_departamento[depto].append(f["salario"])

#exercício 4
avaliacoes = {
    "loja A": [8, 9, 7, 10, 6],
    "loja B": [5, 7, 6, 8, 7],
    "loja C": [9, 8, 9, 10, 9],
}
medias = {loja: sum(notas)/len(notas) for loja, notas in avaliacoes.items()}
maior_media = max(medias, key=medias.get)

#exercício 5
vendas = [
    {"vendedor": "Marcos", "itens": {"notebook": 2, "mouse": 5}},
    {"vendedor": "Lucia", "itens": {"notebook": 1, "teclado": 3}},
    {"vendedor": "Paula", "itens": {"mouse": 4, "teclado": 2}},
]
total_notebooks = 0
for v in vendas:
    total_notebooks += v["itens"].get("notebook", 0)
maior_total = 0
melhor_vendedor = ""
for v in vendas:
    soma = 0
    for qtd in v["itens"].values():
        soma += qtd
    if soma > maior_total:
        maior_total = soma
        melhor_vendedor = v["vendedor"]
consolidado = {}
for v in vendas:
    for produto, qtd in v["itens"].items():
        if produto not in consolidado:
            consolidado[produto] = 0
        consolidado[produto] += qtd

#exercício 6
produtos = [
    {"nome": "Notebook", "preco": 3500},
    {"nome": "Mouse", "preco": 80},
    {"nome": "Teclado", "preco": 150},
    {"nome": "Cadeira", "preco": 900},
]
classificacao = {}
for p in produtos:
    preco = p["preco"]
    if preco <= 100:
        tipo = "barato"
    elif preco <= 1000:
        tipo = "médio"
    else:
        tipo = "caro"
    classificacao[p["nome"]] = tipo

#exercício 7
funcionarios = [
    {"nome": "Ana", "nota": 9},
    {"nome": "Carlos", "nota": 6},
    {"nome": "Beatriz", "nota": 4},
    {"nome": "João", "nota": 7},
]
avaliacao = {}
for f in funcionarios:
    nota = f["nota"]
    if nota >= 8:
        status = "Excelente"
    elif nota >= 5:
        status = "Regular"
    else:
        status = "Precisa melhorar"
    avaliacao[f["nome"]] = status

#exercício 8
estoque = {
    "notebook": 3,
    "mouse": 25,
    "teclado": 8,
    "monitor": 2
}
for produto, qtd in estoque.items():
    if qtd < 5:
        print(f"{produto}: Estoque crítico")
    elif qtd < 10:
        print(f"{produto}: Estoque baixo")
    else:
        print(f"{produto}: Estoque adequado")

#exercício 9
vendas = [
    {"regiao": "Sul", "valor": 12000},
    {"regiao": "Norte", "valor": 8000},
    {"regiao": "Sudeste", "valor": 20000},
    {"regiao": "Centro-Oeste", "valor": 5000},
]
classificacao = []
for v in vendas:
    situacao = "Meta atingida" if v["valor"] >= 10000 else "Meta não atingida"
    classificacao.append({"regiao": v["regiao"], "situacao": situacao})

#exercício 10
compras = [
    {"cliente": "Maria", "valor": 450},
    {"cliente": "José", "valor": 1200},
    {"cliente": "Clara", "valor": 3000},
]

resultado = []
for c in compras:
    valor = c["valor"]
    if valor < 500:
        desconto = 0.05
    elif valor < 2000:
        desconto = 0.10
    else:
        desconto = 0.15
    valor_final = valor * (1 - desconto)
    resultado.append({
        "cliente": c["cliente"],
        "valor original": valor,
        "desconto": desconto * 100,
        "valor final": round(valor_final, 2)
    })

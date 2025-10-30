import pandas as pd
file = 'cadastro_alunos.xlsx'
df = pd.read_excel(file)
df['nome_disciplina']
#exercício 1
df.head(5)
df.tail(5)
df.sample(5)
#exercício 2
df.shape
#exercício 3
df.columns
#exercício 4
df.dtypes
#exercício 5
df.describe()
#exercício 6
df.info()
import pandas as pd
file = 'imoveis_brasil.csv'
df = pd.read_csv(file)
#exercício 1
df.head(5)
df.tail(5)
df.sample(5)
#exercício 2
df.shape
#exercício 3
df.columns
#exercício 4
df.dtypes
#exercício 5
df.describe()
#exercício 6
df.info()
#exercício 7
df['Tipo_Imovel'].unique()
#exercício 8
filtro = df['Valor_Imovel']>1000000
df.loc[filtro]
#exercício 9
coluna = df['Cidade','Bairro','Valor_Imovel']
df[coluna]
#exercício 10
filtro = df['Cidade'] == 'Curitiba'
df.loc[filtro]
#exercício 11
df.isnull().sum()
#exercício 12
df.sort_values('Valor_Imovel', ascending = False)
#exercício 13
df['Valor_Imovel'].mean()
#exercício 14
df['Valor_Imovel'].median()
#exercício 15
df['Valor_Imovel'].std()
#exercício 16
df['Area_m2'].min()
df['Area_m2'].max()
#exercício 17
media = df['Valor_Imovel'].mean()
filtro = df['Valor_Imovel']>media
df.loc[filtro]
#exercício 18
valor = df['Valor_Imovel']
area = df['Valor_m2']
df['Valor_m2'] = valor/area
#exercício 19
dic = {'Cidade': 'Teste', 'Valor_Imovel':999, 'Area_m2':100}
df.loc[len(df)] = dic
#exercício 20
df.isnull().sum()
#exercício 21
filtro = df['Numero_Quartos'] != 5
df = df.loc[filtro]
#exercício 22
df.drop(columns=['ID_Imovel'])
#exercício 23
filtro = df['Cidade'] != 'Teste'
df = df.loc[filtro]
#exercício 24

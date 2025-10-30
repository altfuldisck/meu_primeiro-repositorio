import matplotlib.pyplot as plt
import pandas as pd

file='empresas_desempenho.csv'
df=pd.read_csv(file)
df.head()

#gráfico de linha
filtro=df['Setor']=='Comércio'
df_com = df.loc[filtro]
plt.figure(figsize=(8,5))
plt.plot(df_com['Ano'], df_com['Receita'])
plt.title('Gráfico de linha receita x ano')
plt.xlabel('Ano')
plt.ylabel('Receita')
plt.show()

#gráfico de barras
df_grouped = df.groupby('Setor')['Receita'].sum().reset_index()
plt.figure(figsize=(8,5))
plt.bar(df_grouped['Setor'], df_grouped['Receita'])
plt.title('Gráfico de barras setor x receita')
plt.xlabel('Setor')
plt.ylabel('Receita')
plt.show()

#gráfico de pizza
import matplotlib.pyplot as plt
import pandas as pd

file='empresas_desempenho.csv'
df=pd.read_csv(file)
df.head()

df_part = df.groupby('Setor')['ParticipacaoMercado'].mean().reset_index()
plt.figure(figsize=(8,5))
plt.pie(df_part['ParticipacaoMercado'], autopct ='%1.2f%%')
plt.title('Gráfico de pizza de Participação do Mercado')
plt.show()

#chat
import matplotlib.pyplot as plt
import seaborn as sns

# Filtragem
filtro = df['Setor'] == 'Comércio'
df_com = df.loc[filtro]

# Estilo geral
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("flare")

# Criar figura
plt.figure(figsize=(10,6))

# Plot com formatação aprimorada
plt.plot(
    df_com['Ano'], df_com['Receita'],
    color='#FF6F61',            # tom coral moderno
    linewidth=3,
    marker='o',
    markersize=9,
    markerfacecolor='#FFD700',  # dourado
    markeredgecolor='white',
    alpha=0.9
)

# Títulos e rótulos
plt.title('📈 Receita do Setor de Comércio por Ano', fontsize=18, fontweight='bold', color='#333')
plt.xlabel('Ano', fontsize=14, color='#555')
plt.ylabel('Receita (R$)', fontsize=14, color='#555')

# Ajustes visuais
plt.grid(True, linestyle='--', alpha=0.6)
sns.despine()

# Fundo suave
plt.gca().set_facecolor('#f9f9f9')

# Anotar o valor máximo (opcional, mas bonito!)
max_ano = df_com.loc[df_com['Receita'].idxmax(), 'Ano']
max_val = df_com['Receita'].max()
plt.text(max_ano, max_val, f'Máximo: {max_val:,.0f}', color='#FF6F61', fontsize=12,
         ha='left', va='bottom', fontweight='bold')

# Mostrar gráfico
plt.tight_layout()
plt.show()


#chat 2
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Leitura e agrupamento
file = 'empresas_desempenho.csv'
df = pd.read_csv(file)
df_part = df.groupby('Setor')['ParticipacaoMercado'].mean().reset_index()

# Paleta de cores moderna e elegante
colors = sns.color_palette("viridis", len(df_part))

# Figura
plt.figure(figsize=(9,6))

# Gráfico de pizza formatado
wedges, texts, autotexts = plt.pie(
    df_part['ParticipacaoMercado'],
    labels=df_part['Setor'],
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    pctdistance=0.8,
    textprops={'color':'black', 'fontsize':11}
)

# Estilo dos percentuais
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontweight('bold')

# Título
plt.title(
    'Participação Média de Mercado por Setor',
    fontsize=16,
    fontweight='bold',
    color='#333',
    pad=20
)

# Adiciona o círculo central (rosquinha)
centre_circle = plt.Circle((0,0),0.60,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Mantém o formato circular
plt.axis('equal')

# Fundo limpo e layout ajustado
fig.set_facecolor('#f7f7f7')
plt.tight_layout()
plt.show()




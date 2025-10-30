import streamlit as st

st.title('meu primeiro dashboard')
st.text('meu nome é vitória')
st.button('aperte aqui')
st.slider('idade',0,100,25)
df = pd.read_csv('empresas_desempenho.csv')
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

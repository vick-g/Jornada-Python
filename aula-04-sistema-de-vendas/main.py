## titulo: Sistema de Vendas
# Seção cadastrar vendas
    # Campo data
    # Campo vendedor
    # Campo produto
    # Campo quantidade
    # Campo valor
    # Botão cadastrar venda
        # Tem q salvar a venda na tabela de vendas
# Vendas cadastradas
    # Tabela com as vendas cadastradas
# Seção dashboard
    # Card/Metrica de vendas totais
    # Gráfico de barras para vendas por vendedor
    # Gráfico de pizza para vendas por produto

# Usamos
    # Streamlit para criar a interface
    # Pandas para manipular os dados
    # Plotly para criar os gráficos

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de dados 
tabela_vendas = pd.read_csv("aula-04-sistema-de-vendas/vendas.csv")

st.write("# Sistema de Vendas 💰")

# seção de cadastro de vendas


st.write("## Cadastrar Vendas")
data = st.date_input("Data da Venda")
vendedor = st.selectbox("Vendedor", ["Victor", "Pedro", "João"], index=None, placeholder="Selecione o vendedor")
produto = st.selectbox("Produto", ["Notebook", "Celular", "Tablet"], index=None, placeholder="Selecione o produto")
quantidade = st.number_input("Quantidade", step=1)
valor = st.number_input("Valor Unitário", step=0.01)
Botao_cadastrar = st.button("Cadastrar Venda")

# seção de vendas cadastradas
st.write("## Vendass Cadastradas")
st.dataframe(tabela_vendas)

# seção de dashboard
st.write("## Dashboard")
# Card/Metrica de vendas totais
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de barras para vendas por vendedor
grafico_vendas = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto", title="Vendas por Vendedor")
st.plotly_chart(grafico_vendas)

# Gráfico de pizza para vendas por produto
grafico_produtos = px.pie(tabela_vendas, values="valor", names="produto", title="Vendas por Produto")
st.plotly_chart(grafico_produtos)

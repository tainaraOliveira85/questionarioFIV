import streamlit as st

st.title('Questionario feminino pos Fertilizacao In Vitro (FIV)')

dimensao1 = st.container('Dimensao 1: Competencia tecnica medica')
dimensao1.selectbox('Medical care','I received the best possible medical care (examinations and treatments) as far as I can tell')
dimensao2 = st.container('Dimensao 2: Condicoes tecnico-fisicas ')
dimensao2.selectbox('Medical care','I received the best possible medical care (examinations and treatments) as far as I can tell')
dimensao3 = st.container('Dimensao 3: Abordagem de orientacao')
dimensao3.selectbox('Medical care','I received the best possible medical care (examinations and treatments) as far as I can tell')
dimensao4 = st.container('Dimensao 4: Atmosfera socio-cultural')
dimensao4.selectbox('Medical care','I received the best possible medical care (examinations and treatments) as far as I can tell')

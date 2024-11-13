import streamlit as st
st.title("Este é o título do app")
st.header("Este é o subtítulo")
st.subheader("Este é o terceiro subtítulo")
st.markdown("Este é texto")
st.caption("Esta é a a legenda")
st.code("x=2021")
st.latex(r''' a+a r^1+a r^2+a r^3 ''')

numero = st.slider('Selecione um número', min_value = 0, max_value = 100)
st.text("Seu número é " + str(numero))


satisfacao = st.select_slider("Grau de Satisfação", [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
st.text("Seu grau de satisfação é " + str(satisfacao))
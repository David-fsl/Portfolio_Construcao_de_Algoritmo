import streamlit as st
import requests

st.set_page_config(page_title="Portfólio - Construção de Algoritmos", layout="centered")

st.title("Portfólio - Construção de Algoritmos")
st.write("Este aplicativo demonstra os conhecimentos adquiridos durante o semestre na disciplina 'Construção de Algoritmos'")

menu = st.sidebar.radio(
    "Escolha um tema:",
    (
        "Decisão e Repetição", 
        "Vetores e Matrizes", 
        "Funções e Bibliotecas", 
        "Registros", 
        "Arquivos em Disco", 
        "Recursividade", 
        "Complexidade de Tempo de Algoritmo (Big O)", 
        "Uso de API's Externas"
    )
)

if menu == "Decisão e Repetição":
    st.subheader("Decisão e Repetição")

elif menu == "Vetores e Matrizes":
    st.subheader("Vetores e Matrizes")

elif menu == "Funções e Bibliotecas":
    st.subheader("Funções e Bibliotecas")

elif menu == "Registros":
    st.subheader("Registros")

elif menu == "Arquivos em Disco":
    st.subheader("Arquivos em Disco")

elif menu == "Recursividade":
    st.subheader("Recursividade")

elif menu == "Complexidade de Tempo de Algoritmo (Big O)":
    st.subheader("Complexidade de Tempo de Algoritmo (Big O)")

elif menu == "Uso de API's Externas":
    st.subheader("Uso de API's Externas")

else:
    st.subheader("Tópico não encontrado")
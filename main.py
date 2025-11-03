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
        "Uso de API's Externas",
        "Consulta CEP",
        "Cotação Dólar",
        "Monitoramento de ônibus"
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
    st.write("Clique aqui para gerar um fato aleatório utilizando a API pública 'Useless Facts'")
    
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random"
    
    if st.button("Gerar fato aleatório"):
        response = requests.get(url)

        if(response.status_code == 200):
            dados = response.json()
            fato = dados['text']
            st.write(fato)
        
        else:
            st.write("Erro ao fazer a requisição para a API")
    
    
    
elif menu == "Consulta CEP":
    st.subheader("Consulta CEP")

elif menu == "Cotação Dólar":
    st.subheader("Cotação Dólar")

elif menu == "Cotação Dólar":
    st.subheader("Cotação Dólar")
 
elif menu == "Monitoramento de ônibus":
    st.subheader("Monitoramento de ônibus")

else:
    st.subheader("Tópico não encontrado")

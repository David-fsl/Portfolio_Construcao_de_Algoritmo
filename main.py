import streamlit as st
import requests

st.set_page_config(page_title="Portfólio de Algoritmos", layout="centered")

st.title("Portfólio - Construção de Algoritmos")
st.write("Este aplicativo demonstra os conhecimentos adquiridos durante o semestre na disciplina Construção de Algoritmos.")


st.sidebar.header("Escolha um tema:")

menu = st.sidebar.radio(
    " ",
    (

        "Decisão e Repetição", 
        "Vetores e Matrizes", 
        "Funções e Bibliotecas", 
        "Registros", 
        "Arquivos em Disco", 
        "Recursividade", 
        "API Externa",
        "Big O",
        "Consulta CEP",
        "Cotação Dólar",
        
    )
)
#__________________________________________________________________________________________________________________________________
if menu == "Decisão e Repetição":
    st.subheader("Decisão e Repetição:")

    # Verificar se um número é par ou ímpar
    numero = st.number_input("Digite um número inteiro para verificar se é inpar ou par:", step=1, format="%d")
    if st.button("Verificar"):
        if numero % 2 == 0:
            st.write(f"O número {numero} é Par.")
        else:
            st.write(f"O número {numero} é Ímpar.")
    
    st.markdown("---")

    # Tabuada de multiplicação
    st.write("Tabuada de Multiplicação:")
    tabuada_numero = st.number_input("Digite um número inteiro para ver sua tabuada:", step=1, format="%d", value=5)
    if st.button("Gerar Tabuada"):
        st.write(f"Tabuada do {tabuada_numero}:")
        for i in range(1, 11):
            resultado = tabuada_numero * i
            st.write(f"{tabuada_numero} x {i} = {resultado}")
    # NOTA
    with st.expander("📑 - Nota sobre o exemplo de Decisão e Repetição:"):
        st.write(
            """
            - O primeiro exemplo utiliza uma estrutura condicional simples para determinar se um número é par ou ímpar.
            - O segundo exemplo utiliza um loop 'for' para gerar a tabuada de multiplicação de um número fornecido pelo usuário.
            - Ambos os exemplos demonstram conceitos básicos de decisão e repetição em programação.
            """
        )
#__________________________________________________________________________________________________________________________________


elif menu == "Vetores e Matrizes":
    st.subheader("Vetores e Matrizes:")

    tipo = st.radio("Escolha o tipo:", ["Vetor", "Matriz 2x2"], horizontal=True)

    # Vetor:
    
    if tipo == "Vetor":
        st.markdown("**Digite números separados por vírgula (ex.: 1, 2, 3, 4)**")
        texto = st.text_input("Vetor (lista):", value="1, 2, 3, 4, 5")

        if st.button("Calcular", key="btn_vetor"):
            try:
            # Aceita vírgula ou ponto e vírgula como separador
                itens = [x.strip() for x in texto.replace(";", ",").split(",")]
                vetor = [int(x) for x in itens if x != ""]

                if len(vetor) == 0:
                    st.warning("Digite pelo menos um número.")
                else:
                    st.write(f"**Vetor lido:** {vetor}")
                    st.write(f"**Tamanho:** {len(vetor)}")
                    st.write(f"**Soma:** {sum(vetor)}")
                    st.write(f"**Média:** {sum(vetor) / len(vetor):.2f}")
                    st.write(f"**Maior:** {max(vetor)}   |   **Menor:** {min(vetor)}")
                    st.write(f"**Ordenado (crescente):** {sorted(vetor)}")
            except ValueError:
                st.error("Entrada inválida. Use apenas números inteiros separados por vírgula.")
        with st.expander("📑 - Nota sobre o exemplo de Vetores:"):
            st.write(
                """
                - O exemplo lê uma lista de números inteiros fornecidos pelo usuário.
                - Calcula e exibe várias propriedades do vetor, como soma, média, maior e menor valor, e a versão ordenada do vetor.
                - Demonstra manipulação básica de listas (vetores) em Python.
                """
            )
    # Matriz 2x2:
    else:
        st.markdown("**Preencha os elementos da matriz A (2x2):**")
        c1, c2 = st.columns(2)
        with c1:
            a11 = st.number_input("a11", value=1, step=1, format="%d")
            a21 = st.number_input("a21", value=0, step=1, format="%d")
        with c2:
            a12 = st.number_input("a12", value=0, step=1, format="%d")
            a22 = st.number_input("a22", value=1, step=1, format="%d")

        if st.button("Calcular", key="btn_matriz"):
            A = [[a11, a12],
                [a21, a22]]

            # Transposta troca linhas por colunas
            AT = [[a11, a21],
            [a12, a22]]

            # Determinante 2x2: ad - bc
            det = a11 * a22 - a12 * a21

            st.markdown("**Matriz A:**")
            st.table(A)

            st.markdown("**Transposta Aᵀ:**")
            st.table(AT)

            st.markdown(f"**Determinante (det A):** `{det}`")
        
        with st.expander("📑 - Nota sobre o exemplo de Matrizes:"):
            st.write(
                """
                - O exemplo lê os elementos de uma matriz 2x2 fornecidos pelo usuário.
                - Calcula e exibe a transposta da matriz e o seu determinante.
                - Demonstra manipulação básica de matrizes em Python.
                """
            )
#__________________________________________________________________________________________________________________________________

elif menu == "Funções e Bibliotecas":
    st.subheader("Funções e Bibliotecas:")
    st.write("Exemplo de uso de funções e bibliotecas em Python:")
    # Importe de bibliotecas
    import math
    from datetime import date 
    from collections import Counter

    exemplo = st.radio(
        "Escolha o exemplo:", 
        ["Função - IMC", "Biblioteca padrão: datetime"], 
        horizontal=True, 
        key="fb_exemplo"
    )
    # Função - IMC
    if exemplo == "Função - IMC":
        st.markdown("**Exemplo de função com parâmetros, retorno e validação simples.**")
        
        def imc(peso: float, altura: float, casas: int = 2) -> float:
            
            """"
            Calcula o IMC = peso / altura^2.
            - peso: em kg
            - altura: em metros (não pode ser 0)
            - casas: casas decimais no arredondamento
            """
            if altura <= 0:
                raise ValueError("Altura deve ser maior que zero.")
            return round(peso / (altura ** 2), casas)
        col1, col2, col3 = st.columns(3)
        with col1:
            peso = st.number_input("Peso (kg):", min_value=0.0, value=70.0, step=0.1, format="%.1f", key="fb_imc_peso")   
        with col2:
            altura = st.number_input("Altura (m):", min_value=0.0, value=1.70, step=0.01, format="%.1f", key="fb_imc_altura")
        with col3:
            casas = st.number_input("Casas decimais:", min_value=0, max_value=5, value=2, step=1, format="%d", key="fb_imc_casas")
        
        if st.button("Calcular IMC", key="fb_imc_btn"):
            try:
                resultado = imc(peso, altura, casas)
                st.write(f"Seu IMC é: **{resultado}**")
            except ValueError as e:
                st.error(str(e))
        with st.expander("📑 - Nota sobre o exemplo de Funções:"):
            st.markdown(
                """
                - O exemplo define uma função `imc` que calcula o Índice de Massa Corporal (IMC) com validação de entrada.
                - Demonstra o uso de parâmetros, retorno de valores e tratamento de exceções em funções Python.
                """
            )
    # Biblioteca padrão: datetime
    else:
        st.markdown("**Calcular diferença de dias entre duas datas usando a biblioteca `datetime`.**")

        hoje = date.today()
        date1 = st.date_input("Data 1:", value=hoje.replace(day=1), key="fb_date1")
        date2 = st.date_input("Data 2:", value=hoje, key="fb_date2")

        if st.button("Calcular Diferença", key="fb_date_btn"):
            try:
                diferenca = abs((date2 - date1).days)
                st.write(f"A diferença entre {date1} e {date2} é de **{diferenca} dias**.")
            except Exception as e:
                st.error(f"Erro ao calcular a diferença: {str(e)}")
        with st.expander("📑 - Nota sobre o exemplo de Bibliotecas:"):
                st.markdown(
                    """
                    - O exemplo utiliza a biblioteca padrão `datetime` para manipulação de datas.
                    - Calcula a diferença em dias entre duas datas fornecidas pelo usuário.
                    - Demonstra o uso de bibliotecas padrão do Python para tarefas comuns.

                    """
                )
#__________________________________________________________________________________________________________________________________
    
elif menu == "Registros":
    st.subheader("Registros:")
    # Inicializa a lista de registros na sessão (uma vez)
    if "registros" not in st.session_state:
        st.session_state.registros = []

    # --- Formulário simples para criar um registro (aluno) ---
    with st.form("form_registro", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nome = st.text_input("Nome", key="reg_nome")
            curso = st.selectbox("Curso", ["Construção de Algoritmos", "Antropologia Cristã", "Interação Humano Computador", "Matemática Computacional"], key="reg_curso")
        with col2:
            idade = st.number_input("Idade", min_value=0, step=1, format="%d", key="reg_idade")
            ativo = st.checkbox("Ativo", value=True, key="reg_ativo")

        enviado = st.form_submit_button("Adicionar")
        if enviado:
            if not nome.strip():
                st.warning("Informe um nome.")
            else:
                registro = {
                    "nome": nome.strip(),
                    "idade": int(idade),
                    "curso": curso,
                    "ativo": ativo,
                }
                st.session_state.registros.append(registro)
                st.success(f"Registro de {registro['nome']} adicionado!")

    # --- Mostra registros + estatísticas simples ---
    if st.session_state.registros:
        st.markdown("**Registros cadastrados:**")
        st.dataframe(st.session_state.registros, use_container_width=True)

        # Estatísticas
        idades = [r["idade"] for r in st.session_state.registros if isinstance(r.get("idade"), (int, float))]
        total = len(st.session_state.registros)
        media = (sum(idades) / len(idades)) if idades else 0
        st.write(f"**Total:** {total} | **Média de idades:** {media:.1f}")

        # Filtro por curso (opcional)
        cursos_disponiveis = ["Todos"] + sorted({r["curso"] for r in st.session_state.registros})
        curso_filtro = st.selectbox("Filtrar por curso:", cursos_disponiveis, key="reg_filtro")
        if curso_filtro != "Todos":
            filtrados = [r for r in st.session_state.registros if r["curso"] == curso_filtro]
        else:
            filtrados = st.session_state.registros

        st.markdown("**Resultado do filtro:**")
        st.table(filtrados)

        # Limpar tudo (opcional)
        if st.button("Limpar todos os registros", key="reg_limpar"):
            st.session_state.registros.clear()
            st.info("Lista de registros esvaziada.")

    else:
        st.info("Nenhum registro ainda. Use o formulário acima para adicionar.")
    with st.expander("📑 - Nota sobre o exemplo de Registros:"):
        st.write(
            """
            - O exemplo utiliza uma lista de dicionários para armazenar registros de alunos.
            - Permite adicionar novos registros via formulário, exibir todos os registros em uma tabela e calcular estatísticas simples.
            - Demonstra manipulação básica de estruturas de dados (registros) em Python.
            """
        )       
#_____________________________________________________________________________________________________________

elif menu == "Arquivos em Disco":
    st.subheader("Arquivos em Disco")

    import os
    import pandas as pd

    exemplo = st.radio(
        "Escolha o exemplo:",
        ["Texto (.txt)", "CSV"],
        horizontal=True,
        key="arq_exemplo"
    )

    # ===================== TEXTO (.txt) =====================
    if exemplo == "Texto (.txt)":
        st.markdown("**Salvar e ler um arquivo .txt**")

        # pasta padrão onde salvaremos os arquivos
        pasta_padrao = "data"
        os.makedirs(pasta_padrao, exist_ok=True)

        nome = st.text_input("Nome do arquivo (sem extensão):", value="meu_texto", key="arq_txt_nome")
        conteudo = st.text_area("Conteúdo do arquivo:", "Olá, mundo!", height=120, key="arq_txt_conteudo")
        pasta = st.text_input("Pasta (relativa ao projeto):", value=pasta_padrao, key="arq_txt_pasta")

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Salvar .txt", key="arq_btn_salvar_txt"):
                caminho = os.path.join(pasta, f"{nome}.txt")
                os.makedirs(os.path.dirname(caminho), exist_ok=True)
                try:
                    with open(caminho, "w", encoding="utf-8") as f:
                        f.write(conteudo)
                    st.success(f"Arquivo salvo em `{caminho}`")
                except Exception as e:
                    st.error(f"Erro ao salvar: {e}")

        with col2:
            if st.button("Ler .txt", key="arq_btn_ler_txt"):
                caminho = os.path.join(pasta, f"{nome}.txt")
                if os.path.exists(caminho):
                    try:
                        with open(caminho, "r", encoding="utf-8") as f:
                            lido = f.read()
                        st.markdown("**Conteúdo lido:**")
                        st.code(lido, language="text")
                    except Exception as e:
                        st.error(f"Erro ao ler: {e}")
                else:
                    st.warning(f"Arquivo não encontrado em `{caminho}`")

        with st.expander("Como funciona (.txt)"):
            st.markdown(
                """
- **Salvar**: `open(caminho, "w", encoding="utf-8").write(conteudo)` cria/substitui o arquivo.
- **Ler**: `open(caminho, "r", encoding="utf-8").read()` retorna o texto.
- `os.path.join` monta caminhos portáveis; `os.makedirs(..., exist_ok=True)` garante a pasta.
                """
            )

    # ===================== CSV =====================
    elif exemplo == "CSV":
        st.markdown("**Ler (upload) e salvar CSV no disco**")
        os.makedirs("data", exist_ok=True)

        # ---- Upload e leitura do CSV ----
        up = st.file_uploader("Envie um arquivo CSV", type=["csv"], key="arq_csv_up")
        if up is not None:
            try:
                df = pd.read_csv(up)
                st.success("CSV lido com sucesso!")
                st.dataframe(df, use_container_width=True)

                if st.button("Salvar CSV enviado no disco", key="arq_btn_salvar_up"):
                    caminho_up = os.path.join("data", "upload.csv")
                    df.to_csv(caminho_up, index=False, encoding="utf-8")
                    st.info(f"Arquivo salvo em `{caminho_up}`")
            except Exception as e:
                st.error(f"Erro ao ler CSV: {e}")

        st.markdown("---")

        # ---- Gerar um CSV de exemplo ----
        st.markdown("**Gerar um CSV de exemplo**")
        df_ex = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

        col1, col2 = st.columns(2)
        with col1:
            if st.button("Salvar exemplo em disco", key="arq_btn_salvar_exemplo"):
                caminho_ex = os.path.join("data", "exemplo.csv")
                try:
                    df_ex.to_csv(caminho_ex, index=False, encoding="utf-8")
                    st.success(f"Exemplo salvo em `{caminho_ex}`")
                except Exception as e:
                    st.error(f"Erro ao salvar CSV: {e}")

        with col2:
            st.download_button(
                "Baixar exemplo.csv",
                df_ex.to_csv(index=False).encode("utf-8"),
                file_name="exemplo.csv",
                mime="text/csv",
                key="arq_btn_download_exemplo"
            )

        with st.expander("Como funciona (CSV)"):
            st.markdown(
                """
- **Ler** CSV: `pd.read_csv(uploaded_file)` já entende o arquivo enviado pelo `st.file_uploader`.
- **Salvar** CSV: `df.to_csv("data/arquivo.csv", index=False, encoding="utf-8")`.
- **Download** sem salvar: `st.download_button(..., df.to_csv(...).encode("utf-8"))`.
                """
            )
#__________________________________________________________________________________________________________________________________


elif menu == "Recursividade":
    st.subheader("Recursividade")

    exemplo = st.radio(
        "Escolha o exemplo:",
        ["Fatorial (n!)", "Fibonacci"],
        horizontal=True,
        key="rec_exemplo"
    )

    # --------------------- 1) Fatorial (n!) ---------------------
    if exemplo == "Fatorial (n!)":
        n = st.number_input("n (0 a 20)", min_value=0, max_value=20, value=5, step=1, format="%d", key="rec_fat_n")
        trace = st.checkbox("Mostrar rastro das chamadas (fat(k))", key="rec_fat_trace")

        if st.button("Calcular fatorial", key="rec_fat_btn"):
            chamadas = []

            def fat(k: int) -> int:
                if trace:
                    chamadas.append(f"fat({k})")
                if k == 0 or k == 1:          # CASO BASE
                    return 1
                return k * fat(k - 1)         # PASSO RECURSIVO

            resultado = fat(n)
            st.success(f"{n}! = {resultado}")
            if trace:
                st.code(" → ".join(chamadas), language="text")

            st.caption("Complexidade: tempo Θ(n) e espaço de pilha Θ(n).")

    # --------------------- 2) Fibonacci ---------------------
    elif exemplo == "Fibonacci":
        n = st.number_input("n (0 a 35 para recursivo puro)", min_value=0, max_value=50, value=10, step=1, format="%d", key="rec_fib_n")
        metodo = st.radio("Método", ["Recursivo puro", "Com memoization (rápido)"], horizontal=True, key="rec_fib_m")

        if st.button("Calcular Fibonacci", key="rec_fib_btn"):
            if metodo == "Recursivo puro":
                def fib(k: int) -> int:
                    if k <= 1:               # CASO BASES
                        return k
                    return fib(k - 1) + fib(k - 2)   # SUBPROBLEMAS
                res = fib(n)
                st.success(f"F({n}) = {res}")
                st.caption("Complexidade: tempo Θ(φ^n) (exponencial) e espaço Θ(n). Use para n pequeno.")
            else:
                from functools import lru_cache

                @lru_cache(maxsize=None)
                def fib(k: int) -> int:
                    if k <= 1:
                        return k
                    return fib(k - 1) + fib(k - 2)

                res = fib(n)
                st.success(f"F({n}) = {res}")
                st.caption("Complexidade: tempo Θ(n) e espaço Θ(n) (cache + pilha).")
    with st.expander("📑 - Nota sobre o exemplo de Recursividade:"):
        st.write(
            """
            - O exemplo do fatorial demonstra uma função recursiva simples com um caso base e um passo recursivo.
            - O exemplo de Fibonacci mostra tanto a implementação recursiva pura (ineficiente) quanto a otimizada com memoization usando `lru_cache`.
            - Ambos os exemplos ilustram conceitos fundamentais de recursividade em programação.
            """
        )


#__________________________________________________________________________________________________________________________________

elif menu == "API Externa":
    st.subheader("API Externa:")
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
    with st.expander("📑 - Nota sobre o exemplo de API Externa:"):
        st.write(
            """
            - O exemplo faz uma requisição HTTP para uma API pública que fornece fatos aleatórios.
            - Utiliza a biblioteca `requests` para realizar a chamada à API e processar a resposta JSON.
            - Demonstra como integrar APIs externas em aplicações Python.
            """
        )           
#__________________________________________________________________________________________________________________________________

elif menu == "Big O":
    st.subheader("Big O:")

    st.write("Visualize diferentes complexidades de tempo de algoritmos com base no tamanho da entrada.")

    import numpy as np
    import pandas as pd

    # Tamanhos de entrada
    n = np.linspace(1, 100, 100)

    # Funções de complexidade
    complexidades = {
        "O(1)": np.ones_like(n),
        "O(log n)": np.log(n),
        "O(n)": n,
        "O(n log n)": n * np.log(n),
        "O(n²)": n**2,
        "O(2ⁿ)": 2**(n / 10),  # reduzido para visualização
    }

    # Seleção de complexidades
    selecionadas = st.multiselect(
        "Escolha as complexidades para visualizar:",
        list(complexidades.keys()),
        default=["O(1)", "O(n)", "O(n²)"]
    )

    # Criar DataFrame para o gráfico
    df = pd.DataFrame({nome: complexidades[nome] for nome in selecionadas})
    df.index = n
    df.index.name = "Tamanho da entrada (n)"

    # Exibir gráfico
    st.line_chart(df)
    with st.expander("📑 - Nota sobre o exemplo de Big O:"):
        st.write(
            """
            - O exemplo visualiza diferentes classes de complexidade de tempo usando gráficos.
            - Permite aos usuários selecionar quais complexidades desejam comparar.
            - Ajuda a entender como o tempo de execução cresce com o aumento do tamanho da entrada.
            """
        )
#__________________________________________________________________________________________________________________________________

elif menu == "Consulta CEP":
    st.subheader("Consulta de CEP")

    cep = st.text_input("Digite o CEP (somente números):")

    if cep:
        if len(cep) == 8 and cep.isdigit():
            url = f"https://viacep.com.br/ws/{cep}/json/"
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
                if "erro" not in data:
                    st.success("CEP encontrado!")
                    st.write(f"📍 **Endereço:** {data['logradouro']}")
                    st.write(f"🏙️ **Bairro:** {data['bairro']}")
                    st.write(f"🌆 **Cidade:** {data['localidade']}")
                    st.write(f"🧭 **Estado:** {data['uf']}")
                else:
                    st.error("CEP não encontrado.")
            else:
                st.error("Erro ao consultar o CEP.")
        else:
            st.warning("Digite um CEP válido com 8 dígitos.")
#__________________________________________________________________________________________________________________________________

elif menu == "Cotação Dólar":
    st.subheader("Cotação do Dólar Comercial")

    import requests

    st.write("Confira abaixo a cotação atual do dólar.")
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial=@ini,dataFinalCotacao=@fim)?@ini='01-01-2000'&@fim='12-31-2100'&$top=1&$orderby=dataHoraCotacao%20desc&$format=json"
    res = requests.get(url)
    res = res.json()
    valor = res['value'][0]['cotacaoVenda']
    st.metric(label="💵 1 USD em BRL", value=f"R$ {valor:.4f}")
#__________________________________________________________________________________________________________________________________

else:
    st.subheader("Tópico não encontrado")


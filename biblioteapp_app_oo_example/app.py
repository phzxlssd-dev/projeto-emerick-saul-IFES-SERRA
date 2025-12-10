import streamlit as st
import pandas as pd
from src.services import SistemaService

service = SistemaService()

st.set_page_config(page_title="Sistema Acadêmico", layout="wide")
st.title("🎓 Sistema Acadêmico - Resultados dos Alunos")

menu = st.sidebar.selectbox(
    "Menu",
    ["Cadastrar Usuário", "Enviar Resultado CSV (Aluno)", "Consultar Resultados (Professor)"]
)

#---------------- CADASTRO ----------------
if menu == "Cadastrar Usuário":
    st.header("Cadastro de Usuários")

    tipo = st.selectbox("Tipo", ["Aluno", "Professor"])
    nome = st.text_input("Nome")
    email = st.text_input("E-mail")

    if st.button("Salvar"):
        if tipo == "Aluno":
            st.success(service.cadastrar_aluno(nome, email))
        else:
            st.success(service.cadastrar_professor(nome, email))


#---------------- UPLOAD ALUNO ----------------
elif menu == "Enviar Resultado CSV (Aluno)":
    st.header("Envio de Resultados - Aluno")

    aluno_nome = st.text_input("Nome do Aluno")
    arquivo = st.file_uploader("Envie seu arquivo CSV", type=["csv"])

    if arquivo and st.button("Enviar"):
        st.success(service.enviar_resultado_csv(aluno_nome, arquivo))
#---------------- CONSULTA PROFESSOR ----------------
elif menu == "Consultar Resultados (Professor)":
    st.header("Resultados Enviados pelos Alunos")

    resultados = service.listar_resultados()

    if resultados:
        data = [{
            "ID": r.id,
            "Aluno": r.aluno_nome,
            "Arquivo CSV": r.arquivo_csv
        } for r in resultados]

        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.divider()
        st.subheader("Visualizar Conteúdo do CSV")

        resultado_id = st.number_input("ID do Resultado", min_value=0, step=1)

        if st.button("Abrir CSV"):
            for r in resultados:
                if r.id == resultado_id:
                    df_csv = pd.read_csv(r.arquivo_csv)
                    st.dataframe(df_csv, use_container_width=True)

        st.divider()
        st.subheader("Remover Resultado")

        if st.button("Excluir Resultado"):
            st.success(service.remover_resultado(resultado_id))
            st.rerun()

    else:
        st.info("Nenhum resultado enviado ainda.")

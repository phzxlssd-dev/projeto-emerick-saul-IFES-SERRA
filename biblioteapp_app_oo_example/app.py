## app.py (apenas estrutura de cadastro)

import streamlit as st
from src.services import UsuarioService, ResultadoService

usuarios = UsuarioService()
resultados = ResultadoService()

menu = st.sidebar.selectbox("Menu", ["Cadastrar Aluno", "Cadastrar Professor", "Enviar CSV (Aluno)", "Ver Resultados (Professor)"])

if menu == "Cadastrar Aluno":
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    matricula = st.text_input("Matrícula")
    if st.button("Salvar"):
        usuarios.registrar_aluno(nome, email, matricula)
        st.success("Aluno cadastrado!")

elif menu == "Cadastrar Professor":
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    matricula = st.text_input("Matrícula do Professor")
    if st.button("Salvar"):
        usuarios.registrar_professor(nome, email, matricula)
        st.success("Professor cadastrado!")


# --- Consulta de resultados para Professor ---
if menu == "Ver Resultados (Professor)":
    st.header("Resultados dos Alunos")

    dados = resultados.repo.get_by_professor()

    for r in dados:
        resultado_id, aluno_id, nome_dp, tempo, valor, processado, comentario = r
        nome_aluno = usuarios.obter_nome(aluno_id)

        st.write(f"**Aluno:** {nome_aluno} (ID: {aluno_id})")
        st.write(f"Data Point: {nome_dp}")
        st.write(f"Tempo: {tempo}")
        st.write(f"Valor: {valor}")
        st.write(f"Processado: {processado}")
        st.write(f"Comentário: {comentario}")
        st.markdown("---")

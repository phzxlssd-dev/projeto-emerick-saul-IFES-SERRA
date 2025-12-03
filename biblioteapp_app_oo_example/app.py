import streamlit as st
import pandas as pd
from src.services import LibraryService

# Instancia o serviço (Controller)
service = LibraryService()

st.set_page_config(page_title="Gestão de Biblioteca", layout="wide")
st.title("📚 Sistema de Gestão de Biblioteca")

# Menu lateral para navegação
menu = st.sidebar.selectbox("Menu", ["Cadastrar Livro", "Consultar Acervo"])

if menu == "Cadastrar Livro":
    st.header("Novo Cadastro")
    
    with st.form("book_form", clear_on_submit=True):
        title = st.text_input("Título do Livro")
        author = st.text_input("Autor")
        year = st.number_input("Ano de Publicação", min_value=1000, max_value=2100, step=1)
        submitted = st.form_submit_button("Salvar Livro")

        if submitted:
            result = service.register_book(title, author, year)
            if "Erro" in result:
                st.error(result)
            else:
                st.success(result)

elif menu == "Consultar Acervo":
    st.header("Acervo Disponível")
    
    books = service.list_books()
    
    if books:
        # Convertendo objetos para DataFrame para exibição bonita
        data = [{
            "ID": b.id, 
            "Título": b.title, 
            "Autor": b.author, 
            "Ano": b.year, 
            "Status": b.status
        } for b in books]
        
        df = pd.DataFrame(data)
        st.dataframe(df, use_container_width=True, hide_index=True)

        st.divider()
        st.subheader("Gerenciar")
        
        # Opção de exclusão
        col1, col2 = st.columns([3, 1])
        with col1:
            id_to_delete = st.number_input("ID do livro para remover", min_value=0, step=1)
        with col2:
            st.write("") # Espaçamento
            st.write("") 
            if st.button("Remover Livro"):
                service.remove_book(id_to_delete)
                st.rerun() # Atualiza a tela
    else:
        st.info("Nenhum livro cadastrado no sistema.")
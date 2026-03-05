import streamlit as st
import os
from datetime import datetime

# Criar pasta principal de uploads
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.title("Cadastro e Upload de Voo - Parapente")

# Formulário de cadastro e upload
with st.form("cadastro_voo"):
    st.header("Cadastro do Piloto")
    nome = st.text_input("Nome do Piloto")
    parapente = st.text_input("Nome do Parapente / Equipe")
    arquivo_igc = st.file_uploader("Enviar arquivo IGC", type=["igc"])
    enviar = st.form_submit_button("Enviar Voo")

if enviar:
    if not nome or not parapente or not arquivo_igc:
        st.error("Preencha todos os campos e envie o arquivo IGC!")
    else:
        # Criar pasta do piloto
        pasta_piloto = os.path.join(UPLOAD_DIR, nome.replace(" ", "_"))
        if not os.path.exists(pasta_piloto):
            os.makedirs(pasta_piloto)

        # Salvar arquivo IGC com timestamp para não sobrescrever
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"{timestamp}_{arquivo_igc.name}"
        caminho_arquivo = os.path.join(pasta_piloto, nome_arquivo)

        with open(caminho_arquivo, "wb") as f:
            f.write(arquivo_igc.getbuffer())

        st.success(f"Arquivo enviado com sucesso! Salvo em: {caminho_arquivo}")
        st.info(f"Piloto: {nome} | Parapente: {parapente}")
        
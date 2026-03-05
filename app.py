import streamlit as st
import os
from datetime import datetime

# Criar pasta principal de uploads
UPLOAD_DIR = "uploads"
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

st.title("🪂 Copa Castelo 2026 - Envio de Voos")

# Formulário de cadastro e upload
with st.form("cadastro_voo"):
    st.header("Cadastro do Piloto")
    nome = st.text_input("Nome do Piloto")
    parapente = st.text_input("Nome do Parapente")
   arquivo_igc = st.file_uploader(
    "Enviar arquivo de voo (.igc)",
    accept_multiple_files=False
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
        from datetime import datetime
import os

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

if enviar:
    if not nome or not arquivo_igc:
        st.error("Preencha o nome e envie o voo")
    else:

        piloto_dir = os.path.join(UPLOAD_DIR, nome.replace(" ","_"))

        if not os.path.exists(piloto_dir):
            os.makedirs(piloto_dir)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        nome_final = f"{nome}_{timestamp}_{arquivo_igc.name}"

        caminho = os.path.join(piloto_dir, nome_final)

        with open(caminho, "wb") as f:
            f.write(arquivo_igc.getbuffer())

        st.success("Voo enviado com sucesso!")

        

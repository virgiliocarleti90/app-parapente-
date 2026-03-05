import streamlit as st
import os
from datetime import datetime

st.title("🪂 Copa Castelo 2026 - Envio de Voos")

UPLOAD_DIR = "uploads"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

with st.form("cadastro_voo"):

    nome = st.text_input("Nome do piloto")
    parapente = st.text_input("Parapente")

    arquivo_igc = st.file_uploader(
        "Enviar arquivo de voo (.igc)",
        accept_multiple_files=False
    )

    enviar = st.form_submit_button("Enviar voo")

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
   


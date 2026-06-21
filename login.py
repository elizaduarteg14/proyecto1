import streamlit as st
from config.conexion import conectar

def login():

    st.title("🔐 Sistema de Login")

    # Usamos form para permitir ENTER
    with st.form("login_form"):

        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        submit = st.form_submit_button("Ingresar")

        if submit:

            conn = conectar()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT * FROM usuario WHERE usuario=%s AND password=%s",
                (usuario, password)
            )

            resultado = cursor.fetchone()

            conn.close()

            if resultado:
                st.session_state["login"] = True
                st.rerun()
            else:
                st.error("Credenciales incorrectas")
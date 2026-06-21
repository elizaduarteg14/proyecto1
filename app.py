# import streamlit as st
#from login import login
#from modulos.clientes import clientes
#from modulos.productos import productos
#from modulos.ventas import ventas

# ---------------- SESIÓN ----------------
#if "login" not in st.session_state:
    st.session_state["login"] = False

# ---------------- LOGIN ----------------
if not st.session_state["login"]:
    login()

# ---------------- SISTEMA ----------------
else:

    st.sidebar.title("📋 Menú")

    opcion = st.sidebar.selectbox(
        "Ir a:",
        ["Inicio", "Clientes", "Productos", "Ventas"]
    )

    if opcion == "Inicio":
        st.title("🏠 Bienvenido al sistema")

        if st.button("Cerrar sesión"):
            st.session_state["login"] = False
            st.rerun()

    elif opcion == "Clientes":
        clientes()

    elif opcion == "Productos":
        productos()

    elif opcion == "Ventas":
        ventas()

import streamlit as st
from config.conexion import conectar

def ventas():

    st.title("💰 Gestión de Ventas")

    # ---------------- INSERTAR ----------------
    st.subheader("Registrar venta")

    cliente = st.text_input("Cliente")
    producto = st.text_input("Producto")
    cantidad = st.number_input("Cantidad", min_value=1)

    if st.button("Guardar venta"):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO ventas(cliente, producto, cantidad) VALUES (%s, %s, %s)",
            (cliente, producto, cantidad)
        )

        conn.commit()
        conn.close()

        st.success("Venta registrada con exito")

    st.divider()

    # ---------------- MOSTRAR ----------------
    st.subheader("Lista de ventas")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM ventas")
    datos = cursor.fetchall()

    conn.close()

    for d in datos:
        st.write(f"ID: {d[0]} | Cliente: {d[1]} | Producto: {d[2]} | Cantidad: {d[3]}")
import streamlit as st
from config.conexion import conectar

def productos():

    st.title("📦 Gestión de Productos")

    # ---------------- INSERTAR ----------------
    st.subheader("➕ Agregar producto")

    nombre = st.text_input("Nombre del producto")
    precio = st.number_input("Precio", min_value=0.0, format="%.2f")
    stock = st.number_input("Stock", min_value=0)
    
    if st.button("Guardar producto"):

        if nombre and precio:

            conn = conectar()
            cursor = conn.cursor()

            cursor.execute(
    "INSERT INTO productos(nombre, precio, stock) VALUES (%s, %s, %s)",
    (nombre, precio, stock)
)

            conn.commit()
            conn.close()

            st.success("Producto guardado 🎉")
            st.rerun()

        else:
            st.warning("Completa todos los campos")

    st.divider()

    # ---------------- MOSTRAR ----------------
    st.subheader("📋 Lista de productos")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()

    conn.close()

    for d in datos:
        st.write(f"ID: {d[0]} | Nombre: {d[1]} | Precio: ${d[2]}")

    st.divider()

    # ---------------- ELIMINAR ----------------
    st.subheader("🗑️ Eliminar producto")

    id_delete = st.number_input("ID a eliminar", min_value=1, step=1)

    if st.button("Eliminar producto"):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM productos WHERE id=%s", (id_delete,))

        conn.commit()
        conn.close()

        st.success("Producto eliminado 🗑️")
        st.rerun()

    st.divider()

    # ---------------- EDITAR ----------------
    st.subheader("✏️ Editar producto")

    id_edit = st.number_input("ID a editar", min_value=1, step=1)

    nuevo_nombre = st.text_input("Nuevo nombre del producto")
    nuevo_precio = st.number_input("Nuevo precio", min_value=0.0, format="%.2f")

    if st.button("Actualizar producto"):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE productos 
            SET nombre=%s, precio=%s 
            WHERE id=%s
            """,
            (nuevo_nombre, nuevo_precio, id_edit)
        )

        conn.commit()
        conn.close()

        st.success("Producto actualizado ✏️")
        st.rerun()

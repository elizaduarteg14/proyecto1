import streamlit as st
from config.conexion import conectar

def clientes():

    st.title("👤 Gestión de Clientes")

    # ---------------- INSERTAR ----------------
    st.subheader("➕ Agregar cliente")

    nombre = st.text_input("Nombre")
    telefono = st.text_input("Teléfono")
    correo = st.text_input("Correo")

    if st.button("Guardar cliente"):

        if nombre and telefono and correo:

            conn = conectar()
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO clientes(nombre, telefono, correo) VALUES (%s, %s, %s)",
                (nombre, telefono, correo)
            )

            conn.commit()
            conn.close()

            st.success("Cliente guardado 🎉")
            st.rerun()

        else:
            st.warning("Completa todos los campos")

    st.divider()

    # ---------------- MOSTRAR ----------------
    st.subheader("📋 Lista de clientes")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM clientes")
    datos = cursor.fetchall()

    conn.close()

    for d in datos:
        st.write(f"ID: {d[0]} | Nombre: {d[1]} | Tel: {d[2]} | Correo: {d[3]}")

    st.divider()

    # ---------------- ELIMINAR ----------------
    st.subheader("🗑️ Eliminar cliente")

    id_delete = st.number_input("ID a eliminar", min_value=1, step=1)

    if st.button("Eliminar"):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM clientes WHERE id=%s", (id_delete,))

        conn.commit()
        conn.close()

        st.success("Cliente eliminado 🗑️")
        st.rerun()

    st.divider()

    # ---------------- EDITAR (NUEVO) ----------------
    st.subheader("✏️ Editar cliente")

    id_edit = st.number_input("ID a editar", min_value=1, step=1)

    nuevo_nombre = st.text_input("Nuevo nombre")
    nuevo_telefono = st.text_input("Nuevo teléfono")
    nuevo_correo = st.text_input("Nuevo correo")

    if st.button("Actualizar"):

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE clientes 
            SET nombre=%s, telefono=%s, correo=%s 
            WHERE id=%s
            """,
            (nuevo_nombre, nuevo_telefono, nuevo_correo, id_edit)
        )

        conn.commit()
        conn.close()

        st.success("Cliente actualizado ✏️")
        st.rerun()
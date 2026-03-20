import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Household OS", page_icon="🏠")

st.title("🏠 Household OS")

# Conexión
conn = st.connection("gsheets", type=GSheetsConnection)

# Menú lateral
menu = st.sidebar.selectbox("Módulo", ["📋 Tareas Diarias", "🍲 Comidas", "💰 Finanzas"])

if menu == "📋 Tareas Diarias":
    st.header("Checklist de Operaciones")
    try:
        # Intentamos leer la pestaña "Tareas"
        df_tareas = conn.read(worksheet="Tareas", ttl="0") # ttl=0 para que siempre refresque datos
        
        if not df_tareas.empty:
            for index, row in df_tareas.iterrows():
                # Mostramos la tarea
                st.checkbox(f"{row['Hora']} - {row['Tarea']}", key=f"t_{index}")
        else:
            st.warning("El Excel está vacío. Agrega tareas en la pestaña 'Tareas'.")
            
    except Exception as e:
        st.error("❌ No se pudo leer la pestaña 'Tareas'")
        st.info("Asegúrate de que la pestaña abajo en tu Excel se llame exactamente 'Tareas' (con T mayúscula y sin espacios).")
        st.exception(e)

elif menu == "🍲 Comidas":
    st.header("Plan de Comidas")
    try:
        df_comidas = conn.read(worksheet="Comidas", ttl="0")
        st.dataframe(df_comidas, use_container_width=True)
    except:
        st.error("Error al cargar la pestaña 'Comidas'. Revisa el nombre en el Excel.")

elif menu == "💰 Finanzas":
    st.header("Finanzas")
    st.info("Módulo en desarrollo. Pronto podrás registrar gastos aquí.")

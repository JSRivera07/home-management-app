import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Household OS", page_icon="🏠")

# --- CONEXIÓN A GOOGLE SHEETS ---
conn = st.connection("gsheets", type=GSheetsConnection)

# Leer datos de las pestañas
df_tareas = conn.read(worksheet="Tareas")
df_comidas = conn.read(worksheet="Comidas")

st.title("🏠 Household OS")
menu = st.sidebar.selectbox("Módulo", ["📋 Tareas Diarias", "🍲 Comidas", "💰 Finanzas"])

if menu == "📋 Tareas Diarias":
    st.header("Checklist de Operaciones")
    
    # Mostrar tareas desde el Excel
    for index, row in df_tareas.iterrows():
        check = st.checkbox(f"{row['Hora']} - {row['Tarea']}", value=(row['Estado'] == 'Hecho'), key=f"task_{index}")
        
        # Si el estado cambia, podrías implementar una función para actualizar el Excel aquí
        # Por ahora, esto lee lo que pongas manualmente en el Excel

elif menu == "🍲 Comidas":
    st.header("Menú Semanal")
    st.table(df_comidas)
    
    with st.expander("📝 Editar Menú"):
        nuevo_desayuno = st.text_input("Nuevo Desayuno")
        if st.button("Actualizar"):
            st.success("Dato listo para enviarse al Excel")

elif menu == "💰 Finanzas":
    st.header("Gastos")
    st.info("Conectando con la pestaña de Finanzas...")

import streamlit as st
import pandas as pd

# Configuración de página
st.set_page_config(page_title="Household OS", page_icon="🏠", layout="wide")

# ID de tu Google Sheet (Sacado de tu link)
SHEET_ID = "182qzbStN9L4Dxv-Vo423LVRPfG5evUlopVToTYBUUOA"

# Función para leer pestañas de forma segura
def cargar_datos(pestaña):
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={pestaña}"
    return pd.read_csv(url)

st.title("🏠 Household OS")

# Menú lateral
menu = st.sidebar.selectbox("Módulo", ["📋 Tareas Diarias", "🍲 Comidas", "💰 Finanzas"])

try:
    if menu == "📋 Tareas Diarias":
        st.header("Checklist de Operaciones")
        df_tareas = cargar_datos("Tareas")
        
        if not df_tareas.empty:
            # Mostramos progreso
            total = len(df_tareas)
            st.write(f"Tareas totales para hoy: **{total}**")
            
            for index, row in df_tareas.iterrows():
                # Creamos el checklist
                st.checkbox(f"{row['Hora']} - {row['Tarea']}", key=f"t_{index}")
        else:
            st.warning("Agregue tareas en la pestaña 'Tareas' de su Excel.")

    elif menu == "🍲 Comidas":
        st.header("Menú de la Semana")
        df_comidas = cargar_datos("Comidas")
        st.dataframe(df_comidas, use_container_width=True)

    elif menu == "💰 Finanzas":
        st.header("Control de Gastos")
        df_finanzas = cargar_datos("Finanzas")
        st.metric("Balance Mensual Estimado", "$1,200") # Placeholder
        st.dataframe(df_finanzas)

except Exception as e:
    st.error("⚠️ Error de conexión")
    st.info("Asegúrate de que los nombres de las pestañas en el Excel sean exactamente: Tareas, Comidas y Finanzas.")

import streamlit as st
import pandas as pd

st.set_page_config(page_title="Household OS", page_icon="🏠", layout="wide")

# --- INTERFAZ ---
st.title("🏠 Household OS")
menu = st.sidebar.selectbox("Módulo", ["📋 Tareas Diarias", "🍲 Plan de Comidas", "💰 Finanzas"])

# --- MÓDULO TAREAS ---
if menu == "📋 Tareas Diarias":
    st.header("Checklist de Operaciones")
    
    # Lista basada en tu rutina real
    tasks_data = [
        {"Hora": "07:30 AM", "Actividad": "Preparar shot digestivo"},
        {"Hora": "07:40 AM", "Actividad": "Preparar café"},
        {"Hora": "07:50 AM", "Actividad": "Preparar desayuno"},
        {"Hora": "08:25 AM", "Actividad": "Estación de Salida (Revisar pertenencias)"},
        {"Hora": "09:30 AM", "Actividad": "Paseo con Kaiser (20 min)"},
        {"Hora": "10:15 AM", "Actividad": "Inicio preparación Lunch"},
        {"Hora": "01:40 PM", "Actividad": "Bloque de Tarea Pesada (Limpieza)"},
        {"Hora": "03:10 PM", "Actividad": "Preparar Snack"},
        {"Hora": "05:00 PM", "Actividad": "Workout"}
    ]
    
    for t in tasks_data:
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            st.checkbox("", key=t['Actividad'])
        with col2:
            st.write(f"**{t['Hora']}** - {t['Actividad']}")

# --- MÓDULO COMIDAS ---
elif menu == "🍲 Plan de Comidas":
    st.header("Dashboard del Chef")
    cat = st.selectbox("Categoría", ["Parrilla/Sartén", "Frescos/Ligeros", "Healthy Comfort", "Del Mar"])
    
    if cat == "Parrilla/Sartén":
        st.write("- Carne asada / Pollo parrilla\n- Bisteck ranchero\n- Pavo Flaco")
    elif cat == "Del Mar":
        st.write("- Pescado a la plancha\n- Salmón en Airfryer\n- Tacos Ensenada (Airfryer)")
    
    st.text_input("Sugerencia de nueva receta:")
    if st.button("Guardar en Lista de Compras"):
        st.success("Agregado al inventario")

# --- MÓDULO FINANZAS ---
elif menu == "💰 Finanzas":
    st.header("Presupuesto Mensual")
    st.metric("Balance Disponible", "$1,200", "-$50 hoy")
    with st.expander("Registrar Gasto Diario"):
        st.date_input("Fecha")
        st.number_input("Monto", min_value=0.0)
        st.selectbox("Categoría", ["Súper", "Renta/Servicios", "Kaiser", "Ocio"])
        st.button("Guardar Gasto")

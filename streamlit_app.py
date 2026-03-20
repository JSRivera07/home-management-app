import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Household OS", layout="wide")

# --- ESTILOS ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🏠 Household OS")
st.sidebar.title("Módulos")
menu = st.sidebar.radio("Ir a:", ["📋 Tareas", "🍲 Comidas", "💰 Finanzas"])

# --- DATOS DE EJEMPLO (Luego conectaremos tu Google Sheet) ---
if 'tasks' not in st.session_state:
    st.session_state.tasks = [
        {"hora": "07:30 AM", "tarea": "Shot digestivo", "done": False},
        {"hora": "07:40 AM", "tarea": "Preparar café", "done": False},
        {"hora": "08:25 AM", "tarea": "Revisar pertenencias esposa", "done": False},
        {"hora": "09:30 AM", "tarea": "Paseo con Kaiser", "done": False},
        {"hora": "05:00 PM", "tarea": "Workout", "done": False}
    ]

# --- MÓDULO TAREAS ---
if menu == "📋 Tareas":
    st.header("Checklist Diaria")
    
    # Progreso
    total = len(st.session_state.tasks)
    completas = sum(1 for t in st.session_state.tasks if t['done'])
    progreso = completas / total
    st.progress(progreso)
    st.write(f"Progreso del día: **{int(progreso*100)}%**")

    # Lista de tareas
    for i, item in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.1, 0.9])
        with col1:
            st.session_state.tasks[i]['done'] = st.checkbox("", value=item['done'], key=f"check_{i}")
        with col2:
            texto = f"**{item['hora']}** - {item['tarea']}"
            if st.session_state.tasks[i]['done']:
                st.write(f"~~{texto}~~ ✅")
            else:
                st.write(texto)

# --- MÓDULO COMIDAS ---
elif menu == "🍲 Comidas":
    st.header("Planificación de Comidas")
    st.info("Aquí conectaremos tu lista de recetas y el calendario semanal.")
    # Placeholder para el siguiente paso

# --- MÓDULO FINANZAS ---
elif menu == "💰 Finanzas":
    st.header("Control de Gastos")
    st.write("Presupuesto Mensual: **$X,XXX**")
    # Placeholder para el siguiente paso

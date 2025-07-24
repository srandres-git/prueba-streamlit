import streamlit as st
import pandas as pd
import io
CUENTAS = {
    'Banamex': ['828','829','434'],
    'Santander': ['383','357'],
    'HSBC': ['019','455'],
    'BBVA': ['389','844'],
    'Banorte': ['858'],
    'PNC': ['865']
}
st.title("Asignador de Claves de Estado de Cuenta")

# Sidebar
bank = st.sidebar.selectbox("Selecciona banco", list(CUENTAS.keys()))
cuentas = CUENTAS[bank]
account = st.sidebar.selectbox("Selecciona cuenta", cuentas)

def get_cta():
    st.markdown(f"{bank},{account}")

uploaded_files = st.file_uploader(
    "Arrastra uno o más archivos de estados de cuenta",
    type=['csv', 'xlsx', 'txt'],
    accept_multiple_files=True,
    on_change=get_cta
)
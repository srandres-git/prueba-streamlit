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
st.title("Prueba conciliación")

# # Sidebar
# bank = st.sidebar.selectbox("Selecciona banco", list(CUENTAS.keys()))
# cuentas = CUENTAS[bank]
# account = st.sidebar.selectbox("Selecciona cuenta", cuentas)

st.title("Arrastra los estados de cuenta")
uploaded_files = {}
for banco, cuentas in CUENTAS.items():
    st.markdown(f"**{banco}**")
    for cuenta in cuentas:
        uploaded_files[(banco,cuenta)] = st.file_uploader(
            f"Cuenta {cuenta}",
            type=['csv', 'xlsx', 'txt'],
            accept_multiple_files=False
        )
if uploaded_files:
    for (banco,cuenta), file in uploaded_files.items():
        if file:
            st.markdown(f'archivo subido de {banco} {cuenta}')

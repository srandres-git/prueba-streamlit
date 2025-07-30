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

st.header("Arrastra los estados de cuenta")
uploaded_files = {}
# Creamos las tabs por banco
tabs = st.tabs(CUENTAS.keys())
tab_dict = {banco: t for banco in CUENTAS.keys() for t in tabs}
# Creamos las columnas contenedor
cols = {(b,c):None for b,ctas in CUENTAS.items() for c in ctas}
for banco, cuentas in CUENTAS.items():
    with tab_dict[banco]:
        col_list = st.columns(len(cuentas))
        for i,cuenta in enumerate(cuentas):
            cols[(banco,cuenta)]= col_list[i]
# Agregamos los widget para arrastrar el archivo
for banco, cuentas in CUENTAS.items():
    for cuenta in cuentas:
        uploaded_files[(banco,cuenta)] = cols[(banco,cuenta)].file_uploader(
            f"Cuenta {cuenta}",
            type=['csv', 'xlsx', 'txt'],
            accept_multiple_files=False,
        )
if uploaded_files:
    for (banco,cuenta), file in uploaded_files.items():
        if file:
            cols[(banco,cuenta)].markdown(f'archivo subido de {banco} {cuenta}')

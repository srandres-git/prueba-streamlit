import streamlit as st
import pandas as pd
st.title("Pruebas de Streamlit")

st.write(f'Secreto: {st.secrets["my_secret"]}')
# imprimimos la tabla 'ejecutivos_cxp' del secreto
ejecutivos_cxp = st.secrets["ejecutivos_cxp"]
df = pd.DataFrame(ejecutivos_cxp)
st.write("Tabla 'ejecutivos_cxp':")
import streamlit as st
st.title("Pruebas de Streamlit")

st.write(f'Secreto: {st.secrets["my_secret"]}')
# imprimimos la tabla 'ejecutivos_cxp' del secreto
st.write(st.secrets["ejecutivos_cxp"])
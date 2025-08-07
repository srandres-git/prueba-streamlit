import streamlit as st
st.title("Pruebas de Streamlit")

st.write(f'Secreto: {st.secrets["my_secret"]}')
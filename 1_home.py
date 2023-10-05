import streamlit as st
import pandas as pd
st.title("Controle Infra")
df_data = pd.read_csv("datasets/relatorios.xlsx", index_col=0)
df_data
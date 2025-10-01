import streamlit as st
import pandas  as pd
import seaborn as sns
import plotly.express as px

st.title('CFB  MODEL')

df = pd.read_csv('cfbdata.csv')

opts = df.columns.tolist()

col1, col2 = st.columns(2)

choice = st.multiselect(opts)

fig = sns.heatmap(df[choice].corr())

st.figure(fig)

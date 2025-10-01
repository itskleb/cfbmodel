import streamlit as st
import pandas  as pd
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt

st.title('CFB  MODEL')

df = pd.read_csv('cfbdata.csv')

opts = df.columns.tolist()

col1, col2 = st.columns(2)

choice = st.multiselect(label='Choose Columns',options=opts)

fig, ax = plt.subplots()

sns.heatmap(df[choice].corr(),ax=ax)

st.pyplot(fig=fig)

import streamlit as st
import pandas as pd
import duckdb

data = {"Nom": ("Rafael", "Jean", "Pierre"),
        "Anniversaire": ("2000", "1995", "1968"),
        "Ville": ("Paris", "Lyon", "Toulouse")}

df = pd.DataFrame(data)
st.write("Dataframe : df")
st.dataframe(df)


query = st.text_area(label="sql_query",
                     label_visibility="hidden",
                     height=3)

try:
    res = duckdb.sql(query).df()
    st.dataframe(res)
except AttributeError:
    st.write("waiting for query ...")

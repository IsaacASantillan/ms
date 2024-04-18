import streamlit as st 
import pandas as pd
import numpy as np
from textfileparser import df
from ast import literal_eval 
import seaborn as sns
import plotly.express as px 
import plotly.graph_objects as go

st.write("""
    # Mass Spectral Database
    """)
""""""


def dataframeselection(df):
    ed = st.data_editor(df, column_config={"Select": st.column_config.CheckboxColumn(default=False)})
    selected_rows = ed[ed["Select"]]
    return selected_rows.drop('Select', axis=1)
 
    
def create_graph(df):
    dat = []
    for index, row in df.iterrows():
        go.Scatter(x=literal_eval(row["X-Values"]), y = literal_eval(row["Y-Values"]), name = row["Name"])
        dat.append(go.Scatter(x=literal_eval(row["X-Values"]), y = literal_eval(row["Y-Values"]), name = row["Name"]))
    fig = go.Figure(data = dat, layout = {"xaxis": {"title": "x axis"}, "yaxis": {"title": "y axis"}, "title": "Mass Spec"})
    return fig

def filter_graph(df):
    st.slider

selection = dataframeselection(df)
st.write("Your selection:")
st.write(selection)
buttonclicked = st.sidebar.button('Scatterplot')
if buttonclicked:
    st.write(create_graph(selection))
    
a = st.sidebar.slider("Double Ended", value=[0,1000])
selmin, selmax = a






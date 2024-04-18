import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from ast import literal_eval 
import seaborn as sns

gsheetid = "158IXsTDTJc3Z2q3Nm-lCw6kE2-JxGAsWOvzKF-ec1-4"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
df = pd.read_csv(gsheet_url, engine="pyarrow")

st.write("""
    # Mass Spectral Database
    """)
""""""

def dataframeselection(df):
    ed = st.data_editor(df, column_config={"Select": st.column_config.CheckboxColumn(default=False)})
    selected_rows = ed[ed["Select"]]
    return selected_rows.drop('Select', axis=1)


selection = dataframeselection(df)
st.write("Your selection:")
st.write(selection)
buttonclicked = st.button('Scatterplot')
if buttonclicked:
    plt.xticks(np.arange(0, 400, step=15))
    for index, row in selection.iterrows():
        scatterplot = plt.scatter(x=literal_eval(row["X-Values"]), y=literal_eval(row["Y-Values"])).figure
    st.pyplot(scatterplot)
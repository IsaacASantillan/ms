import pandas as pd
import pyarrow





gsheetid = "158IXsTDTJc3Z2q3Nm-lCw6kE2-JxGAsWOvzKF-ec1-4"
sheet_name = "Data"
gsheet_url = "https://docs.google.com/spreadsheets/d/{}/gviz/tq?tqx=out:csv&sheet={}".format(gsheetid, sheet_name)
df = pd.read_csv(gsheet_url, engine="pyarrow")

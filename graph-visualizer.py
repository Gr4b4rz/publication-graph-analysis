# PRESUMABLY TO BE USED LATER ON

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.read_csv('publications.csv')
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = dash_table.DataTable(
    id='table',
    columns=[{"name": i, "id": i} for i in df.columns],
    data=df.to_dict('records'),
)

if __name__ == '__main__':
    app.run_server(debug=True, port=8000)

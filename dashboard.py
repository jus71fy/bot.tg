# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/jus71fy/bot.tg/refs/heads/master/data.csv')
# Initialize the app
app = Dash(__name__)


# App layout
app.layout = html.Div([
    html.Div(children='Фотостудия'),
    html.Hr(),
    dcc.RadioItems(options=['Дата', 'Имя'], value='Зал', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=10),
    dcc.Graph(figure={}, id='controls-and-graph'),
    dcc.Graph(figure=px.pie(df, values='Стоимость', names='Зал')),
    dcc.Graph(figure=px.bar(df, x='Имя', y='Время'))
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df, x='Номер', y=col_chosen, histfunc='avg')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
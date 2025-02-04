import dash
import dash_html_components as html
import dash_core_components as dcc 

from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets= external_stylesheets)

app.layout = html.Div([
    dcc.Tabs(id="tabs", value = 'tab-1', children = [
        dcc.Tab(label = 'tab one', value = 'tab-1'),
        dcc.Tab(label = 'tab two', value = 'tab-2')
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
[Input('tabs', 'value')])
def render_content(tab):
    if tab == "tab-1":
        return html.Div([
            html.H3('tab content 1')
        ])
        # "do this"
    elif tab == "tab-2":
        return html.Div([
            html.H3('tab content 2')
        ])
        # do that


if __name__ == "__main__":
    app.run_server(debug = True)
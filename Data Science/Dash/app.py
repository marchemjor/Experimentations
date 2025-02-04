
import dash
import dash_html_components as html
import dash_core_components as dcc
from assets import patient_demographics, patient_med_readmit
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
colors = {"background": "#F3F6FA", "background_div": "white", 'text': '#009999'}
app.config['suppress_callback_exceptions']= True

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1('Patient Data Dashboard', style={
            'textAlign': 'center',
            'color': colors['text']
        }),

      dcc.Tabs(id="tabs", className="row", style={"margin": "2% 3%","height":"20","verticalAlign":"middle"}, value='med_tab', children=[
        dcc.Tab(label='Summary of Patients in the Hospital', value='dem_tab'),
        dcc.Tab(label='Morbidity, deaths and Healthcare acquired  infections(HAI)', value='med_tab')
        # dcc.Tab(label='Re-admissions', value='readmit_tab')
    ]),
    html.Div(id='tabs-content')
])

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'dem_tab':
        return patient_demographics.tab_1_layout
    elif tab == 'med_tab':
        return patient_med_readmit.tab_2_layout
if __name__ == '__main__':
    app.run_server(port=8000)

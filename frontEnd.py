import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from pandas import ExcelWriter
from PIL import Image
from Person import Person
from Group import Group
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

niya = Person("Niya", 8000, "60 Minutes", 20, 120, "60 Mins", "10%")
kelly = Person("Kelly", 6000, "60 Minutes", 17, 120, "60 Mins", "10%")
laurie = Person("Laurie", 9000, "60 Minutes", 23, 120, "60 Mins", "10%")
gauri = Person("Gauri", 5000, "60 Minutes", 15, 120, "60 Mins", "10%")
mary = Person("Mary", 4000, "60 Minutes", 12, 120, "60 Mins", "10%")

friends = [niya, kelly, laurie, gauri, mary]
ourGroup = Group(friends, 0, 0)

stepsData = pd.DataFrame({
    "Person": [niya.name, kelly.name, laurie.name, gauri.name, mary.name],
    "Average Weekly Steps": [niya.steps, kelly.steps, laurie.steps, gauri.steps, mary.steps],
    "Activity Level": ["Very Active", "Mildly Active", "Very Active", "Mildly Active", "Mildly Active"]
})

groupGoalPoints = pd.DataFrame({
    "Person": [niya.name, kelly.name, laurie.name, gauri.name, mary.name],
    "Individual Points": [niya.points, kelly.points, laurie.points, gauri.points, mary.points],
    "Activity Level": ["Usually Very Active", "Usually Mildly Active", "Usually Very Active", " Usually Mildly Active",
                       "Usually Mildly Active"]
})

bpmDataIndividual = pd.DataFrame({
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Average Weekly BPM": [120, 100, 80, 180, 156, 200, 69],
})

steps = px.bar(stepsData, x="Person", y="Average Weekly Steps", color="Activity Level", barmode="group", title='Group Steps Breakdown')
groupPie = px.pie(groupGoalPoints, values='Individual Points', names='Person', title='Group Goal Breakdown')

bpmNiya = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM", title="Niya's Daily BPM")
bpmKelly = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM", title="Kelly's Daily BPM")
bpmLaurie = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM", title="Laurie's Daily BPM")
bpmGauri = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM", title="Niya's Daily BPM")
bpmMary = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM", title="Niya's Daily BPM")

logo = Image.open("data/fit together.png")
rocket = Image.open("data/rocket.png")

app.layout = html.Div(children=[
    html.Img(src=logo, style={'width': '30%', 'height': '30%', 'padding-left':'37%', 'padding-right':'25%'},),
    html.H3(children='''The app that takes fitness with friends to whole new level.''', style={"textAlign": 'center'}),
    html.H3(children='''Please enter your information below to get started!''', style={"textAlign": 'center', 'padding-bottom': '5%'}),
    html.Img(src=rocket, style={'width': '15%', 'height': '15%', 'padding-left': '43%', 'padding-right': '28%'}, ),
    html.Form([
        html.H3("First Name"),
        dcc.Input(id='first-name-input', type='text'),
        html.Br(),
        html.H3("Last Name"),
        dcc.Input(id='last-name-input', type='text'),
        html.Br(),
        html.H3("Fitness Level"),
        dcc.Dropdown(placeholder="Pick Me", id='fitness-level', options=["Rarely Active", "Mildly Active", "Very Active"], style={'width': '15%', 'padding-left': '43%', 'padding-right': '30%'}),
        html.H3("Group Fitness Level"),
        dcc.Dropdown(placeholder="Pick Me", id='group-fitness-level',
                     options=["Rarely Active", "Mildly Active", "Very Active"],
                     style={'width': '15%', 'padding-left': '43%', 'padding-right': '30%'}),
        html.H2("", style={'textAlign': 'center', 'padding-bottom': '1%'}),
        html.Button('Submit Form', id='submit-form', n_clicks=0, style={'textAlign': 'center', 'width': '20%'})
    ], style={'textAlign': 'center', 'padding-bottom': '5%'}),
    html.Div(id='output-div'),

    html.H2(children='Individual Data Visualization', style={'textAlign': 'center'}),
    dcc.Graph(
        id='weekly-bpm-individual1',
        figure=bpmNiya
    ),
    dcc.Graph(
        id='weekly-bpm-individual2',
        figure=bpmKelly
    ),
    dcc.Graph(
        id='weekly-bpm-individual3',
        figure=bpmLaurie
    ),
    dcc.Graph(
        id='weekly-bpm-individual4',
        figure=bpmGauri
    ),
    dcc.Graph(
        id='weekly-bpm-individual5',
        figure=bpmMary
    ),

    html.H2(children='Group Data Visualization', style={'textAlign': 'center'}),
    dcc.Graph(
        id='group-pie',
        figure=groupPie
    ),
    dcc.Graph(
        id='weekly-steps',
        figure=steps
    )
])


@app.callback(
    Output('output-div', 'children'),
    [Input('submit-form', 'n_clicks')],
    [State('first-name-input', 'value'),
     State('last-name-input', 'value'),
     State('fitness-level', 'value'),
     State('group-fitness-level', 'value')]
)
def update_output(n_clicks, firstName, lastName, fitnessLevel, groupFitness):
    if n_clicks > 0:
        df = pd.DataFrame([[firstName, lastName, fitnessLevel, groupFitness]], columns=["First Name", "Last Name", "Individual Fitness Level", "Group Fitness Level"])
        with ExcelWriter("personData.xlsx") as writer:
            df.to_excel(writer)



if __name__ == '__main__':
    app.run_server(debug=True)

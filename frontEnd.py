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
    "Average Daily Steps": [niya.steps, kelly.steps, laurie.steps, gauri.steps, mary.steps],
    "Activity Level": ["Rarely Active", "Mildly Active", "Very Active", "Mildly Active", "Mildly Active"]
})

groupGoalPoints = pd.DataFrame({
    "Person": [niya.name, kelly.name, laurie.name, gauri.name, mary.name],
    "Individual Points": [niya.points, kelly.points, laurie.points, gauri.points, mary.points],
    "Activity Level": ["Usually Very Active", "Usually Mildly Active", "Usually Very Active", " Usually Mildly Active",
                       "Usually Mildly Active"]
})

bpmDataNiya = pd.DataFrame({
    "Hours": ["6:00AM", "7:00AM", "8:00AM", "9:00AM", "10:00AM", "11:00AM", "12:00PM",
              "1:00PM", "2:00PM", "3:00PM", "4:00PM", "5:00PM", "6:00PM", "7:00PM", "8:00PM",
              "9:00PM", "10:00PM", "11:00PM", "12:00AM", "1:00AM", "2:00AM", "3:00AM", "4:00AM",
              "5:00AM"],
    "Average Daily BPM": [120, 34, 80, 180, 156, 200, 69, 120, 89, 80, 180, 156,
                          120, 100, 80, 46, 156, 123, 69, 120, 34, 80, 90, 156]
})

bpmDataKelly = pd.DataFrame({
    "Hours": ["6:00AM", "7:00AM", "8:00AM", "9:00AM", "10:00AM", "11:00AM", "12:00PM",
              "1:00PM", "2:00PM", "3:00PM", "4:00PM", "5:00PM", "6:00PM", "7:00PM", "8:00PM",
              "9:00PM", "10:00PM", "11:00PM", "12:00AM", "1:00AM", "2:00AM", "3:00AM", "4:00AM",
              "5:00AM"],
    "Average Daily BPM": [80, 40, 120, 180, 156, 123, 69, 56, 100, 80, 180, 200,
                          120, 100, 80, 180, 67, 150, 69, 120, 67, 80, 180, 123]
})

steps = px.bar(stepsData, x="Person", y="Average Daily Steps", color="Activity Level", barmode="group", title='Group Steps Breakdown')
groupPie = px.pie(groupGoalPoints, values='Individual Points', names='Person', title='Group Goal Breakdown')

bpmNiya = px.line(bpmDataNiya, x="Hours", y="Average Daily BPM", title="Niya's Daily BPM")
bpmKelly = px.line(bpmDataKelly, x="Hours", y="Average Daily BPM", title="Kelly's Daily BPM")

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
        html.H3("Fitness Level Goal"),
        dcc.Dropdown(placeholder="Pick Me", id='fitness-level',
        options=["Rarely Active - 10 Points", "Mildly Active - 20 Points", "Very Active - 30 Points"],
        style={'width': '15%', 'padding-left': '43%', 'padding-right': '30%', 'padding-bottom': '2%'}),
        html.Button('Submit Form', id='submit-form', n_clicks=0, style={'textAlign': 'center', 'width': '20%'})
    ], style={'textAlign': 'center', 'padding-bottom': '5%'}),
    html.Div(id='output-div'),

    html.H2(children='Individual Data Visualization', style={'textAlign': 'center'}),
    dcc.Graph(
        id='daily-bpm-individual1',
        figure=bpmNiya
    ),
    dcc.Graph(
        id='daily-bpm-individual2',
        figure=bpmKelly
    ),

    html.H2(children='Group Data Visualization', style={'textAlign': 'center'}),
    dcc.Graph(
        id='group-pie',
        figure=groupPie
    ),
    dcc.Graph(
        id='daily-steps',
        figure=steps
    )
])


@app.callback(
    Output('output-div', 'children'),
    [Input('submit-form', 'n_clicks')],
    [State('first-name-input', 'value'),
     State('last-name-input', 'value'),
     State('fitness-level', 'value')]
)

def update_output(n_clicks, firstName, lastName, fitnessLevel):
    if n_clicks > 0:
        fitnessLevelSplit = fitnessLevel.split('- ')
        points = fitnessLevelSplit[1].split('Points')
        df = pd.DataFrame([[firstName, lastName, points[0]]], columns=["First Name", "Last Name", "Individual Points Goal"])
        with ExcelWriter("data/%s.xlsx", firstName) as writer:
            df.to_excel(writer)

if __name__ == '__main__':
    app.run_server(debug=True)

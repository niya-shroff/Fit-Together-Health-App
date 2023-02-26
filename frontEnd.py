import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd
from personClass import Person
from pymongo import MongoClient
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

niya = Person("Niya", 8000, "60 Minutes", 20, 120, "60 Mins", "10%")
kelly = Person("Kelly", 6000, "60 Minutes", 17, 120, "60 Mins", "10%")
laurie = Person("Laurie", 9000, "60 Minutes", 23, 120, "60 Mins", "10%")
gauri = Person("Gauri", 5000, "60 Minutes", 15, 120, "60 Mins", "10%")
mary = Person("Mary", 4000, "60 Minutes", 12, 120, "60 Mins", "10%")

group = [niya, kelly, laurie, gauri, mary]

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

name = "Niya Shroff"
steps = px.bar(stepsData, x="Person", y="Average Weekly Steps", color="Activity Level", barmode="group",
               title='Group Steps Breakdown')
groupPie = px.pie(groupGoalPoints, values='Individual Points', names='Person', title='Group Goal Breakdown')
bpm = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM", title=name + "'s Weekly BPM")

app.layout = html.Div(children=[
    html.H1(children='HealthHack App', style={'textAlign': 'center'}),
    html.Div(children='''
        A collaborative health application that allows 
        individuals to reach their personal goals with their friends
        while working towards the group's goal.
    ''', style={'textAlign': 'center'}),

    # Form for basic information
    html.H1("Example Form"),
    html.Form([
        html.Label("Name"),
        dcc.Input(id='name-input', type='text'),
        html.Br(),
        html.Label("Email"),
        dcc.Input(id='email-input', type='email'),
        html.Br(),
        html.Button('Submit', id='submit-form', n_clicks=0)
    ]),
    html.Div(id='output-div'),

    html.H2(children='Group Data Visualization', style={'textAlign': 'center'}),
    dcc.Graph(
        id='group-pie',
        figure=groupPie
    ),
    dcc.Graph(
        id='weekly-steps',
        figure=steps
    ),

    html.H2(children='Individual Data Visualization', style={'textAlign': 'center'}),
    dcc.Graph(
        id='weekly-bpm-individual',
        figure=bpm
    )
])


@app.callback(
    Output('output-div', 'children'),
    [Input('submit-form', 'n_clicks')],
    [State('name-input', 'value'),
     State('email-input', 'value')]
)
def update_output(n_clicks, name, email):
    if n_clicks > 0:
       print(f"Thank you, {name} ({email}), for submitting the form!")


if __name__ == '__main__':
    app.run_server(debug=True)

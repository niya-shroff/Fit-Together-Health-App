import dash
from dash import dcc
from dash import html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

stepsData = pd.DataFrame({
    "Person": ["Niya", "Kelly", "Laurie", "Gauri", "Mary"],
    "Average Weekly Steps": [8000, 5000, 10000, 5000, 7500],
    "Activity Level": ["Very Active", "Mildly Active", "Very Active", "Mildly Active", "Mildly Active"]
})

groupGoalPoints = pd.DataFrame({
    "Person": ["Niya", "Kelly", "Laurie", "Gauri", "Mary"],
    "Individual Points": [20, 100, 80, 180, 156],
    "Activity Level": ["Very Active", "Mildly Active", "Very Active", "Mildly Active", "Mildly Active"]
})

bpmDataIndividual = pd.DataFrame({
    "Days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Average Weekly BPM": [120, 100, 80, 180, 156, 200, 69],
})

steps = px.bar(stepsData, x="Person", y="Average Weekly Steps", color="Activity Level", barmode="group")
bpm = px.line(bpmDataIndividual, x="Days", y="Average Weekly BPM")
groupPie = px.pie(groupGoalPoints, values='Individual Points', names='Person', title='Group Goal Breakdown')

app.layout = html.Div(children=[
    html.H1(children='HealthHack App'),
    html.Div(children='''
        A collaborative health application that allows 
        individuals to reach their personal goals with their friends
        while working towards the group's goal.
    '''),

    html.H2(children='Group Data Visualization'),
    dcc.Graph(
        id='group-pie',
        figure=groupPie
    ),
    dcc.Graph(
        id='weekly-steps',
        figure=steps
    ),

    html.H2(children='Individual Data Visualization'),
    dcc.Graph(
        id='weekly-bpm-individual',
        figure=bpm
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
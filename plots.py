import plotly
import plotly.express as px
from cleaning_data import feature, data_bankmarketing
import json
import pickle

def feature_plots():
    score = pickle.load(open('feature_importance.sav','rb'))
    fig = px.bar(score.reset_index().sort_values(by='Score', ascending=True).tail(20), x='Score', y='index', orientation='h')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def euribor_plots():
    df = data_bankmarketing()
    fig = px.histogram(df, x="euribor3m", color="y",
                   marginal="box", 
                   hover_data=df.columns)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def default_plots():
    df = data_bankmarketing()
    fig = fig = px.bar(x=df["default"].value_counts().index, y=df["default"].value_counts().values)
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
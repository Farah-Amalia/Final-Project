import plotly
import plotly.express as px
from cleaning_data import feature
import json
import pickle

def feature_plots():
    score = pickle.load(open('feature_importance.sav','rb'))
    fig = px.bar(score.reset_index().sort_values(by='Score', ascending=True).tail(20), x='Score', y='index', orientation='h')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json
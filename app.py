from flask import Flask,render_template,request
from data import job, marital, education, default, day, month
from prediction import prediction
from cleaning_data import data_bankmarketing
from plots import feature_plots, euribor_plots, default_plots

## translate Flask to python object
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        hasil = prediction(data)
        return render_template('result.html', hasil_prediction=hasil)
    return render_template('prediction.html',
    data_job=sorted(job),
    data_marital=sorted(marital),
    data_education=sorted(education),
    data_default=sorted(default),
    data_month=month,
    data_day=day
    )

@app.route('/data')
def data():
    data = data_bankmarketing().head(50)
    return render_template('table_data.html', data=data)

@app.route('/plots')
def plots():
    data1 = feature_plots()
    data2 = euribor_plots()
    data3 = default_plots()
    return render_template('plots.html', data1=data1, data2=data2, data3=data3)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=1111)
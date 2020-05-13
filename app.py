from flask import Flask,render_template,request
from data import job, marital, education, default, day, month
from prediction import prediction
from cleaning_data import data_bankmarketing

## translate Flask to python object
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index_prediction():
    if request.method == "POST":
        data = request.form
        data = data.to_dict()
        # data['Rooms'] = int(data['Rooms'])
        # data['Bathrooms'] = int(data['Bathrooms'])
        # data['Size Num'] = int(data['Size Num'])
        hasil = prediction(data)
        return render_template('result.html', hasil_prediction=hasil)
    return render_template('prediction.html',
    data_job=sorted(job),
    data_marital=sorted(marital),
    data_education=sorted(education),
    data_default=sorted(default),
    data_month=sorted(month),
    data_day=sorted(day)
    )

@app.route('/data')
def data():
    data = data_bankmarketing()
    return render_template('table_data.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, port=1111)
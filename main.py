import pickle
from flask import Flask, render_template, request
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
#from typing import List
#from pydantic import BaseModel


'''1. Your main page at root (meaning URL `/`) has to display the page
      containing the data to fill. In other words you have to render in your
      root (`/`) the HTML file `index.html`.'''

app = Flask(__name__)

@app.route('/', methods=['GET'])
def auto_mpg_index():
    return render_template('index.html')


'''2. Create a function supporting the `POST` method, where you will gather
      the data from the previous form and predict the mpg and
      display it by putting in a variable named `price` and render `prediction.html`.'''


@app.route('/predict/', methods=['POST'])
def result():
    if request.method == 'POST':
        cylinders = int(request.form['Cylinders'])
        displacement = float(request.form['Displacement'])
        horsepower = float(request.form['Horsepower'])
        weight = float(request.form['Weight'])
        acceleration = float(request.form['Acceleration'])
        origin = int(request.form['Origin'])
        model_year = float(request.form['Model_year'])

        if origin == 1:
            origin_2 = 0
            origin_3 = 0
        elif origin == 2:
            origin_2 = 1
            origin_3 = 0
        elif origin == 3:
            origin_2 = 0
            origin_3 = 1

        if model_year == 70:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 71:
            model_year_71 = 1
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 72:
            model_year_71 = 0
            model_year_72 = 1
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 73:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 1
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 74:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 1
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 75:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 1
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 76:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 1
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 77:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 1
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 78:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 1
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 79:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 1
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 80:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 1
            model_year_81 = 0
            model_year_82 = 0
        elif model_year == 81:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 1
            model_year_82 = 0
        elif model_year == 82:
            model_year_71 = 0
            model_year_72 = 0
            model_year_73 = 0
            model_year_74 = 0
            model_year_75 = 0
            model_year_76 = 0
            model_year_77 = 0
            model_year_78 = 0
            model_year_79 = 0
            model_year_80 = 0
            model_year_81 = 0
            model_year_82 = 1

        loaded_scaler = pickle.load(open('auto_mpg_scaler.pkl', 'rb'))
        data_to_scale = [[displacement, horsepower, weight, acceleration]]
        data_scaled = loaded_scaler.transform(data_to_scale)
        displacement, horsepower, weight, acceleration = data_scaled.ravel()

        data = [[cylinders, displacement, horsepower, weight, acceleration, origin_2, origin_3, \
        model_year_71, model_year_72, model_year_73, model_year_74, model_year_75, \
        model_year_76, model_year_77, model_year_78, model_year_79, model_year_80, \
        model_year_81, model_year_82]]

        loaded_model = pickle.load(open(f"auto_mpg_model.pkl", 'rb')) # loading a pretrained model
        pred = loaded_model.predict(data)

        return render_template('prediction.html', fuel=round(pred[0], 1))


if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
        )

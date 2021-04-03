import flask
from flask import request, render_template
app = flask.Flask(__name__)
app.config["DEBUG"] = True

from flask_cors import CORS
CORS(app)


@app.route('/search',methods=['GET'])
def search():
    return ''' <h1> Searching...  '''+ request.args['s']+ '''</h1>'''


@app.route('/',methods=['GET'])
def home():
    return render_template('hp.html')


@app.route('/predict',methods=['GET', 'POST'])
def predict():
    import joblib
    model = joblib.load('house_price_prediction_trained_model.pkl')
    price = model.predict([[int(request.args['sqft']),
                            int(request.args['place']),
                            int(request.args['yo']),
                            int(request.args['tf']),
                            int(request.args['bhk']),
                           ]])
    return str(round(price[0]))


app.run()

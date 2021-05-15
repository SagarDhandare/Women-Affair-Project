from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)
model = pickle.load(open('LogisReg.pickle', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        rate_marriage = float(request.form['rate_marriage'])
        age = float(request.form['age'])
        yrs_married = float(request.form['yrs_married'])
        children = float(request.form['children'])
        religious = float(request.form['religious'])
        educ = float(request.form['educ'])
        occupation = float(request.form['occupation'])
        occupation_husb = float(request.form['occupation_husb'])


        prediction = model.predict(standard_to.fit_transform([[rate_marriage,age, yrs_married, children, religious, educ, occupation, occupation_husb]]))[0]
        output = int(prediction)
        if output == 1:
            return render_template('index.html', prediction_text = 'The Women having atleast 1 affair.')
        else:
            return render_template('index.html', prediction_text='The Women dont have affair.')

    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)


from flask import Flask, render_template, request

#initiaze application
app = Flask(__name__)

#Load your Trained model
import pickle
model = pickle.load(open('pizza_model.pkl','rb'))

#GET API(default landing page)
@app.route("/")
def home():
    return render_template("index.html")

#POST API
@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        age = int(request.form['ageinp'])
        weight = int(request.form['weightinp'])
        pred = model.predict([[age,weight]])
        if pred.item() == 1:
            msg = "Enjoy Pizza"
            return render_template("index.html", message = msg)
        else:
            msg = "Go to GYM"
            return render_template("index.html", message = msg)
        
       


if __name__=='__main__':
    app.run(debug=True)
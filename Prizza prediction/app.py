from flask import Flask, render_template

#initiaze application
app = Flask(__name__)

#GET API(default landing page)
@app.route("/")
def home():
    return render_template("index.html")


#GET AII
@app.route("/about_us")
def about_us():
    return "This is about us page"


if __name__=='__main__':
    app.run(debug=True)
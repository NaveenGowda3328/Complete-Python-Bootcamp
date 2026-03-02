from flask import Flask,flash,render_template

app = Flask(__name__)

app.secret_key = "225sfg13dds5s1f21f312f132d1f3af"

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logout")
def logout():
    flash("You have been logged out!","success")
    return render_template("index.html")

app.run(debug=True)
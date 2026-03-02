from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello_world():
    if(request.method == "POST"):
        # Handle the from
       
        return render_template("contact.html")

   
app.run(debug=True)
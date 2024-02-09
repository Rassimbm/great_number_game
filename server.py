from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = random.randint(1,100)
    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def guess():
    session["guess_num"] = int(request.form["guess_num"])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "num" and "guess_count" not in session:
        session["num"] = random.randint(1,100)
        session["guess_count"] = 0
    
    return render_template("index.html", guess_count=session["guess_count"])

@app.route("/guess", methods = ["POST"])
def guess():
    session["guess_count"] += 1
    session["guess_num"] = int(request.form["guess_num"])
    return redirect("/")

@app.route("/reset-game")
def reset_game():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
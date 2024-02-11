from flask import Flask, session, render_template, request, redirect
import random

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "num" and "count" not in session:
        session["num"] = random.randint(1,100)
        session["count"] = 5
    return render_template("index.html")

@app.route("/guess", methods = ["POST"])
def guess():
    session["guess"] = int(request.form["guess_num"])
    session["count"] -= 1
    # if session["count"] == 0:
    #     session.pop("count")
    return redirect("/")

@app.route("/reset-game")
def reset_game():
    session.clear()
    return redirect("/")

@app.route("/play-again")
def play_again():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, session, render_template
import random

app = Flask(__name__)
app.secret_key = "8891techa0128"

@app.route("/")
def index():
    if "num" not in session:
        session["num"] = random.randint(1,100)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
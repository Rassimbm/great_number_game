from flask import Flask, render_template, session, redirect

app = Flask(__name__)
app.secret_key = "8891techa0128"


if __name__ == "__main__":
    app.run(debug=True)
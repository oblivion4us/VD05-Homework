from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/")
def discography():
    return render_template("discography.html")

@app.route("/contacts/")
def contacts():
    return render_template("about.html")

if __name__ == "__main__":
    app.run()
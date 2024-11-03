from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    context = {


    }
    return render_template("base.html", **context)

@app.route("/discography/")
def discography():
    context = {

    }
    return render_template("discography.html")

@app.route("/contacts/")
def contacts():
    return render_template("contacts.html")

if __name__ == "__main__":
    app.run()
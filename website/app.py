from flask import Flask, url_for,render_template,redirect, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", title="Home")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


if __name__ == "__main__":
    app.run(debug=True)
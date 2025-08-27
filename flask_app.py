from flask import Flask, render_template, abort
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template("index.html", time=current_time)

# Só funciona quando o nome for exatamente "Soraya Gomes"
@app.route("/user/<name>")
def user(name):
    if name == "Soraya Gomes":
        return render_template("user.html", name=name)
    abort(404)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run()

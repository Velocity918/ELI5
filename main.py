import backend
import flask
from flask import Flask,render_template, request

main = Flask(__name__)


@main.route("/", methods = ["POST", "GET"])
def home():
    
    if request.method== 'POST':
        query = request.form['query']
        return render_template('answer.html', answer = backend.ELI5(query) )
    return render_template("index.html")  
    
@main.route("/answer", methods = ["POST", "GET"])
def answer():
    if request.method == "POST":
        return flask.redirect(flask.url_for("home"))
    return render_template("answer.html")  


if __name__ == "__main__":
    main.run(debug=True)
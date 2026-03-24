import backend
from flask import Flask,render_template,request

main = Flask(__name__)


@main.route("/", methods = ["POST", "GET"])
def home():
    while True:
        if request.method== 'POST':
            query = request.form['query']
            return backend.ELI5(query)
        return render_template('index.html')
    



if __name__ == "__main__":
    main.run(debug=True)
# user_input = input()

# answer = backend.ELI5(user_input)
# print(answer)
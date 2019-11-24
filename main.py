from flask import Flask, render_template, request, make_response

import random

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    secretNumber = request.cookies.get("secretNumber")
    response = make_response(render_template("index.html"))

    if not secretNumber:
        secretNumber = random.randint(1, 30)
        response.set_cookie("secretNumber", str(secretNumber))

    return response


@app.route("/result", methods=["POST"])
def result():
    guess = int(request.form.get("guess"))
    secretNumber = int(request.cookies.get("secretNumber"))

    if guess == secretNumber:
        message = "Correct! The secret number is " + str(secretNumber)
        response = make_response(render_template("result.html", message=message))
        response.set_cookie("secretNumber", str(random.randint(1, 30)))
        return response
    elif guess > secretNumber:
        message = "Your guess is not correct... try something smaller."
        return render_template("result.html", message=message)
    elif guess < secretNumber:
        message = "Your guess is not correct... try something bigger."
        return render_template("result.html", message=message)


if __name__ == '__main__':
    app.run()

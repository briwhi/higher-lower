import random
from flask import Flask
app = Flask(__name__)
number = random.randint(0, 9)


@app.route('/')
def start_game():
    return '<h1>Guess a number between 0 and 9: </h1>' \
       '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"/>'


@app.route('/<int:guess>')
def guess(guess):
    if guess == number:
        return '<h1 style="color:green"> You found me!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"/>'
    elif guess > number:
        return '<h1 style="color:red">Too high</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"/>'
    else:
        return '<h1 style="color:yellow">Too low</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"/>'



def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


@app.route('/bye')
@make_bold
def goodbye():
    return 'Goodbye'


@app.route("/username/<name>")
def greet(name):
    return f"Hello {name}"


if __name__ == "__main__":
    app.run(debug=True)
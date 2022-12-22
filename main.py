from flask import Flask
import random

app = Flask(__name__)


# def make_bold(function):
#     def wrapper():
#         start_tag = '<b>'
#         rv = function()
#         end_tag = "</b>"
#         return start_tag+rv+end_tag
#     return wrapper

generated_number = random.choice(range(0, 10))

@app.route('/')
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media2.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e471hcfb70d1mgzu3wmverzz215arubd5vxdn3tq8wn&rid=giphy.gif&ct=g" width=200>'


@app.route('/bye')
# @make_bold
def bye():
    return "Bye!"


@app.route('/<int:guess>')
def check(guess):
    number = generated_number
    if guess > number:
        return '<h1>Too High!</h1>' \
               '<img src="https://media3.giphy.com/media/3o7abAHdYvZdBNnGZq/giphy.gif?cid=ecf05e473099fjgjpi96fyaie8k4j830dsy3lj3wjq42ea3d&rid=giphy.gif&ct=g" width=200>'
    elif guess < number:
        return '<h1>Too Low!</h1>' \
               '<img src="https://media1.giphy.com/media/xT5LMXHr6YUQdlRI5i/giphy.gif?cid=ecf05e47i2oos3ladxl2c0ds4n6prb6qgn10wcdtdgrhml8s&rid=giphy.gif&ct=g" width=200>'
    else:
        return '<h1>You got it!</h1>' \
               '<img src="https://media4.giphy.com/media/Rznz8HjrKQAOQ/giphy.gif?cid=ecf05e47kfrumgfim1afj8vfxc163fcn3ko70wi82polfn1x&rid=giphy.gif&ct=g" width=200>'


if __name__ == "__main__":
    app.run(debug=True)

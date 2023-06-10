# flask --app D:\Pyhton_Dir\Projects\Working_repo\web\hello_flask\hello.py run
from flask import Flask

app = Flask(__name__) # Flask check __name__

def make_bold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped


def make_italic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped


def make_underline(fn):
    def wrapped():
        return "<u>" + fn() + "</u>"
    return wrapped



@app.route("/") # / - home page
def hello_world():
    return '<h1 style="text-align: center">  Hello, Alena!</h1>' \
            '<p> This is a par. </p>' \
            '<img src="https://media1.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e47looxxhca2gwns7bna2535jjp9xivxqrrbv63fifs&ep=v1_gifs_search&rid=200.webp&ct=g">' \
            '<p> This is a par. 2</p>'

@make_bold
@make_italic
@make_underline
@app.route("/bye")
def say_bye():
    return "Bye"


@app.route("/username/<name>/<int:number>")  # variable to route
def greet(name, number):
    return f'Hello {name} you are {number} years old!'


if __name__ == '__main__':
    app.run(debug=True) # debug

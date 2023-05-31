# flask --app D:\Pyhton_Dir\Projects\Working_repo\web\hello_flask\hello.py run
from flask import Flask
import random

app = Flask(__name__) # Flask check __name__

print(random.__name__)

@app.route("/") # / - home page
def hello_world():
    return "<p>Hello, World!</p>"


# @app.route("/bye")
# def say_bye():
#     return "Bye"

if __name__ == '__main__':
    app.run()
    
    
# python Decorators function that gives additional functionality to our function     
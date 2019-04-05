from flask import Flask
from flask_restful import Resource, Api
from user import *
from language import *

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Frontend HTML goes here'

#Initialize as rest
add_user_to_router(api)
add_language_to_router(api)

if __name__ == '__main__':
    app.run()

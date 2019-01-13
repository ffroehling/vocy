from flask import Flask
from flask_restful import Resource, Api
from user import User

app = Flask(__name__)
api = Api(app)

@app.route('/')
def index():
    return 'Frontend HTML goes here'

#Initialize as rest
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run()

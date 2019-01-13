from flask import Flask
from flask_restful import Resource, Api

class User(Resource):
    #get all user
    def get(self):
        return {'hello': 'get'}

    #create a new user
    def post(self):
        return {'hello': 'post'}

    #update user information 
    def put(self):
        return {'hello': 'put'}

    #delete user information 
    def delete(self):
        return {'hello': 'delete'}



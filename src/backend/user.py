from flask import Flask 
from flask_restful import Resource, Api, reqparse
from database import Session
import json
import random
from model import *

#Base class
#class UserBase(Resource):
#    def __init__(self):
#        self.load_user_data()
#
#    def load_user_data(self):
#        with open("data/user.json", "r") as f:
#            content = f.read()
#            self.user_data = json.loads(content)
#
#    #get random id max 10000
#    def get_available_id(self):
#        id = random.randrange(10000)
#        for user in self.user_data:
#            if user['id'] == id:
#                return self.get_available_id()
#
#        return id
#
#    def update_json(self):
#        with open("data/user.json", "w") as f:
#            f.write(json.dumps(self.user_data))
#
##specific user instances
#class UserDetail(UserBase):
#    #update user 
#    def put(self):
#        return {'hello': 'put'}
#
#    #delete user
#    def delete(self):
#        return {'hello': 'delete'}
#
##list operations
#class UserList(UserBase):
#    #get all user
#    def get(self):
#        return self.user_data
#
#    #create a new user
#    def post(self):
#        #validate request
#        parser = reqparse.RequestParser()
#        parser.add_argument('name', help='The name of the user', required=True)
#        args = parser.parse_args()
#
#        #create instance
#        id = self.get_available_id()
#        obj = {'id' : id, 'name' : args['name']}
#
#        #store it to json
#        self.user_data.append(obj)
#        self.update_json()
#        
#        return obj
#
def add_user_to_router(api):
    api.add_resource(UserList, '/user')
    #api.add_resource(UserDetail, '/user/<int:todo_id>')

#returns all user
def get_user(session):
    users = session.query(User).all()
    print(users)
    for u in users:
        print(u.as_json())
        #print(u.jaijfois())

    return None

    return [u.as_json() for u in user] 

def operation(func, *args):
    session = Session()
    result = None
    #try:
    result = func(session, *args)
    #finally:
    session.close()
    return result

class UserList(Resource):
    def get(self):
        result = operation(get_user)
        return result

#user = User()
#user.name = "Felix"
#session = Session()
#session.add(user)
#session.commit()
#session.close()
#Session().add(user)

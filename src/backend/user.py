from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from database import Session
from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
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
    api.add_resource(UserList, '/user', endpoint='users')
    api.add_resource(UserDetail, '/user/<int:user_id>', endpoint='user')
    #api.add_resource(UserDetail, '/user/<int:todo_id>')

#returns all user
def get_all_user(session):
    users = session.query(User).all()
    for u in users:
        print(u.as_json())
        #print(u.jaijfois())

    return [u.as_json(relationships=False) for u in users] 

def get_user_detail(session, user_id):
    user = session.query(User).filter(User.id == user_id).first()
    return user

def update_user(session, user_id, name):
    user = session.query(User).filter(User.id == user_id).first()

    if user is not None:
        user.name = name
        session.add(user)
        session.commit()

    return user

def delete_user(session, user_id):
    user = session.query(User).filter(User.id == user_id).first()

    if user:
        session.delete(user)
        session.commit()
        return True

    return False



def create_user(session, name):
    try:
        user = User()
        user.name = name
        session.add(user)
        session.commit()
        print(user)
        return (True, user)
    except Exception as e:
        #TODO: Log eception
        return (False, None)



def operation(func, *args):
    session = Session()
    result = func(session, *args)

    return (result, session)

class UserList(Resource):
    args = {
        'name': fields.Str(
            required=True
        ),
    }

    #return all users
    def get(self):
        result, session = operation(get_all_user)
        session.close()
        return result

    #create a new user
    @use_kwargs(args)
    def post(self, name):
        (succ, user), session = operation(create_user, name)
        if succ:
            resp = (user.as_json(), 200)
            session.close()

            return resp
        else:
            session.close()
            return make_response('Unexpected error occured :(', 500)

class UserDetail(Resource):
    args = {
        'name': fields.Str(
            required=True
        ),
    }

    def get(self, user_id):
        user, session = operation(get_user_detail, user_id)

        if user is not None:
            resp = (user.as_json(), 200)
            session.close()
            return resp
        else:
            session.close()
            return make_response('User not found', 400)

        return result

    @use_kwargs(args)
    def put(self, user_id, name):
        user, session = operation(update_user, user_id, name)

        if user is not None:
            resp = (user.as_json(), 200)
            session.close()
            return resp
        else:
            session.close()
            return make_response('User not found', 400)

    def delete(self, user_id):
        succ, session = operation(delete_user, user_id)
        
        session.close()

        if succ:
            return make_response('', 200)
        else:
            return make_response('User not found', 400)





            

#@parser.error_handler
#def handle_error(error, req, schema, status_code, headers):
#    raise ValidationError("Invalid User Object received")
            

#user = User()
#user.name = "Felix"
#session = Session()
#session.add(user)
#session.commit()
#session.close()
#Session().add(user)

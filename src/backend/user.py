from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from database import Session
from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
import json
import random
from model import *

def add_user_to_router(api):
    api.add_resource(UserList, '/user', endpoint='users')
    api.add_resource(UserDetail, '/user/<int:user_id>', endpoint='user')

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

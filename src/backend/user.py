from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
from model import *
from database import Session
from entities import EntityList, EntityDetail
from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse

def add_user_to_router(api):
    api.add_resource(UserList, '/user', endpoint='users')
    api.add_resource(UserDetail, '/user/<int:item_id>', endpoint='user')
    api.add_resource(UserWordList, '/user/<int:user_id>/lists', endpoint='userlist')

class UserList(EntityList):
    args = {
        'name': fields.Str(
            required=True
        ),
    }

    def __init__(self):
        super(UserList, self).__init__(User)

    #create a new user
    @use_kwargs(args)
    def post(self, name):
        user = User()
        user.name = name
        return super(UserList, self).post(user)

class UserDetail(EntityDetail):
    args = {
        'name': fields.Str(
            required=True
        ),
    }

    def __init__(self):
        super(UserDetail, self).__init__(User)

    @use_kwargs(args)
    def put(self, item_id, name):
        return super(UserDetail, self).put(item_id, name=name)

class UserWordList(Resource):
    def get(self, user_id):
        session = Session()
        lists = session.query(List).filter(List.user_id == user_id).all()

        result = [l.as_json() for l in lists]

        session.close()

        return result

        session.close()

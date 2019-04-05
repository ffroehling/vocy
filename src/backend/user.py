from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
from model import *
from entities import EntityList, EntityDetail

def add_user_to_router(api):
    api.add_resource(UserList, '/user', endpoint='users')
    api.add_resource(UserDetail, '/user/<int:item_id>', endpoint='user')

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

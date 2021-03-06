from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
from model import *
from database import Session
from entities import EntityList, EntityDetail
from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse

def add_list_to_router(api):
    api.add_resource(WordlistList, '/api/list', endpoint='lists')
    api.add_resource(WordlistList, '/api/user/<int:user_id>/list', endpoint='userlists')
    api.add_resource(WordlistDetail, '/api/list/<int:item_id>', endpoint='list')
    api.add_resource(ListWordPair, '/api/list/<int:list_id>/wordpairs', endpoint='wordpairlist')


class WordlistList(EntityList):
    args = {
        'name': fields.Str(
            required=True
        ),
        'user_id' : fields.Int(
            required=True   
        ),
        'first_language_id' : fields.Int(
            required=True   
        ),
        'second_language_id' : fields.Int(
            required=True   
        ),
    }

    def get(self, user_id = None):
        if user_id:
            return super(WordlistList, self).get_for_user(user_id)
        else:
            return super(WordlistList, self).get()
        
    def validate_input(self, user_id, first_language_id, second_language_id):
        session = self.get_session()
        
        user = session.query(User).filter(User.id == user_id).first()
        firstl = session.query(Language).filter(Language.id == first_language_id).first()
        secondl = session.query(Language).filter(Language.id == second_language_id).first()

        result = user and firstl and secondl

        session.close()

        return result

    def __init__(self):
        super(WordlistList, self).__init__(List)

    #create a new wordlist
    @use_kwargs(args)
    def post(self, name, user_id, first_language_id, second_language_id):

        if self.validate_input(user_id, first_language_id, second_language_id):
            wordlist = List()
            wordlist.name = name
            wordlist.user_id = user_id
            wordlist.first_language_id = first_language_id
            wordlist.second_language_id = second_language_id
            return super(WordlistList, self).post(wordlist)
        else:
            return 'Invalid id received', 400 

class WordlistDetail(EntityDetail):
    args = {
        'name': fields.Str(
            required=True
        ),
        'user_id' : fields.Int(
            required=True   
        ),
        'first_language_id' : fields.Int(
            required=True   
        ),
        'second_language_id' : fields.Int(
            required=True   
        ),
    }

    def validate_input(self, user_id, first_language_id, second_language_id):
        session = self.get_session()
        
        user = session.query(User).filter(User.id == user_id).first()
        firstl = session.query(Language).filter(Language.id == first_language_id).first()
        secondl = session.query(Language).filter(Language.id == second_language_id).first()

        result = user and firstl and secondl

        session.close()

        return result

    def __init__(self):
        super(WordlistDetail, self).__init__(List)

    @use_kwargs(args)
    def put(self, item_id, name, user_id, first_language_id, second_language_id):
        if self.validate_input(user_id, first_language_id, second_language_id):
            return super(WordlistDetail, self).put(item_id, name=name, user_id=user_id, first_language_id=first_language_id, second_language_id=second_language_id)
        else:
            return 'Invalid id received', 400 

class ListWordPair(Resource):
    def get(self, list_id):
        session = Session()
        pairs = session.query(WordPair).filter(WordPair.llist_id == list_id).all()

        result = [p.as_json() for p in pairs]

        session.close()

        return result

        session.close()

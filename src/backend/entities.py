from flask import Flask, make_response
from flask_restful import Resource, Api, reqparse
from database import Session
from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
from model import *

class Entity(Resource):
    def __init__(self, T):
        super(Entity, self).__init__()
        self.T = T

    def get_session(self):
        return Session()

class EntityList(Entity):
    def get(self):
        session = self.get_session()
        l = session.query(self.T).all()
        
        result = [item.as_json(relationships=False) for item in l] 

        session.close()

        return result

    def post(self, item):
        try:
            session = self.get_session()
            session.add(item)
            session.commit()
        
            result = item.as_json(False), 200

            session.close()

            return result
        except Exception as e:
            #TODO: Log eception
            return make_response("Unknown error occured", 500)


class EntityDetail(Entity):
    def get(self, item_id):
        session = self.get_session()
        item = session.query(self.T).filter(self.T.id == item_id).first()

        if item is not None:
            result = item.as_json(relationships=True), 200
            session.close()
            return result
        else:
            session.close()
            return make_response("Entity not found", 400)


    def put(self, item_id, **kwargs):
        session = self.get_session()

        item = session.query(self.T).filter(self.T.id == item_id).first()

        if item is not None:
            for key,value in kwargs.items(): 
                setattr(item, key, value)

            session.add(item)
            session.commit()
        
            result = item.as_json(True)

            session.close()

            return result,200
        else:
            session.close()
            return make_response("Entity not found", 400)

    def delete(self, item_id):
        session = self.get_session()
        item = session.query(self.T).filter(self.T.id == item_id).first()
    
        if item:
            session.delete(item)
            session.commit()

            session.close()

            return make_response('', 200)
    
        session.close()
        return make_response('Item not found', 400)

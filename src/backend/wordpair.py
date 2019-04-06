from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
from model import *
from entities import EntityList, EntityDetail

def add_wordpair_to_router(api):
    api.add_resource(WordPairList, '/api/wordpair', endpoint='wordpairs')
    api.add_resource(WordPairDetail, '/api/wordpair/<int:item_id>', endpoint='wordpair')

class WordPairList(EntityList):
    args = {
        'list_id': fields.Int(
            required=True
        ),
        'first': fields.Str(
            required=True
        ),
        'second': fields.Str(
            required=True
        )
    }

    def validate_input(self, llist_id):
        session = self.get_session()
        
        llist = session.query(List).filter(List.id == llist_id).first()

        result = False

        if llist:
            result = True

        session.close()

        return result

    def __init__(self):
        super(WordPairList, self).__init__(WordPair)

    #create a new wordpair
    @use_kwargs(args)
    def post(self, list_id, first, second):
        if not self.validate_input(list_id):
            return 'Invalid ids received', 400

        wordpair = WordPair()
        wordpair.llist_id = list_id 
        wordpair.first = first 
        wordpair.second = second 

        return super(WordPairList, self).post(wordpair)

class WordPairDetail(EntityDetail):
    args = {
        'list_id': fields.Int(
            required=True
        ),
        'first': fields.Str(
            required=True
        ),
        'second': fields.Str(
            required=True
        )
    }

    def validate_input(self, llist_id):
        session = self.get_session()
        
        llist = session.query(List).filter(List.id == llist_id).first()

        result = False

        if llist:
            result = True

        session.close()

        return result

    def __init__(self):
        super(WordPairDetail, self).__init__(WordPair)

    @use_kwargs(args)
    def put(self, item_id, list_id, first, second):
        if not self.validate_input(list_id):
            return 'Invalid ids received', 400

        return super(WordPairDetail, self).put(item_id, llist_id=list_id, first=first, second=second)

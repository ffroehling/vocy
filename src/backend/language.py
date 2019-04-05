from webargs import fields, validate, ValidationError
from webargs.flaskparser import use_kwargs, use_args, parser
from model import *
from entities import EntityList, EntityDetail

def add_language_to_router(api):
    api.add_resource(LanguageList, '/language', endpoint='languages')
    api.add_resource(LanguageDetail, '/language/<int:item_id>', endpoint='language')

class LanguageList(EntityList):
    args = {
        'name': fields.Str(
            required=True
        ),
    }

    def __init__(self):
        super(LanguageList, self).__init__(Language)

    #create a new language
    @use_kwargs(args)
    def post(self, name):
        language = Language()
        language.name = name
        return super(LanguageList, self).post(language)

class LanguageDetail(EntityDetail):
    args = {
        'name': fields.Str(
            required=True
        ),
    }

    def __init__(self):
        super(LanguageDetail, self).__init__(Language)

    @use_kwargs(args)
    def put(self, item_id, name):
        return super(LanguageDetail, self).put(item_id, name=name)

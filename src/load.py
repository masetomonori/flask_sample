#from flask import request
from flask_restful import reqparse, abort, Api, Resource

class Load(Resource):
    def get(self):
        print('### load !')
        #print(request)
        #args = reqparse.RequestParser().parse_args()
        #print(args)
        #print(request)
        print(Resource)
    
        response = {
            "message":"OK:Load successful",
            "code":"EN000",
            "result":{
                "word_set":[]
            }
        }
        return response, 200


# {"message":"OK:Load successful","code":"EN000","result":{"word_set":[



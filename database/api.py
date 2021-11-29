from flask import Flask
from flask_restful import Resource, Api, reqparse
from modules.mongodb import *
import json
from bson import json_util

app = Flask(__name__)
api = Api(app)

class Actualites(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('namepost')
        args = parser.parse_args()  # parse arguments to dictionary

        if not args['namepost']:
            data = get_Actualites_All()
            return {'data': json.loads(json_util.dumps(data))}, 200
        else:
            data = get_Actualites_One(args['namepost'])    
            if data != None:
                return {'data': json.loads(json_util.dumps(data))}, 200
            else:
                return {"This user doesn't exist"}, 404    

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('namepost', required=True)   
        parser.add_argument('uriimg', required=True) 
        parser.add_argument('descriptionpost', required=True)     
        args = parser.parse_args()

        data = get_Actualites_One(args['namepost'])    
        if data != None:
            return {'data':"This actuality already exist"},404
        else:
            data = add_Actualites(args['namepost'], args['uriimg'], args['descriptionpost'])    
            return {'data': json.loads(json_util.dumps(data))}, 200

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('namepost', required=True)
        parser.add_argument('uriimg', required=True)
        parser.add_argument('descriptionpost', required=True)
        args = parser.parse_args()

        filter = {'namepost': args['namepost']}
        newvalues = {"$set": {'uriimg':args['uriimg'], 'descriptionpost':args['descriptionpost']}}
        result = update_Actualites(filter, newvalues)    
        if result.modified_count == 1:
            return {'data':"This actuality has been updated"}, 200
        else:
            return {'data':"Failed to update this actuality"}, 404    
        

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('namepost', required=True)    
        args = parser.parse_args()

        result = delete_Actualites(args['namepost'])
        if result.deleted_count == 1:
            return {'data':"This actuality has been deleted"}, 200
        else:
            return {'data':"Failed to delete this actuality"}, 404  


class Formations(Resource):
    def get(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('nameformation')
        args = parser.parse_args()  # parse arguments to dictionary

        if not args['nameformation']:
            data = get_Formation_All()
            return {'data': json.loads(json_util.dumps(data))}, 200
        else:
            data = get_Formation_One(args['nameformation'])    
            if data != None:
                return {'data': json.loads(json_util.dumps(data))}, 200
            else:
                return {"This user doesn't exist"}, 404    

    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('nameformation', required=True)   
        parser.add_argument('uriimg', required=True) 
        parser.add_argument('descriptionformation', required=True)     
        args = parser.parse_args()

        data = get_Formation_One(args['nameformation'])    
        if data != None:
            return {'data':"This formation already exist"},404
        else:
            data = add_Formation(args['nameformation'], args['uriimg'], args['descriptionformation'])    
            return {'data': json.loads(json_util.dumps(data))}, 200

    def put(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('nameformation', required=True)
        parser.add_argument('uriimg', required=True)
        parser.add_argument('descriptionformation', required=True)
        args = parser.parse_args()

        filter = {'nameformation': args['nameformation']}
        newvalues = {"$set": {'uriimg':args['uriimg'], 'descriptionformation':args['descriptionformation']}}
        result = update_Formation(filter, newvalues)    
        if result.modified_count == 1:
            return {'data':"This actuality has been updated"}, 200
        else:
            return {'data':"Failed to update this actuality"}, 404    
        

    def delete(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('namepost', required=True)    
        args = parser.parse_args()

        result = delete_Formation(args['namepost'])
        if result.deleted_count == 1:
            return {'data':"This actuality has been deleted"}, 200
        else:
            return {'data':"Failed to delete this actuality"}, 404                
        

api.add_resource(Actualites, '/actualites')  # add endpoints
api.add_resource(Formations, '/formations')

if __name__ == '__main__':
    app.run()  # run our Flask app        
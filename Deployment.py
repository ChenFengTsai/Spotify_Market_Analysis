from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

class getLabel(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('danceability', type = float, required = True)
        parser.add_argument('energy', type = float, required = True)
        parser.add_argument('key', type = float, required = True)
        parser.add_argument('speechiness', type = float, required = True)
        parser.add_argument('acousticness', type = float, required = True)
        parser.add_argument('tempo', type = float, required = True)
        parser.add_argument('duration', type = float, required = True)
        
        arguments = parser.parse_args()
        with open('gmm_model.pkl', 'rb') as file: 
            model = pickle.load(file)
        vector = [arguments['danceability']*50, arguments['energy']*50, arguments['key']*50, np.log(arguments['speechiness']*50),
                 np.log(arguments['acousticness']*50), arguments['tempo']*50, arguments['duration']*50]
        prediction = model.predict([vector])
        return {'label': prediction[0]}

api.add_resource(getLabel, '/')

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
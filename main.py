from flask import Flask
from flask_restful import Api
import config as conf
from routes import Etherscan

app = Flask(__name__)
api = Api(app)


api.add_resource(Etherscan, '/etherscan')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=conf.PORT, debug=True)
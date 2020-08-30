from models.modules.core import app, jsonify, InvalidUsage
from controllers.email import *
from models.modules.jwt import *

@app.route('/subscribers', methods=['GET'])
@validate_token
def getallSubscribersRoute():
    try:
        return Newsletter.getAllSubscribers()
    except Exception as e:
        raise InvalidUsage(str(e), status_code=500)

@app.route('/subscribers', methods=['POST'])
@validate_token
def addSubscriber():
    try:
        return Newsletter.subscribe_user()
    except Exception as e:
        raise InvalidUsage(str(e), status_code=500)

@app.route('/unsubscribe/<value>', methods=['DELETE'])
@validate_token
def unsubscribeProvider(value):
    try:
        return Newsletter.unsubscribe(value)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=500)
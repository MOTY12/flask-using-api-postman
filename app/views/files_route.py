from models.modules.core import app, jsonify, InvalidUsage, send_from_directory
from controllers.files import *
from models.modules.jwt import *

@app.route('/files/<path>/<filename>', methods=['GET'])
def get_file(path, filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'] + '/'+ path, filename)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=500)

@app.route('/files/<path>', methods=['GET'])
@validate_token
def get_folder(path):
    try:
        return Files.getAllFiles(path)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=500)

@app.route('/files/<path>/upload', methods=['POST'])
@validate_token
def upload_file(path):
    try:
        return Files.uploadProfileImage(path)
    except Exception as e:
        raise InvalidUsage(str(e), status_code=500)
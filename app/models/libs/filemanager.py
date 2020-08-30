from models.modules.core import app, os, secure_filename, url_for, jsonify

def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

def list_files(path = "/"):
    try:
        files = []
        target = os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'] + path)
        for filename in os.listdir(target):
            path = os.path.join(target, filename)
            if os.path.isfile(path):
                filename = secure_filename(filename)
                files.append(filename)
        return files
    except Exception as e:
        raise Exception(str(e))

def upload_image(fileInfo, path = "/"): 
    try:
        target = os.path.join(os.path.dirname(__file__), app.config['UPLOAD_FOLDER'] + path)
        
        if not os.path.isdir(target):
            os.mkdir(target)

        for file in fileInfo:
            filename = file.filename
            if filename == '':
                return { 'error': 'No selected file' }
            if filename and allowed_file(filename) == True:
                filename = secure_filename(filename)
                destination = "/".join([target, filename])
                file.save(destination)
            else:
                raise Exception("File upload terminated")
        return filename
    except Exception as e:
        raise Exception(str(e))

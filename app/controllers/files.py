from models.modules.core import logger, request, InvalidUsage, make_response, app, url_for
from models.libs.filemanager import upload_image, list_files

class Files():
    def getAllFiles(path):
        try:
            file_list = list_files("/" + path)
            files = []
            for filename in file_list:
                file_url = url_for("get_file", filename=filename, path=path)
                files.append(app.config['URL'] + file_url)
            return make_response({
                "message": files
            }, 200)
        except Exception as e:
            raise Exception(str(e))

    def uploadProfileImage(path):
        try:
            resp = upload_image(request.files.getlist('file'), "/" + path)
            file_url = url_for("get_file", filename=resp, path=path)
            return  make_response({
                "message": {
                    "upload_url": app.config['URL'] + file_url
                },
            }, 200)
        except Exception as e:
            raise Exception(str(e))
from models.modules.core import logger, request, InvalidUsage, make_response, app, url_for
from models.libs.filemanager import upload_image
from models.dbmodels.user_model import *
from models.modules.jwt import *
from datetime import datetime
import os

class Blog():
    def blog_all_post():
        try:
            blogs = Blog.query.all()
            return {
                "message": blogs_scheme.dump(blogs)[::-1]
            }
        except exc.SQLAlchemyError as e:
            raise Exception(e._message)
        except Exception as e:
            raise Exception(str(e))
    def 
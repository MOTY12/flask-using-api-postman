from models.modules.core import app
from views.route import *


if __name__ == "__main__":
    app.run(debug=True,
    use_reloader = True)
    

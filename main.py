from flask import Flask
import os

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'View/templates'))
app = Flask(__name__, template_folder=template_dir)

from Controller.views import init_routes
init_routes(app)

if __name__ == '__main__':
    app.run()


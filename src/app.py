from flask import Flask
from flask_cors import CORS

from config import config

# Routes    //aca es donde se importan las rutas que creamos
from routes import Movie

app = Flask(__name__)

# El puerto que decidimos depende del puerto de la aplicacion con la que corremos el programa.
# CORS(app, resources={"*": {"origins": "http://localhost:9300"}})


def page_not_found(error):
    return "<h1>Not found page<h1>", 404


if __name__ == '__main__':
    app.config.from_object(config['development'])

    # BLue prints // las cuales son las rutas de la aplicacion
    app.register_blueprint(Movie.main, url_prefix='/api/movies')

    # Error Handlers
    app.register_error_handler(404, page_not_found)
    app.run()

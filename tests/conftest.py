import pytest
from flask import Flask
from config import config
from routes import Movie
from app import app as flask_app

flask_app.config.from_object(config['testing'])


app_context = flask_app.app_context()
app_context.push()


@pytest.fixture
def app():

    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def cleanup_app_context():
    app_context.pop()

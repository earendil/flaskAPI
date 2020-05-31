import pytest

from api.api import app


@pytest.fixture(scope='module')
def test_client():
    flask_app = app
    app.testing = True
    app.debug = True

    testing_client = flask_app.test_client()

    context = flask_app.app_context()
    context.push()

    yield testing_client

    context.pop()

import sys
sys.path.append('.')
sys.path.append('./packages/')
sys.path.append('./packages/ml_api')
sys.path.append('./packages/ml_api/api')

from api.config import TestingConfig
from api.app import create_app
import pytest
import sys
sys.path.append('.')


@pytest.fixture
def app():
    app = create_app(config_object=TestingConfig)

    with app.app_context():
        yield app


@pytest.fixture
def flask_test_client(app):
    with app.test_client() as test_client:
        yield test_client


print('done!!!')

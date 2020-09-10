from api.app import create_app
from api.config import DevelopmentConfig, ProductionConfig


application = create_app()


if __name__ == '__main__':
    application.run()

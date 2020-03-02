from os import system

from flask import Flask
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app.app import create_app
from app.db import create_db
from app.jwt import create_jwt
from app.models import Good, User, Category, Busket


app: Flask = create_app()
CORS(app)
db: SQLAlchemy = create_db(app)
jwt: JWTManager = create_jwt(app)
manager: Manager = Manager(app)
migrate: Migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def run():
    system('python manage.py db upgrade')
    app.run(debug=True, host="0.0.0.0", port=5000)


if __name__ == '__main__':
    manager.run()

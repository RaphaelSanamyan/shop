from os import environ as env

DEBUG = True
SECRET_KEY = "FKO2-F0OJ-O]j4fgj"
SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@postgresql:5432/{}".format(
    env.get("DBUSER"),
    env.get("DBPASS"),
    env.get("DBNAME")
)
SQLALCHEMY_TRACK_MODIFICATIONS = True
RESTPLUS_MASK_SWAGGER = False
JWT_SECRET_KEY = "hn9grzAnEQBsEE9E"

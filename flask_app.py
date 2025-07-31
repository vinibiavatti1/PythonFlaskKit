from flask import Flask, g
from app.enums.env_enum import EnvEnum
from app.props import props
from app.blueprints import blueprints


g.env = EnvEnum.PROD
app = Flask(__name__)
app.secret_key = props['secret_key']
[app.register_blueprint(x) for x in blueprints]
print(f'Running in {g.env} environment!')

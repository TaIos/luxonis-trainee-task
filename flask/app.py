from configparser import ConfigParser

from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask import render_template


def read_and_validate_config(path: str) -> ConfigParser:
    cfg = ConfigParser(allow_no_value=True)
    cfg.read(path)
    if not cfg.has_section('postgresql'):
        raise ValueError(f'Invalid config file [{path}], no section [postgresql]')
    return cfg


cfg_pg = read_and_validate_config(path='database.ini')['postgresql']
db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    f'postgresql://{cfg_pg["user"]}:{cfg_pg["password"]}@{cfg_pg["host"]}:{cfg_pg["port"]}/{cfg_pg["database"]}'
db.init_app(app)


class Advertisements(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(100), nullable=False)
    scraped_hash_id = db.Column(db.String(100), nullable=False)


@app.route('/')
def home():
    advertisements = db.session.execute(db.select(Advertisements).order_by(Advertisements.id)).scalars()
    return render_template("index.html", advertisements=advertisements)


if __name__ == '__main__':
    app.run(debug=True)

import os

from flask_sqlalchemy import SQLAlchemy

from flask import Flask
from flask import render_template

print()


def retrieve_db_url_with_secrets() -> str:
    user = os.environ['POSTGRES_USER']
    password = os.environ['POSTGRES_PASSWORD']
    database = os.environ['POSTGRES_DB']
    host = os.environ['POSTGRES_HOST']
    port = os.environ['POSTGRES_PORT']
    return f'postgresql://{user}:{password}@{host}:{port}/{database}'


db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = retrieve_db_url_with_secrets()
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

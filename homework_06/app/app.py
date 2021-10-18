import os
import json
from urllib.request import urlopen
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.exc import IntegrityError, DatabaseError

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

PG_USER = os.environ.get("PG_USER")
PG_PASS = os.environ.get("PG_PASS")
PG_HOST = os.environ.get("PG_HOST")
PG_DB = os.environ.get("PG_DB")
PG_CONN_URI = 'postgresql://{}:{}@{}/{}'.format(PG_USER, PG_PASS, PG_HOST, PG_DB)

app = Flask(__name__)
db = SQLAlchemy()

app.config.update(
    SQLALCHEMY_DATABASE_URI=PG_CONN_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(app)
migrate = Migrate(app, db)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(50), nullable=False)
    posts = db.relationship("Post", back_populates='user')


class Post(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    title = db.Column(db.Text, nullable=False, default="")
    body = db.Column(db.Text, nullable=False, default="")
    user = db.relationship("User", back_populates='posts')


def fetch_data(url: str):
    resp = urlopen(url)
    resp_json = json.loads(resp.read().decode())
    return resp_json


def user_create(user_data):
    for user in user_data:
        db.session.add(
            User(
                name=user["name"],
                username=user["username"],
                email=user["email"]
            ))
    try:
        db.session.commit()
    except (IntegrityError, DatabaseError) as e:
        print(e)
        db.session.rollback()


def post_create(post_data):
    for post in post_data:
        db.session.add(
            Post(
                user_id=post['userId'],
                title=post['title'],
                body=post['body']
            ))
    try:
        db.session.commit()
    except (IntegrityError, DatabaseError) as e:
        print(e)
        db.session.rollback()


@app.route("/")
def home():
    users = User.query.all()
    return render_template("index.html", users=users)


@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/load", endpoint="loads")
def loads():
    user_create(fetch_data(USERS_DATA_URL))
    post_create(fetch_data(POSTS_DATA_URL))
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)

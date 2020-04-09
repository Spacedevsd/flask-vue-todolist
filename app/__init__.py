from flask import Flask, render_template
from flask_vuejs import Vue
from flask_marshmallow import Marshmallow
from flask_pymongo import PyMongo

vue = Vue()
ma = Marshmallow()
mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = "mongodb://localhost:27017/todos"

    vue.init_app(app)
    ma.init_app(app)
    mongo.init_app(app)

    @app.route("/")
    def base():
        return render_template("base.html")


    from . import views
    app.register_blueprint(views.todos)

    return app
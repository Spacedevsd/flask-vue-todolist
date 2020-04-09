from flask import Blueprint, jsonify, request
from . import schema
from . import mongo
from bson import ObjectId


todos = Blueprint("todos", __name__, url_prefix="/ws/v1/todos")


@todos.route("/")
def gettodos():
    schemas = schema.TodoSchema(many=True)
    todos_list = mongo.db.todos.find()
    return jsonify(schemas.dump(todos_list))


@todos.route("/insert", methods=["POST"])
def addtodos():
    data = request.get_json()
    mongo.db.todos.insert_one(data)

    schemas = schema.TodoSchema()  
    return jsonify(schemas.dump(data))


@todos.route("/close/<_id>", methods=["PUT"])
def closetodo(_id):
    todo = mongo.db.todos.update_one({"_id": ObjectId(_id)}, {
        "$set": {"status": False}})
    return jsonify({"modified": todo.modified_count })

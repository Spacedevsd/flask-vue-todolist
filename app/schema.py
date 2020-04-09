from . import ma
from marshmallow.fields import String
from bson import ObjectId 

ma.Schema.TYPE_MAPPING[ObjectId] = String

class TodoSchema(ma.Schema):
    class Meta:
        fields = ("_id", "name", "status")


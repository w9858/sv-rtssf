from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import recipe_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

recipe = Blueprint("api-recipe")



@recipe.post("/recipe/<path:path>")
async def recipe_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return recipe_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
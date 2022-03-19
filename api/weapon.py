from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import weapon_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

weapon = Blueprint("api-weapon")



@weapon.post("/weapon/<path:path>")
async def weapon_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return weapon_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
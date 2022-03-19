from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import unit_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

unit = Blueprint("api-unit")



@unit.post("/unit/<path:path>")
async def unit_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return unit_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
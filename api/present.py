from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import present_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

present = Blueprint("api-present")



@present.post("/present/<path:path>")
async def present_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return present_(request, pb.Request(), pb.Response())
    if (any): return empty() # empty return
    else: raise exceptions.NotFound()
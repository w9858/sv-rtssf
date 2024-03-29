from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import tips_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

tips = Blueprint("api-tips")



@tips.post("/tips/<path:path>")
async def tips_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return tips_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import gamecenter_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

gamecenter = Blueprint("api-gamecenter")



@gamecenter.post("/gamecenter/<path:path>")
async def gamecenter_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return gamecenter_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
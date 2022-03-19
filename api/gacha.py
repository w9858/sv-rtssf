from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import gacha_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

gacha = Blueprint("api-gacha")



@gacha.post("/gacha/<path:path>")
async def gacha_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return gamecenter_(request, pb.Request(), pb.Response())
    if (any): return empty() # empty return
    else: raise exceptions.NotFound()
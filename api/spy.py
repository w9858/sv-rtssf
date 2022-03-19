from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import spy_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

spy = Blueprint("api-spy")



@spy.post("/spy/<path:path>")
async def spy_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return spy_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
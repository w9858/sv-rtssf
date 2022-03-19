from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import achievement_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

achievement = Blueprint("api-achievement")



@achievement.post("/achievement/<path:path>")
async def achievement_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return achievement_(request, pb.RequestAdvStart(), pb.ResponseAdvStart())
    if (any): return empty() # empty return
    else: raise exceptions.NotFound()
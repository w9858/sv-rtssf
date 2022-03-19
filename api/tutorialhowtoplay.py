from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import tutorialhowtoplay_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

tutorialhowtoplay = Blueprint("api-tutorialhowtoplay")

def tutorialhowtoplay_save(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    return empty()

@tutorialhowtoplay.post("/tutorialhowtoplay/<path:path>")
async def tutorialhowtoplay_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "save"): return tutorialhowtoplay_save(request, pb.RequestSave(), pb.ResponseSave())
    else: raise exceptions.NotFound()
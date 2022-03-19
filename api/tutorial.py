from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import tutorial_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

tutorial = Blueprint("api-tutorial")

def tutorial_adv_start(request, pbrq, pbrs):
    pbrs.script_file = input("script: ")
    return raw(pbrs.SerializeToString())

@tutorial.post("/tutorial/<path:path>")
async def tutorial_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "adv_start"): return tutorial_adv_start(request, pb.RequestAdvStart(), pb.ResponseAdvStart())
    if (path == "adv_clear"): return empty()
    if (path == "update_progress"): return empty()
    else: raise exceptions.NotFound()
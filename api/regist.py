from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import regist_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

regist = Blueprint("api-regist")

def regist_check(request,pbrq,pbrs):
    pbrs.is_register = True
    pbrs.is_review = False
    pbrs.master_check_user = 0
    pbrs.sqlite_ver = 81
    return raw(pbrs.SerializeToString())

@regist.post("/regist/<path:path>")
async def regist_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "check"): return regist_check(request, pb.RequestCheck(), pb.ResponseCheck())
    else: raise exceptions.NotFound()
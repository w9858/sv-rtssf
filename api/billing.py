from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import billing_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

billing = Blueprint("api-billing")

def billing_top(request,pbrq,pbrs):
    pbrs.registered_birthday = 1
    return raw(pbrs.SerializeToString())

@billing.post("/billing/<path:path>")
async def billing_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "top"): return billing_top(request, pb.RequestTop(), pb.ResponseTop())
    else: raise exceptions.NotFound()
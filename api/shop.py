from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import shop_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

shop = Blueprint("api-shop")



@shop.post("/shop/<path:path>")
async def shop_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return shop_(request, pb.Request(), pb.Response())
    if (any): request.ctx.errorcode = 201; return empty() # empty maintain return
    else: raise exceptions.NotFound()
from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import exchange_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

exchange = Blueprint("api-exchange")



@exchange.post("/exchange/<path:path>")
async def exchange_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return exchange_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
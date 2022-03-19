from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import item_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

item = Blueprint("api-item")

def item_stamina_recover(request, pbrq, pbrs):
    jf.Parse(cm.read("t_user_item_list"), pbrs)
    jf.Parse(cm.load_worker(), pbrs.t_user_worker)
    return raw(pbrs.SerializeToString())

@item.post("/item/<path:path>")
async def item_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "stamina_recover"): return item_stamina_recover(request, pb.RequestStaminaRecover(), pb.ResponseStaminaRecover())
    else: raise exceptions.NotFound()
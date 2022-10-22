from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import weapon_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

weapon = Blueprint("api-weapon")

def weapon_equip(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    logger.info("\n"+str(pbrq))
    cm.weapon_equip(pbrq.unit_id, pbrq.user_weapon_id)
    jf.Parse(cm.read("t_user_unit_weapon_list"), pbrs)
    if(pbrq.user_weapon_id == 0):
        pbrs.deleted_list.add()
        pbrs.deleted_list[0].user_id = 0
        pbrs.deleted_list[0].unit_id = pbrq.unit_id
        pbrs.deleted_list[0].user_weapon_id = 0
    return raw(pbrs.SerializeToString())

@weapon.post("/weapon/<path:path>")
async def weapon_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == ""): return weapon_(request, pb.Request(), pb.Response())
    else: raise exceptions.NotFound()
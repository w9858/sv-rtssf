from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import eventmap_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

eventmap = Blueprint("api-eventmap")

def eventmap_get(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.t_user_event.event_id = pbrq.event_id
    pbrs.t_user_event.point = 10000000
    pbrs.t_user_event.max_point = 10000000
    pbrs.is_first_access = False
    pbrs.exists_new_clear_event_achievement = False
    pbrs.current_rank = 1
    jf.Parse(cm.read("t_user_quest_list"), pbrs)
    return raw(pbrs.SerializeToString())

@eventmap.post("/eventmap/<path:path>")
async def eventmap_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    # if (path == ""): return eventmap_(request, pb.Request(), pb.Response())
    if (path == "get"): return eventmap_get(request, pb.RequestGet(), pb.ResponseGet())
    if (path == "get_ranking"): return empty()
    else: raise exceptions.NotFound()
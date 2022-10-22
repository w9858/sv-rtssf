from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import spy_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

spy = Blueprint("api-spy")

def spy_get_list(request,pbrq,pbrs):
    for i in range(5):
        pbrs.t_user_spy_list.add()
        pbrs.t_user_spy_list[i].user_spy_id = i+1
        pbrs.t_user_spy_list[i].spy_id = 1000001+i
        pbrs.t_user_spy_list[i].state = 0
        pbrs.t_user_spy_list[i].subscription_flag = 1
    pbrs.today_work.max_count = 100
    pbrs.today_work.current_count = 0
    return raw(pbrs.SerializeToString())

@spy.post("/spy/<path:path>")
async def spy_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "get_list"): return spy_get_list(request, pb.RequestGetList(), pb.ResponseGetList())
    if (any): return empty()
    else: raise exceptions.NotFound()
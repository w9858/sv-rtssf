from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import board_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

board = Blueprint("api-board")

# ALL MAX

def board_release(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.t_user_board.unit_id = pbrq.unit_id
    pbrs.t_user_board.progress_1 = 2147483647
    pbrs.t_user_board.progress_2 = 2147483647
    pbrs.t_user_board.sheet_no = pbrq.sheet_no
    for j in range(4):
        pbrs.t_user_board.square_status_list.add()
        pbrs.t_user_board.square_status_list[j].is_release = True
        pbrs.t_user_board.square_status_list[j].square_id = j
    jf.Parse(cm.read("t_user_item_list"), pbrs)
    jf.Parse(cm.read("t_user"), pbrs)
    jf.Parse(cm.read("t_user_archive_list"), pbrs)
    return raw(pbrs.SerializeToString())

@board.post("/board/<path:path>")
async def board_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "release"): return board_release(request, pb.RequestRelease(), pb.ResponseRelease())
    else: raise exceptions.NotFound()
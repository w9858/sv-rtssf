from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import help_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

help = Blueprint("api-help")

def help_list(request,pbrq,pbrs):
    pbrs.m_help_list.add()
    pbrs.m_help_list[0].id = 1
    pbrs.m_help_list[0].category = 1
    pbrs.m_help_list[0].order = 1
    pbrs.m_help_list[0].title = "Style Infomation"
    pbrs.m_help_list[0].contents = "<img>1</img>\n   <color=#d6083b>紅蓮</color>, <color=#005198>靑藍</color>, <color=#191c1f>黑鉄</color>, \
<color=#b83d96>紫電</color>, <color=#5cc151>翡翠</color>, <color=#ffcc00>琥珀</color>"

    pbrs.m_help_list.add()
    pbrs.m_help_list[1].id = 2
    pbrs.m_help_list[1].category = 1
    pbrs.m_help_list[1].order = 2
    pbrs.m_help_list[1].title = "Contact"
    pbrs.m_help_list[1].contents = "\n\
    <color=#00acee>Twitter</color> : @gggk__  (two underbar)\n\n\
    <color=#ea4335>Email</color> : wjames9858@gmail.com\n\n\
    <color=#5865f2>Discord</color> : jhoon6#9050\n\n\
    <color=#6e5494>GitHub</color> : https://github.com/w9858"

    pbrs.m_help_list.add()
    pbrs.m_help_list[-1].id = 3
    pbrs.m_help_list[-1].category = 2
    pbrs.m_help_list[-1].order = 3
    pbrs.m_help_list[-1].title = "Meaningless title"
    pbrs.m_help_list[-1].contents = "meaningless contents"
    pbrs.m_help_list.add()
    pbrs.m_help_list[-1].id = 4
    pbrs.m_help_list[-1].category = 3
    pbrs.m_help_list[-1].order = 4
    pbrs.m_help_list[-1].title = "can't load other img"
    pbrs.m_help_list[-1].contents = "can load style table image only"

    pbrs.m_help_category_list.add()
    pbrs.m_help_category_list[0].category = 1
    pbrs.m_help_category_list[0].order = 1
    pbrs.m_help_category_list[0].name = "Helps"
    pbrs.m_help_category_list.add()
    pbrs.m_help_category_list[1].category = 2
    pbrs.m_help_category_list[1].order = 2
    pbrs.m_help_category_list[1].name = "Meaningless categoty"
    pbrs.m_help_category_list.add()
    pbrs.m_help_category_list[2].category = 3
    pbrs.m_help_category_list[2].order = 3
    pbrs.m_help_category_list[2].name = "TEST"

    return raw(pbrs.SerializeToString())

@help.post("/help/<path:path>")
async def help_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "list"): return help_list(request, pb.RequestList(), pb.ResponseList())
    else: raise exceptions.NotFound()
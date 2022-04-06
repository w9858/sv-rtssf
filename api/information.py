from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import information_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64, random

information = Blueprint("api-information")


def information_index(requset,pbrq,pbrs):
    chara_name = random.choice(["byakko","dolte","fu","goe","hatsume","kamari","katrina","lappa","mei","momo","monomi","theresia","yuki"])

    pbrs.m_information_tab_list.add()
    pbrs.m_information_tab_list[0].tab_id = 1
    pbrs.m_information_tab_list[0].name = "Information"
    pbrs.m_information_tab_list[0].order = 1

    pbrs.m_information_list.add()
    pbrs.m_information_list[0].information_id = 1
    pbrs.m_information_list[0].tab_id = 1
    pbrs.m_information_list[0].title = "Contact"
    pbrs.m_information_list[0].contents = "<color=#00acee>Twitter</color> : @gggk__  (two underbar)\n\n<color=#ea4335>Email</color> : wjames9858@gmail.com\n\n"+\
    "<color=#5865f2>Discord</color> : jhoon6#9050\n\n<color=#6e5494>GitHub</color> : https://github.com/w9858\n<img>https://w9858.github.io/220206/character/img/chara_"+chara_name+"_face.png</img>"
    pbrs.m_information_list[0].view_android = 1
    pbrs.m_information_list[0].pin_flag = 1

    pbrs.m_information_list.add()
    pbrs.m_information_list[1].information_id = 2
    pbrs.m_information_list[1].tab_id = 1
    pbrs.m_information_list[1].title = "<img>https://w9858.github.io/other/img/bannertest.png</img>"
    pbrs.m_information_list[1].contents = "PNG image from wikimedia, not saved in device local storage.\n"+\
    "Image From Wikimedia Commons, the free media repository\n<img>https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png</img>\n"+\
    "User:Ed g2s, CC BY-SA 3.0<https://creativecommons.org/licenses/by-sa/3.0>\n<img>Info/20190617/311010008</img>\n\nFile : /Info/20190617/311010008.png"
    pbrs.m_information_list[1].view_android = 1
    pbrs.m_information_list[1].pin_flag = 1

    pbrs.t_user_information_list.add()
    pbrs.t_user_information_list.add()
    pbrs.t_user_information_list[0].information_id = 1
    pbrs.t_user_information_list[1].information_id = 2

    return raw(pbrs.SerializeToString())

@information.post("/information/<path:path>")
async def information_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "index"): return information_index(request, pb.RequestIndex(), pb.ResponseIndex())
    if (path == "read"): return empty()
    else: raise exceptions.NotFound()
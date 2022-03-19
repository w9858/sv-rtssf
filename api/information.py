from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import information_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

information = Blueprint("api-information")


def information_index(requset,pbrq,pbrs):
    pbrs.m_information_tab_list.add()
    pbrs.m_information_tab_list[0].tab_id = 1
    pbrs.m_information_tab_list[0].name = "Information"
    pbrs.m_information_tab_list[0].order = 1

    pbrs.m_information_list.add()
    pbrs.m_information_list[0].information_id = 1
    pbrs.m_information_list[0].tab_id = 1
    pbrs.m_information_list[0].title = "<img>Info/1</img>"
    pbrs.m_information_list[0].contents = "<size=72><color=#F550A1>■ RRFR Infomation test</color></size>\ntesting\n<img>https://w9858.github.io/220206/character/img/chara_monomi_face.png</img>"
    pbrs.m_information_list[0].view_android = 1
    pbrs.m_information_list[0].pin_flag = 1

    pbrs.m_information_list.add()
    pbrs.m_information_list[1].information_id = 2
    pbrs.m_information_list[1].tab_id = 1
    pbrs.m_information_list[1].title = "<i>Text Title</i>"
    pbrs.m_information_list[1].contents = "<color=red>RED </color><color=green>GREEN </color><color=blue>BLUE </color><color=cyan>CYAN </color><color=yellow>YELLOW</color><color=magenta>MAGENTA </color><color=black>BLACK </color><color=orange><i><b>ORANGE</b></i> </color>default"
    pbrs.m_information_list[1].view_android = 1
    pbrs.m_information_list[1].pin_flag = 1

    pbrs.m_information_list.add()
    pbrs.m_information_list[2].information_id = 3
    pbrs.m_information_list[2].tab_id = 1
    pbrs.m_information_list[2].title = "PNG images"
    pbrs.m_information_list[2].contents = "PNG image from network, not saved in device local storage.\nImage From Wikimedia Commons, the free media repository\n<img>https://upload.wikimedia.org/wikipedia/commons/4/47/PNG_transparency_demonstration_1.png</img>\nUser:Ed g2s, CC BY-SA 3.0 <https://creativecommons.org/licenses/by-sa/3.0>\n<img>Info/20190617/311010008</img>\nImage from Serv&local"
    pbrs.m_information_list[2].view_android = 1
    pbrs.m_information_list[2].pin_flag = 1

    pbrs.m_information_list.add()
    pbrs.m_information_list[3].information_id = 4
    pbrs.m_information_list[3].tab_id = 1
    pbrs.m_information_list[3].title = "Contact"
    pbrs.m_information_list[3].contents = "<color=#00acee>Twitter</color> : @gggk__  (two underbar)\n\n<color=#ea4335>Email</color> : wjames9858@gmail.com\n\n<color=#5865f2>Discord</color> : jhoon6#9050\n\n<color=#6e5494>GitHub</color> : https://github.com/w9858"
    pbrs.m_information_list[3].view_android = 1
    pbrs.m_information_list[3].pin_flag = 1

    pbrs.t_user_information_list.add()
    pbrs.t_user_information_list.add()
    pbrs.t_user_information_list.add()
    pbrs.t_user_information_list.add()
    pbrs.t_user_information_list[0].information_id = 1
    pbrs.t_user_information_list[1].information_id = 2
    pbrs.t_user_information_list[2].information_id = 3
    pbrs.t_user_information_list[3].information_id = 4

    return raw(pbrs.SerializeToString())

@information.post("/information/<path:path>")
async def information_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "index"): return information_index(request, pb.RequestIndex(), pb.ResponseIndex())
    else: raise exceptions.NotFound()
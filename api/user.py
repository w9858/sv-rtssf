from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import user_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

user = Blueprint("api-user")

def user_change_comment(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_comment(pbrq.comment)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_comment(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_comment(pbrq.comment)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_emblem(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_emblem(pbrq.emblem_id)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_friend_unit(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_friend_unit(pbrq.unit_id)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_home_bg(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_home_bg(pbrq.background_id)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_home_unit_main(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_home_unit(pbrq.unit_id, 1)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_home_unit_sub(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_home_unit(pbrq.unit_id, 2)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_change_name(request, pbrq, pbrs):
    pbrq.ParseFromString(request.body)
    cm.change_name(pbrq.name)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def user_stamina_recover(request, pbrq, pbrs):
    jf.Parse(cm.load_worker(), pbrs.t_user_worker)
    return raw(pbrs.SerializeToString())

@user.post("/user/<path:path>")
async def user_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "change_comment"): return user_change_comment(request, pb.RequestChangeComment(), pb.ResponseChangeComment())
    if (path == "change_emblem"): return user_change_emblem(request, pb.RequestChangeEmblem(), pb.ResponseChangeEmblem())
    if (path == "change_friend_unit"): return user_change_friend_unit(request, pb.RequestChangeFriendUnit(), pb.ResponseChangeFriendUnit())
    if (path == "change_home_bg"): return user_change_home_bg(request, pb.RequestChangeHomeBg(), pb.ResponseChangeHomeBg())
    if (path == "change_home_unit_main"): return user_change_home_unit_main(request, pb.RequestChangeHomeUnitMain(), pb.ResponseChangeHomeUnitMain())
    if (path == "change_home_unit_sub"): return user_change_home_unit_sub(request, pb.RequestChangeHomeUnitSub(), pb.ResponseChangeHomeUnitSub())
    if (path == "change_name"): return user_change_name(request, pb.RequestChangeName(), pb.ResponseChangeName())
    if (path == "stamina_recover"): return user_stamina_recover(request, pb.RequestStaminaRecover(), pb.ResponseStaminaRecover())
    if (path == "get_stamina_recover"): return empty()
    else: raise exceptions.NotFound()
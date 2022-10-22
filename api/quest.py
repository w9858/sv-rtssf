from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import quest_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64, random

quest = Blueprint("api-quest")


def quest_start_adv(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.token = "token"
    return raw(pbrs.SerializeToString())

def quest_clear_adv(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.t_user_quest.quest_id = pbrq.quest_id
    pbrs.t_user_quest.clear_count = 1
    pbrs.t_user_quest_status.quest_id = pbrq.quest_id
    pbrs.t_user_quest_status.token = "token"
    pbrs.t_user_quest_status.start_at = "2020-03-31 15:00:00"
    pbrs.t_user_quest_status.end_at = "2020-03-31 15:00:00"
    cm.adv_clear(pbrq.quest_id)
    jf.Parse(cm.read("t_user"), pbrs)
    return raw(pbrs.SerializeToString())

def quest_start(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.token = "token"
    return raw(pbrs.SerializeToString())

def quest_clear(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.is_friend = True
    pbrs.is_unlock_spy_frame = False
    pbrs.t_user_quest.quest_id = pbrq.quest_id
    pbrs.t_user_quest.clear_count = 1
    pbrs.t_user_quest_status.quest_id = pbrq.quest_id
    pbrs.t_user_quest.quest_mission_id_1 = pbrq.is_clear_mission_1
    pbrs.t_user_quest.quest_mission_id_2 = pbrq.is_clear_mission_2
    pbrs.t_user_quest.quest_mission_id_3 = pbrq.is_clear_mission_3
    pbrs.t_user_quest_status.token = "token"
    pbrs.t_user_quest_status.start_at = "2022-02-15 19:30:44"
    pbrs.t_user_quest_status.end_at = "2022-02-15 19:30:44"
    pbrs.t_user_quest.rank = 0
    pbrs.drop_list.add()
    pbrs.drop_list[0].resource_type = 1
    pbrs.drop_list[0].resource_id = 101070101
    pbrs.drop_list[0].resource_value_id = 1
    pbrs.drop_list[0].amount = 5
    pbrs.drop_list.add()
    pbrs.drop_list[1].resource_type = 1
    pbrs.drop_list[1].resource_id = 101070201
    pbrs.drop_list[1].resource_value_id = 1
    pbrs.drop_list[1].amount = 5
    pbrs.drop_list.add()
    pbrs.drop_list[2].resource_type = 1
    pbrs.drop_list[2].resource_id = 101070301
    pbrs.drop_list[2].resource_value_id = 1
    pbrs.drop_list[2].amount = 5
    pbrs.drop_list.add()
    pbrs.drop_list[3].resource_type = 1
    pbrs.drop_list[3].resource_id = 101070401
    pbrs.drop_list[3].resource_value_id = 1
    pbrs.drop_list[3].amount = 5
    pbrs.mission_complete_reward_list.add()
    pbrs.mission_complete_reward_list[0].resource_type = 1
    pbrs.mission_complete_reward_list[0].resource_id = 190101001
    pbrs.mission_complete_reward_list[0].resource_value_id = 1
    pbrs.mission_complete_reward_list[0].amount = 1
    jf.Parse(cm.read("t_user_character_friendly_list"), pbrs)
    jf.Parse(cm.read("t_user_archive_list"), pbrs)

    cm.add_user_exp(180)
    cm.add_user_friend_point(20)
    cm.add_user_gold(random.choice([8000, 5000, 12000, 2500]))

    cm.quest_clear(pbrq.quest_id,pbrq.is_clear_mission_1,pbrq.is_clear_mission_2,pbrq.is_clear_mission_3)

    pbrs.update_resource_result.MergeFrom(cm.update_resource_result())
    return raw(pbrs.SerializeToString())


def quest_fail(request,pbrq,pbrs):
    pbrs.update_resource_result.MergeFrom(cm.update_resource_result())
    return raw(pbrs.SerializeToString())

def quest_retire(request,pbrq,pbrs):
    pbrs.update_resource_result.MergeFrom(cm.update_resource_result())
    return raw(pbrs.SerializeToString())

def quest_continue(request,pbrq,pbrs):
    pbrs.update_resource_result.MergeFrom(cm.update_resource_result())
    return raw(pbrs.SerializeToString())

@quest.post("/quest/<path:path>")
async def quest_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "start_adv"): return quest_start_adv(request, pb.RequestStartAdv(), pb.ResponseStartAdv())
    if (path == "clear_adv"): return quest_clear_adv(request, pb.RequestClearAdv(), pb.ResponseClearAdv())
    if (path == "start"): return quest_start(request, pb.RequestStart(), pb.ResponseStart())
    if (path == "clear"): return quest_clear(request, pb.RequestClear(), pb.ResponseClear())
    if (path == "retire"): return quest_retire(request, pb.RequestRetire(), pb.ResponseRetire())
    if (path == "fail"): return quest_fail(request, pb.RequestFail(), pb.ResponseFail())
    if (path == "continue"): return quest_continue(request, pb.RequestContinue(), pb.ResponseContinue())
    if (path == "get_continue_crystal"): return empty()
    
    
    else: raise exceptions.NotFound()
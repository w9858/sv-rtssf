from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import friend_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64, random

friend = Blueprint("api-friend")

def rand_chara():
    ssr_chara = [311001001, 311001008, 311001009, 311001010, 311001013, 311001014, 311001015, 311001020,\
                 311002001, 311002008, 311002009, 311002010, 311002013, 311002014, 311002021, 311003001,\
                 311003012, 311003010, 311003013, 311003014, 311003017, 311003018, 311004001, 311004008,\
                 311004010, 311004012, 311004013, 311004014, 311004015, 311004016, 311004019, 311004018,\
                 311005001, 311005008, 311005009, 311005010, 311005012, 311005013, 311005018, 311006001,\
                 311006008, 311006011, 311006013, 311006012, 311006015, 311006014, 311006018, 311006019,\
                 311007001, 311007003, 311007005, 311007009, 311008001, 311008005, 311008009, 311009005,\
                 311009010, 311009013, 311010008, 311010001, 311010012, 311010009, 311010013, 311010014,\
                 312001001, 312001007, 312001008, 312002001, 312002007, 312002008, 312003001, 312004001,\
                 312003007, 312004007, 312004008, 312004011, 313001001, 313001006, 313002001, 313002005,\
                 396006001, 394001001, 394002001, 394003001, 394004001, 396001001, 396002001, 396003001,\
                 396004001, 396005001]
    return random.sample(ssr_chara, k=len(ssr_chara))

def friend_get_list(request,pbrq,pbrs):
    for i in range(50):
        pbrs.user_profile_list.add()
        pbrs.user_profile_list[i].user_id = i+1
        pbrs.user_profile_list[i].view_user_id = i+1
        pbrs.user_profile_list[i].friend_point = i+1
        pbrs.user_profile_list[i].lv = i+1
        pbrs.user_profile_list[i].last_login = "2099-12-31 00:00:00"
        pbrs.user_profile_list[i].name = "DUMMY FRIEND " + str(i+1)
        pbrs.user_profile_list[i].comment = "こんにちは"
        pbrs.user_profile_list[i].friend_unit_id = rand_chara()[i]
        pbrs.user_profile_list[i].home_unit_id_1 = rand_chara()[i]
        pbrs.user_profile_list[i].friend_unit_rarity = 4
        pbrs.user_profile_list[i].home_background_id = 110100004
        pbrs.user_profile_list[i].is_friend = False
        pbrs.user_profile_list[i].emblem_id = 0

    return raw(pbrs.SerializeToString())

def friend_search(request,pbrq,pbrs):
    rand_id = random.randrange(1000000,9999999)

    pbrs.user_profile.user_id = rand_id
    pbrs.user_profile.view_user_id = rand_id
    pbrs.user_profile.friend_point = 500
    pbrs.user_profile.lv = 500
    pbrs.user_profile.last_login = "2099-12-31 00:00:00"
    pbrs.user_profile.name = "DUMMY FRIEND"
    pbrs.user_profile.comment = "こんにちは"
    pbrs.user_profile.friend_unit_id = rand_chara()[0]
    pbrs.user_profile.home_unit_id_1 = rand_chara()[0]
    pbrs.user_profile.friend_unit_rarity = 4
    pbrs.user_profile.home_background_id = 110100004
    pbrs.user_profile.is_friend = True
    pbrs.user_profile.emblem_id = 0

    return raw(pbrs.SerializeToString())

def friend_top(request,pbrq,pbrs):
    for i in range(50):
        pbrs.t_user_friend_list.add()
        pbrs.t_user_friend_list[i].user_id = i+1
        pbrs.t_user_friend_list[i].view_user_id = i+1
        pbrs.t_user_friend_list[i].friend_point = i+1
        pbrs.t_user_friend_list[i].lv = i+1
        pbrs.t_user_friend_list[i].last_login = "2099-12-31 00:00:00"
        pbrs.t_user_friend_list[i].name = "DUMMY FRIEND " + str(i+1)
        pbrs.t_user_friend_list[i].comment = "こんにちは"
        pbrs.t_user_friend_list[i].friend_unit_id = rand_chara()[i]
        pbrs.t_user_friend_list[i].home_unit_id_1 = rand_chara()[i]
        pbrs.t_user_friend_list[i].friend_unit_rarity = 4
        pbrs.t_user_friend_list[i].home_background_id = 110100004
        pbrs.t_user_friend_list[i].is_friend = False
        pbrs.t_user_friend_list[i].emblem_id = 0

    return raw(pbrs.SerializeToString())


@friend.post("/friend/<path:path>")
async def friend_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "get_list"): return friend_get_list(request, pb.RequestGetList(), pb.ResponseGetList())
    if (path == "search"): return friend_search(request, pb.RequestSearch(), pb.ResponseSearch())
    if (path == "top"): return friend_top(request, pb.RequestTop(), pb.ResponseTop())
    elif(any): return empty() # empty return
    else: raise exceptions.NotFound()
from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import load_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

load = Blueprint("api-load")

def load_split(request, pbrq, pbrs):
    pbrs.current_section = 1
    pbrs.max_section = 1

    jf.Parse(cm.read("t_user"), pbrs)
    jf.Parse(cm.read("t_user_crystal"), pbrs)
    jf.Parse(cm.read("t_user_unit_list"), pbrs)
    jf.Parse(cm.read("t_user_worker_list"), pbrs)
    jf.Parse(cm.read("t_user_quest_list"), pbrs)
    # jf.Parse(cm.read("t_user_quest_status"), pbrs)
    jf.Parse(cm.read("t_user_archive_list"), pbrs)
    jf.Parse(cm.read("t_user_count_list"), pbrs)
    jf.Parse(cm.read("t_user_unit_weapon_list"), pbrs)
    jf.Parse(cm.read("t_user_weapon_list"), pbrs)
    jf.Parse(cm.read("t_user_weapon_skill_list"), pbrs)
    jf.Parse(cm.read("t_user_weapon_status_list"), pbrs)
    # jf.Parse(cm.read("t_user_recipe_list"), pbrs)
    # jf.Parse(cm.read("t_user_board_list"), pbrs)
    jf.Parse(cm.read("t_user_tips_list"), pbrs)
    jf.Parse(cm.read("t_user_tutorial_how_to_play_list"), pbrs)
    jf.Parse(cm.read("t_user_deck_list"), pbrs)
    jf.Parse(cm.read("t_user_item_list"), pbrs)
    jf.Parse(cm.read("t_user_character_friendly_list"), pbrs)
    jf.Parse(cm.read("t_user_spy_list"), pbrs)
    jf.Parse(cm.read("t_user_spy_playing_list"), pbrs)
    jf.Parse(cm.read("t_user_subscription_list"), pbrs)
    jf.Parse(cm.read("t_user_background_list"), pbrs)
    jf.Parse(cm.read("t_user_emblem_list"), pbrs)
    jf.Parse(cm.read("t_user_board_list"), pbrs)

    return raw(pbrs.SerializeToString())

@load.post("/load/<path:path>")
async def load_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "split"): return load_split(request, pb.RequestSplit(), pb.ResponseSplit())
    if (path == "sqlite_versions"): return load_sqliteversions(request, pb.RequestSqliteVersions(), pb.ResponseSqliteVersions())
    else: raise exceptions.NotFound()

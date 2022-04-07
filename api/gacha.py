from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import gacha_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

gacha = Blueprint("api-gacha")

def gacha_list(request,pbrq,pbrs):
    pbrs.m_gacha_list.add()
    pbrs.m_gacha_list[0].gacha_id = 3010001
    pbrs.m_gacha_list[0].gacha_type = 1
    pbrs.m_gacha_list[0].order = 1
    pbrs.m_gacha_list[0].name = "TEST GACHA NAME"
    pbrs.m_gacha_list[0].header = "TEST GACHA HEADER"
    pbrs.m_gacha_list[0].description = "TEST GACHA DESCRIPTION"
    pbrs.m_gacha_list[0].background_id = 110401003
    pbrs.m_gacha_list[0].disp_term_flag = 0
    # pbrs.m_gacha_list[0].start_at = "1900-01-01 00:00:00"
    # pbrs.m_gacha_list[0].end_at = "2072-11-21 00:55:54"

    pbrs.m_gacha_feature_list.add()
    pbrs.m_gacha_feature_list.add()
    pbrs.m_gacha_feature_list.add()
    pbrs.m_gacha_feature_list.add()
    pbrs.m_gacha_feature_list.add()
    pbrs.m_gacha_feature_list.add()
    pbrs.m_gacha_feature_list[0].gacha_id = 3010001
    pbrs.m_gacha_feature_list[0].unit_id = 311001001
    pbrs.m_gacha_feature_list[0].order = 1
    pbrs.m_gacha_feature_list[1].gacha_id = 3010001
    pbrs.m_gacha_feature_list[1].unit_id = 311002001
    pbrs.m_gacha_feature_list[1].order = 2
    pbrs.m_gacha_feature_list[2].gacha_id = 3010001
    pbrs.m_gacha_feature_list[2].unit_id = 311003001
    pbrs.m_gacha_feature_list[2].order = 3
    pbrs.m_gacha_feature_list[3].gacha_id = 3010001
    pbrs.m_gacha_feature_list[3].unit_id = 311004001
    pbrs.m_gacha_feature_list[3].order = 3
    pbrs.m_gacha_feature_list[4].gacha_id = 3010001
    pbrs.m_gacha_feature_list[4].unit_id = 311005001
    pbrs.m_gacha_feature_list[4].order = 3
    pbrs.m_gacha_feature_list[5].gacha_id = 3010001
    pbrs.m_gacha_feature_list[5].unit_id = 311006001
    pbrs.m_gacha_feature_list[5].order = 3

    pbrs.m_gacha_normal_detail_list.add()
    pbrs.m_gacha_normal_detail_list[0].gacha_id = 3010001
    pbrs.m_gacha_normal_detail_list[0].detail_id = 30100011
    # pbrs.m_gacha_normal_detail_list[0].one_day_flag = 0
    pbrs.m_gacha_normal_detail_list[0].draw_count = 1
    pbrs.m_gacha_normal_detail_list[0].resource_type = 5
    pbrs.m_gacha_normal_detail_list[0].resource_id = 1
    pbrs.m_gacha_normal_detail_list[0].resource_value_id = 1
    pbrs.m_gacha_normal_detail_list[0].amount = 120
    pbrs.m_gacha_normal_detail_list[0].execution_limit = 0
    pbrs.m_gacha_normal_detail_list.add()
    pbrs.m_gacha_normal_detail_list[1].gacha_id = 3010001
    pbrs.m_gacha_normal_detail_list[1].detail_id = 30100012
    pbrs.m_gacha_normal_detail_list[1].draw_count = 10
    pbrs.m_gacha_normal_detail_list[1].resource_type = 5
    pbrs.m_gacha_normal_detail_list[1].resource_id = 1
    pbrs.m_gacha_normal_detail_list[1].resource_value_id = 1
    pbrs.m_gacha_normal_detail_list[1].amount = 1200
    pbrs.m_gacha_normal_detail_list[1].execution_limit = 0
    
    return raw(pbrs.SerializeToString())

def gacha_draw(request,pbrq,pbrs):
    # DOSEN'T WORK AT THIS TIME
    pbrq.ParseFromString(request.body)
    for i in range(10):
        pbrs.draw_result_list.add()
        pbrs.draw_result_list[0].resource_type = 3
        pbrs.draw_result_list[0].resource_id = 311001001
        pbrs.draw_result_list[0].resource_value_id = 311001001
        pbrs.draw_result_list[0].amount = 0

    # pbrs.omake_list.add()
    # pbrs.omake_list[0].resource_type = 3
    # pbrs.omake_list[0].resource_id = 311001001
    # pbrs.omake_list[0].resource_value_id = 311001001
    # pbrs.omake_list[0].amount = 1

    pbrs.t_user_gacha_normal.gacha_id = 3010001
    pbrs.t_user_gacha_normal.updated_at = "2022-04-20 00:55:54"
    pbrs.t_user_gacha_normal.execution_count = 0

    pbrs.t_user_gacha_normal_detail.gacha_id = 3010001
    pbrs.t_user_gacha_normal_detail.gacha_detail_id = 30100012
    pbrs.t_user_gacha_normal_detail.updated_at = "2022-04-20 00:55:54"
    pbrs.t_user_gacha_normal_detail.execution_count = 0

    # pbrs.update_resource_result.MergeFrom(cm.update_resource_result())

    # pbrs.effect_1 = 1000
    # pbrs.effect_2 = 1
    # pbrs.effect_3_list.extend([1,0,1,0,1,0,1,0,1,0])
    return raw(pbrs.SerializeToString())

@gacha.post("/gacha/<path:path>")
async def gacha_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "list"): return gacha_list(request, pb.RequestList(), pb.ResponseList())
    # if (path == "draw"): return gacha_draw(request, pb.RequestDraw(), pb.ResponseDraw())
    else: raise exceptions.NotFound()
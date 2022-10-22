from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import gacha_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64, random

ssr_rate = 20
sr_rate = 30
r_rate = 50

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
ssr_effect_3 = [3,4,5,6,7,8]

sr_chara = [311001016,311001019,311001022,311002004,311002007,311002017,311002018,311003004,311003007,\
            311003008,311003009,311003015,311004004,311004007,311004009,311004021,311005004,311005007,\
            311006004,311006007,311006010,311006016,311006021,311008010,311009011,311010015,312002009,\
            312003008,311001004,311001007,311001012]

r_chara = [311001003,311001006,311002003,311002006,311003003,311003006,311004003,311004006,311005003,\
           311005006,311006003,311006006,311009003,311010003,312001002,312002002,312003002,312004002]

def draw():
    roll = random.random() * 100
    if roll < r_rate:
        out_chara = random.choice(r_chara)
        return [out_chara,1]
    elif roll >= r_rate and roll < (r_rate + sr_rate):
        out_chara = random.choice(sr_chara)
        return [out_chara,2]
    else:
        out_chara = random.choice(ssr_chara)
        out_effect = random.choice(ssr_effect_3)
        return [out_chara,out_effect]

gacha = Blueprint("api-gacha")

def gacha_list(request,pbrq,pbrs):
    pbrs.m_gacha_list.add()
    pbrs.m_gacha_list[0].gacha_id = 3010001
    pbrs.m_gacha_list[0].gacha_type = 1
    pbrs.m_gacha_list[0].order = 1
    pbrs.m_gacha_list[0].name = "TEST GACHA"
    pbrs.m_gacha_list[0].header = "HEADER"
    pbrs.m_gacha_list[0].description = "DESCRIPTION"
    pbrs.m_gacha_list[0].background_id = 110401003
    pbrs.m_gacha_list[0].disp_term_flag = 0
    pbrs.m_gacha_list[0].start_at = "1900-01-01 00:00:00"
    pbrs.m_gacha_list[0].end_at = "2072-11-21 00:55:54"

    # gacha_feature_chara_list = [311001001,311001004,311001007,311001008,311001009,311001010,311001013,311001014,\
    #     311001015,311001016,311001020,311002001,311002004,311002007,311002008,311002009,311002010,311002013,\
    #     311002014,311002017,311002021,311003001,311003004,311003007,311003008,311003010,311003012,311003013,\
    #     311003014,311003017,311003018,311004001,311004004,311004007,311004008,311004010,311004012,311004013,\
    #     311004014,311004015,311004018,311004019,311005001,311005004,311005007,311005008,311005009,311005010,\
    #     311005012,311005013,311005018,311006001,311006004,311006007,311006008,311006010,311006011,311006012,\
    #     311006013,311006014,311006016,311006019,311007001,311007003,311007005,311008001,311008005,311008009,\
    #     311009005,311009010,311009011,311009013,311010001,311010008,311010009,311010012,311010013,311010014,\
    #     312001001,312001007,312001008,312002001,312002007,312002008,312002009,312003001,312003007,312004001,\
    #     312004007,312004008,312004011,313001001,313001006,313002001,313002005,394001001,394002001,394003001,\
    #     394004001,396001001,396002001,396003001,396004001,396005001,396006001] # all available features..

    gacha_feature_chara_list = [311001001,311002001,311003001,311004001,311005001,311006001]
    
    for i in gacha_feature_chara_list:
        pbrs.m_gacha_feature_list.add()
        pbrs.m_gacha_feature_list[-1].gacha_id = 3010001
        pbrs.m_gacha_feature_list[-1].unit_id = i
        pbrs.m_gacha_feature_list[-1].order = 1

    pbrs.m_gacha_normal_detail_list.add()
    pbrs.m_gacha_normal_detail_list[-1].gacha_id = 3010001
    pbrs.m_gacha_normal_detail_list[-1].detail_id = 30100011
    pbrs.m_gacha_normal_detail_list[-1].one_day_flag = 0
    pbrs.m_gacha_normal_detail_list[-1].draw_count = 1
    pbrs.m_gacha_normal_detail_list[-1].resource_type = 6
    pbrs.m_gacha_normal_detail_list[-1].resource_id = 2
    pbrs.m_gacha_normal_detail_list[-1].resource_value_id = 2
    pbrs.m_gacha_normal_detail_list[-1].amount = 0
    pbrs.m_gacha_normal_detail_list[-1].execution_limit = 0
    pbrs.m_gacha_normal_detail_list.add()
    pbrs.m_gacha_normal_detail_list[-1].gacha_id = 3010001
    pbrs.m_gacha_normal_detail_list[-1].detail_id = 30100012
    pbrs.m_gacha_normal_detail_list[-1].one_day_flag = 0
    pbrs.m_gacha_normal_detail_list[-1].draw_count = 10
    pbrs.m_gacha_normal_detail_list[-1].resource_type = 6
    pbrs.m_gacha_normal_detail_list[-1].resource_id = 2
    pbrs.m_gacha_normal_detail_list[-1].resource_value_id = 2
    pbrs.m_gacha_normal_detail_list[-1].amount = 0
    pbrs.m_gacha_normal_detail_list[-1].execution_limit = 0
    return raw(pbrs.SerializeToString())

def gacha_draw(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    if pbrq.detail_id == 30100011: draw_count = 1
    elif pbrq.detail_id == 30100012: draw_count = 10
    else: draw_count = 10

    for i in range(draw_count):
        rs = draw()
        pbrs.draw_result_list.add()
        pbrs.draw_result_list[i].resource_type = 3
        pbrs.draw_result_list[i].resource_id = rs[0]
        pbrs.draw_result_list[i].resource_value_id = 1
        pbrs.draw_result_list[i].amount = 1
        pbrs.effect_3_list.append(rs[1])

    eff = random.choice([1,1,1,2,2,3])
    pbrs.effect_1 = eff
    pbrs.effect_2 = eff
    # pbrs.effect_3_list.extend([1,2,3,4,5,6,7,8,3,2])

    # pbrs.omake_list.add()
    # pbrs.omake_list[0].resource_type = 4
    # pbrs.omake_list[0].resource_id = 1
    # pbrs.omake_list[0].resource_value_id = 1
    # pbrs.omake_list[0].amount = 1000

    pbrs.t_user_gacha_normal.gacha_id = 3010001
    pbrs.t_user_gacha_normal.updated_at = "2022-04-20 00:55:54"
    pbrs.t_user_gacha_normal.execution_count = 1

    pbrs.t_user_gacha_normal_detail.gacha_id = 3010001
    pbrs.t_user_gacha_normal_detail.gacha_detail_id = 30100011
    pbrs.t_user_gacha_normal_detail.updated_at = "2022-04-20 00:55:54"
    pbrs.t_user_gacha_normal_detail.execution_count = 1

    pbrs.update_resource_result.MergeFrom(cm.update_resource_result())
    return raw(pbrs.SerializeToString())

def gacha_rate_list(request,pbrq,pbrs):
    for i in range(5):
        pbrs.normal_gacha.rare_rate_list.add()
        pbrs.normal_gacha.rare_rate_list[i].rare = i+1
        pbrs.normal_gacha.rare_rate_list[i].rate = "0"
    pbrs.normal_gacha.rare_rate_list[1].rate = str(r_rate)
    pbrs.normal_gacha.rare_rate_list[2].rate = str(sr_rate)
    pbrs.normal_gacha.rare_rate_list[3].rate = str(ssr_rate)
    # pbrs.normal_gacha.rare_rate_list[-1].resource_rate_list.add()
    # pbrs.normal_gacha.rare_rate_list[-1].resource_rate_list[-1].resource_type = 1
    # pbrs.normal_gacha.rare_rate_list[-1].resource_rate_list[-1].resource_id = 1
    # pbrs.normal_gacha.rare_rate_list[-1].resource_rate_list[-1].resource_value_id = 1
    # pbrs.normal_gacha.rare_rate_list[-1].resource_rate_list[-1].amount = 1
    # pbrs.normal_gacha.rare_rate_list[-1].resource_rate_list[-1].rate = "1"
    return raw(pbrs.SerializeToString())

@gacha.post("/gacha/<path:path>")
async def gacha_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "list"): return gacha_list(request, pb.RequestList(), pb.ResponseList())
    if (path == "rate_list"): return gacha_rate_list(request, pb.RequestRateList(), pb.ResponseRateList())
    if (path == "draw"): return gacha_draw(request, pb.RequestDraw(), pb.ResponseDraw())
    else: raise exceptions.NotFound()
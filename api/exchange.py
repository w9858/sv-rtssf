from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import exchange_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64, random

adv_chara = [311001001, 311001002, 311001003, 311001004, 311001005, 311001006, 311001007, 311001008, 311001009, 311001010,\
             311001011, 311001012, 311001013, 311001014, 311001015, 311001016, 311001019, 311001020, 311001022, 311002001,\
             311002002, 311002003, 311002004, 311002005, 311002006, 311002007, 311002008, 311002009, 311002010, 311002011,\
             311002012, 311002013, 311002014, 311002015, 311002016, 311002017, 311002018, 311002021, 311003001, 311003002,\
             311003003, 311003004, 311003005, 311003006, 311003007, 311003008, 311003009, 311003010, 311003011, 311003012,\
             311003013, 311003014, 311003015, 311003017, 311003018, 311004001, 311004002, 311004003, 311004004, 311004005,\
             311004006, 311004007, 311004008, 311004009, 311004010, 311004011, 311004012, 311004013, 311004014, 311004015,\
             311004016, 311004018, 311004019, 311004021, 311004022, 311005001, 311005002, 311005003, 311005004, 311005005,\
             311005006, 311005007, 311005008, 311005009, 311005010, 311005011, 311005012, 311005013, 311005015, 311005018,\
             311006001, 311006002, 311006003, 311006004, 311006005, 311006006, 311006007, 311006008, 311006009, 311006010,\
             311006011, 311006012, 311006013, 311006014, 311006015, 311006016, 311006018, 311006019, 311006021, 311007001,\
             311007002, 311007003, 311007005, 311007008, 311007009, 311008001, 311008002, 311008003, 311008004, 311008005,\
             311008006, 311008007, 311008009, 311008010, 311009001, 311009002, 311009003, 311009004, 311009005, 311009006,\
             311009009, 311009010, 311009011, 311009013, 311010001, 311010002, 311010003, 311010004, 311010005, 311010006,\
             311010007, 311010008, 311010009, 311010011, 311010012, 311010013, 311010014, 311010015, 311011001, 311011002,\
             311012001, 311013001, 311014001, 312001001, 312001002, 312001003, 312001004, 312001005, 312001006, 312001007,\
             312001008, 312001009, 312002001, 312002002, 312002003, 312002004, 312002005, 312002006, 312002007, 312002008,\
             312002009, 312003001, 312003002, 312003003, 312003004, 312003005, 312003006, 312003007, 312003008, 312004001,\
             312004002, 312004003, 312004004, 312004005, 312004006, 312004007, 312004008, 312004011, 312005001, 312005002,\
             313001001, 313001002, 313001004, 313001006, 313002001, 313002003, 313002005, 313002008, 313003002, 313003003,\
             314001001, 314001002, 314002001, 314004001, 314005001, 314006001, 314008001, 314009001, 314011001, 315001001,\
             315002001, 315003001, 315004001, 316001001, 316002001, 316002002, 316002003, 316004001, 316005001, 317001001,\
             394001001, 394001002, 394002001, 394002002, 394003001, 394003002, 394004001, 394004002, 396001001, 396001002,\
             396001003, 396002001, 396002002, 396002003, 396003001, 396003002, 396003003, 396004001, 396004002, 396004003,\
             396005001, 396005002, 396005003, 396006001, 396006002, 396006003, 398001001, 398002001, 398003001, 398004001,\
             398005001, 398005002, 398006001, 398007001, 398010001, 399001001, 399001002, 399001003, 399002001, 399002002,\
             399002003, 399003001, 399003301, 399004001, 399005001]

exchange = Blueprint("api-exchange")

def m_exchange_list(request,pbrq,pbrs):
    pbrs.m_exchange_list.add()
    pbrs.m_exchange_list[-1].exchange_id = random.choice(adv_chara)
    pbrs.m_exchange_list[-1].name = "Mainexchange"
    pbrs.m_exchange_list[-1].balloon_msg = str(pbrs.m_exchange_list[-1].exchange_id)
    pbrs.m_exchange_list[-1].button_type = 0
    pbrs.m_exchange_list.add()
    pbrs.m_exchange_list[-1].exchange_id = random.choice(adv_chara)
    pbrs.m_exchange_list[-1].name = "TESTexchange2"
    pbrs.m_exchange_list[-1].balloon_msg = str(pbrs.m_exchange_list[-1].exchange_id)
    pbrs.m_exchange_list[-1].button_type = 1
    pbrs.m_exchange_list.add()
    pbrs.m_exchange_list[-1].exchange_id = random.choice(adv_chara)
    pbrs.m_exchange_list[-1].name = "TESTexchange3"
    pbrs.m_exchange_list[-1].balloon_msg = str(pbrs.m_exchange_list[-1].exchange_id)
    pbrs.m_exchange_list[-1].button_type = 2
    pbrs.m_exchange_list.add()
    pbrs.m_exchange_list[-1].exchange_id = random.choice(adv_chara)
    pbrs.m_exchange_list[-1].name = "TESTexchange4"
    pbrs.m_exchange_list[-1].balloon_msg = str(pbrs.m_exchange_list[-1].exchange_id)
    pbrs.m_exchange_list[-1].button_type = 3
    
    return raw(pbrs.SerializeToString())

def exchange_item_list(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    pbrs.point = 0
    pbrs.exchange_unit_id = pbrq.exchange_id
    return raw(pbrs.SerializeToString())

@exchange.post("/exchange/<path:path>")
async def exchange_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "list"): return m_exchange_list(request, pb.RequestList(), pb.ResponseList())
    if (path == "item_list"): return exchange_item_list(request, pb.RequestItemList(), pb.ResponseItemList())
    #if (any): request.ctx.errorcode = 201; return empty() # empty maintain return
    else: raise exceptions.NotFound()
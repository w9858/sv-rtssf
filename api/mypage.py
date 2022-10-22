from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from sanic.log import logger
from proto import mypage_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

mypage = Blueprint("api-mypage")
headerlist=[]

def mypage_index(request, pbrq, pbrs):
    #request.ctx.errorcode = 201 #에러코드 일부러 발생
    global headerlist
    pbrq.ParseFromString(request.body)

    jf.Parse(cm.read("t_user"), pbrs)
    jf.Parse(cm.read("t_user_tips_list"), pbrs)
    jf.Parse(cm.read("t_user_crystal"), pbrs)
    jf.Parse(cm.read("t_user_count_list"), pbrs)
    

    #pbrs.m_app_banner_list.add()
    #pbrs.m_app_banner_list[0].banner_img = "Banner/1.png"
    #pbrs.m_app_banner_list[0].order = 0
    #pbrs.m_app_banner_list[0].start_at = "2019-01-03 20:02:44"
    #pbrs.m_app_banner_list[0].end_at = "2027-05-03 20:02:44"
    #pbrs.m_app_banner_list.add()
    #pbrs.m_app_banner_list[1].banner_img = "Banner/2.png"
    #pbrs.m_app_banner_list[1].order = 0
    #pbrs.m_app_banner_list[1].start_at = "2019-01-03 20:02:44"
    #pbrs.m_app_banner_list[1].end_at = "2027-05-03 20:02:44"
    #pbrs.m_app_banner_list.add()
    #pbrs.m_app_banner_list[2].banner_img = "Banner/3.png"
    #pbrs.m_app_banner_list[2].order = 0
    #pbrs.m_app_banner_list[2].start_at = "2019-01-03 20:02:44"
    #pbrs.m_app_banner_list[2].end_at = "2027-05-03 20:02:44"
    #pbrs.m_app_banner_list[2].transition_id = 13
    #pbrs.m_app_banner_list[2].transition_value = 2

    #global headerlist
    #if(request.headers['x_app_huid'] not in headerlist): 
    #    headerlist.append(request.headers['x_app_huid']) 
    #    pbrs.t_user_login_bonus_list.add() 
    #    pbrs.t_user_login_bonus_list[-1].login_bonus_id = 41200201
    #    pbrs.t_user_login_bonus_list[-1].day = 0
    #    pbrs.t_user_login_bonus_list.add()
    #    pbrs.t_user_login_bonus_list[-1].login_bonus_id = 41100801
    #    pbrs.t_user_login_bonus_list[-1].day = 0

    ## daily login bonus  10000001
    ## comeback bonus  50000001
    ## shin sama 4[11010]01

    # pbrs.m_ad_list.add()
    # pbrs.m_ad_list[0].ad_type = 1
    # pbrs.m_ad_list[0].target_id = 3010001
    # pbrs.m_ad_list[0].fade_pattern = 1
    # pbrs.m_ad_list[0].particle_pattern = 2

    pbrs.exists_new_clear_achievement = 0
    pbrs.shop_new_item_flag = 0
    pbrs.exists_friend_invited = 0
    pbrs.no_read_information_count = 0
    pbrs.present_count = 0

    return raw(pbrs.SerializeToString())

#loginbonus
@mypage.post("/mypage/<path:path>")
async def mypage_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "index"): return mypage_index(request, pb.RequestIndex(), pb.ResponseIndex())
    else: raise exceptions.NotFound()

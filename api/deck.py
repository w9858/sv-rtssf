from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import deck_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

deck = Blueprint("api-deck")

def deck_save(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    cm.deck_save(pbrq.t_user_deck)
    jf.Parse(cm.deck_load_one(pbrq.t_user_deck.deck_no),pbrs.t_user_deck)
    return raw(pbrs.SerializeToString())

def deck_change_name(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    cm.deck_change_name(pbrq.name, pbrq.deck_no)
    jf.Parse(cm.deck_load_one(pbrq.deck_no),pbrs.t_user_deck)
    return raw(pbrs.SerializeToString())

@deck.post("/deck/<path:path>")
async def deck_handler(request, path):
    if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "save"): return deck_save(request, pb.RequestSave(), pb.ResponseSave())
    if (path == "change_name"): return deck_change_name(request, pb.RequestChangeName(), pb.ResponseChangeName())
    else: raise exceptions.NotFound()
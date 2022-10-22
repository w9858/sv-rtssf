from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import archive_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

archive = Blueprint("api-archive")

def archive_read(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    cm.adv_clear(pbrq.quest_id)
    jf.Parse(cm.read("t_user_archive_list"), pbrs)
    return raw(pbrs.SerializeToString())

def archive_release(request,pbrq,pbrs):
    pbrq.ParseFromString(request.body)
    cm.adv_clear(pbrq.quest_id)
    jf.Parse(cm.read("t_user_archive_list"), pbrs)
    pbrs.update_resource_result.MergeFrom(cm.update_resource_result())
    return raw(pbrs.SerializeToString())

@archive.post("/archive/<path:path>")
async def archive_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "read"): return archive_read(request, pb.RequestRead(), pb.ResponseRead())
    if (path == "release"): return archive_read(request, pb.RequestRelease(), pb.ResponseRelease())
    else: raise exceptions.NotFound()
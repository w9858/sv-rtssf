from sanic import Blueprint, exceptions
from sanic.response import raw, empty
from proto import help_pb2 as pb
from google.protobuf import json_format as jf
from api import common as cm
import base64

help = Blueprint("api-help")

def help_list(request,pbrq,pbrs):
    pbrs.m_help_list.add()
    pbrs.m_help_list[0].id = 1
    pbrs.m_help_list[0].category = 1
    pbrs.m_help_list[0].order = 1
    pbrs.m_help_list[0].title = "Style Infomation"
    pbrs.m_help_list[0].contents = "<img>1</img>\n   <color=#d6083b>紅蓮</color>, <color=#005198>靑藍</color>, <color=#191c1f>黑鉄</color>, "+\
    "<color=#b83d96>紫電</color>, <color=#5cc151>翡翠</color>, <color=#ffcc00>琥珀</color>"

    pbrs.m_help_list.add()
    pbrs.m_help_list[1].id = 2
    pbrs.m_help_list[1].category = 1
    pbrs.m_help_list[1].order = 2
    pbrs.m_help_list[1].title = "Contact"
    pbrs.m_help_list[1].contents = "\n\
    <color=#00acee>Twitter</color> : @w9858__  (two underbar)\n\n\
    <color=#ea4335>Email</color> : w9858@protonmail.com\n\n\
    <color=#5865f2>Discord</color> : jhoon6#9050\n\n\
    <color=#6e5494>GitHub</color> : https://github.com/w9858"

    pbrs.m_help_list.add()
    pbrs.m_help_list[2].id = 3
    pbrs.m_help_list[2].category = 1
    pbrs.m_help_list[2].order = 3
    pbrs.m_help_list[2].title = "Website Backups"
    pbrs.m_help_list[2].contents = "\n\
    https://w9858.pages.dev/ - Game site\n\n\
    https://w9858.pages.dev/220206/ - Anime site\n\n\
    https://w9858.pages.dev/180129/ - Anime site - old one\n\n\
    https://w9858.pages.dev/180325/ - Anime site - old one"

    pbrs.m_help_list.add()
    pbrs.m_help_list[3].id = 4
    pbrs.m_help_list[3].category = 1
    pbrs.m_help_list[3].order = 4
    pbrs.m_help_list[3].title = "License"
    pbrs.m_help_list[3].contents = 'sv-rtssf made with sanic, awesome python web server/framework.\n\n\
sanic-org/sanic is licensed under the MIT License\n\nMIT License\n\
\n\
Copyright (c) 2016-present Sanic Community\n\
\n\
Permission is hereby granted, free of charge, to any person obtaining a copy\
of this software and associated documentation files (the "Software"), to deal\
in the Software without restriction, including without limitation the rights\
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\
copies of the Software, and to permit persons to whom the Software is\
furnished to do so, subject to the following conditions:\n\
\n\
The above copyright notice and this permission notice shall be included in all\
copies or substantial portions of the Software.\n\
\n\
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR \
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\
SOFTWARE.'

    pbrs.m_help_category_list.add()
    pbrs.m_help_category_list[0].category = 1
    pbrs.m_help_category_list[0].order = 1
    pbrs.m_help_category_list[0].name = "Helpful Informations"

    return raw(pbrs.SerializeToString())

@help.post("/help/<path:path>")
async def help_handler(request, path):
    # if (request.host != "api.relefra.jp"): raise exceptions.Forbidden()
    if (path == "list"): return help_list(request, pb.RequestList(), pb.ResponseList())
    else: raise exceptions.NotFound()

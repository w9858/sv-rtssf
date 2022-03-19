from sanic import Blueprint, exceptions

from .achievement import achievement
from .archive import archive
from .billing import billing
from .board import board
from .deck import deck
from .eventmap import eventmap
from .exchange import exchange
from .friend import friend
from .gacha import gacha
from .gamecenter import gamecenter
from .help import help
from .information import information
from .item import item
from .load import load
from .mypage import mypage
from .present import present
from .quest import quest
from .recipe import recipe
from .regist import regist
from .shop import shop
from .spy import spy
from .tips import tips
from .tutorial import tutorial
from .tutorialhowtoplay import tutorialhowtoplay
from .unit import unit
from .user import user
from .weapon import weapon

api = Blueprint.group(achievement, archive, billing, board, deck, eventmap, exchange, \
                      friend, gacha, gamecenter, help, information, item, load, mypage, \
                      present, quest, recipe, regist, shop, spy, tips, tutorial, tutorialhowtoplay, \
                      unit, user, weapon)

# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gacha.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0bgacha.proto\x12\tSpy.Gacha\x1a\x0c\x63ommon.proto\"]\n\x0bRequestDraw\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x11\n\tdetail_id\x18\x02 \x01(\x05\x12\x0c\n\x04step\x18\x03 \x01(\x05\x12\x1b\n\x13is_exchange_crystal\x18\x04 \x01(\x08\"\r\n\x0bRequestList\"#\n\x0fRequestRateList\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\"\xa3\x03\n\x0cResponseDraw\x12.\n\x10\x64raw_result_list\x18\x01 \x03(\x0b\x32\x14.Spy.Common.Resource\x12(\n\nomake_list\x18\x02 \x03(\x0b\x32\x14.Spy.Common.Resource\x12\x39\n\x13t_user_gacha_stepup\x18\x03 \x01(\x0b\x32\x1c.Spy.Common.TUserGachaStepup\x12\x39\n\x13t_user_gacha_normal\x18\x04 \x01(\x0b\x32\x1c.Spy.Common.TUserGachaNormal\x12\x46\n\x1at_user_gacha_normal_detail\x18\x05 \x01(\x0b\x32\".Spy.Common.TUserGachaNormalDetail\x12@\n\x16update_resource_result\x18\x06 \x01(\x0b\x32 .Spy.Common.UpdateResourceResult\x12\x10\n\x08\x65\x66\x66\x65\x63t_1\x18\x07 \x01(\x05\x12\x10\n\x08\x65\x66\x66\x65\x63t_2\x18\x08 \x01(\x05\x12\x15\n\reffect_3_list\x18\t \x03(\x05\"\xde\r\n\x0cResponseList\x12\x34\n\x0cm_gacha_list\x18\x01 \x03(\x0b\x32\x1e.Spy.Gacha.ResponseList.MGacha\x12N\n\x1am_gacha_normal_detail_list\x18\x03 \x03(\x0b\x32*.Spy.Gacha.ResponseList.MGachaNormalDetail\x12L\n\x19m_gacha_normal_omake_list\x18\x04 \x03(\x0b\x32).Spy.Gacha.ResponseList.MGachaNormalOmake\x12\x41\n\x13m_gacha_stepup_list\x18\x05 \x03(\x0b\x32$.Spy.Gacha.ResponseList.MGachaStepup\x12N\n\x1am_gacha_stepup_detail_list\x18\x06 \x03(\x0b\x32*.Spy.Gacha.ResponseList.MGachaStepupDetail\x12L\n\x19m_gacha_stepup_omake_list\x18\x07 \x03(\x0b\x32).Spy.Gacha.ResponseList.MGachaStepupOmake\x12>\n\x18t_user_gacha_normal_list\x18\x08 \x03(\x0b\x32\x1c.Spy.Common.TUserGachaNormal\x12>\n\x18t_user_gacha_stepup_list\x18\t \x03(\x0b\x32\x1c.Spy.Common.TUserGachaStepup\x12\x43\n\x14m_gacha_feature_list\x18\n \x03(\x0b\x32%.Spy.Gacha.ResponseList.MGachaFeature\x12K\n\x1ft_user_gacha_normal_detail_list\x18\x0b \x03(\x0b\x32\".Spy.Common.TUserGachaNormalDetail\x1a\xdf\x01\n\x06MGacha\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x12\n\ngacha_type\x18\x02 \x01(\x05\x12\r\n\x05order\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x0e\n\x06header\x18\x07 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x08 \x01(\t\x12\x15\n\rbackground_id\x18\t \x01(\x05\x12\x1c\n\x14\x65nd_of_tutorial_from\x18\n \x01(\x05\x12\x16\n\x0e\x64isp_term_flag\x18\x0b \x01(\x05\x12\x10\n\x08start_at\x18\x0c \x01(\t\x12\x0e\n\x06\x65nd_at\x18\r \x01(\t\x1a\x41\n\rMGachaFeature\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x0f\n\x07unit_id\x18\x02 \x01(\x05\x12\r\n\x05order\x18\x03 \x01(\x05\x1a\xd3\x01\n\x12MGachaNormalDetail\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x11\n\tdetail_id\x18\x02 \x01(\x05\x12\x14\n\x0cone_day_flag\x18\x03 \x01(\x05\x12\x12\n\ndraw_count\x18\x04 \x01(\x05\x12\x15\n\rresource_type\x18\x05 \x01(\x05\x12\x13\n\x0bresource_id\x18\x06 \x01(\x05\x12\x19\n\x11resource_value_id\x18\x07 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x08 \x01(\x05\x12\x17\n\x0f\x65xecution_limit\x18\t \x01(\x05\x1a\x8f\x01\n\x11MGachaNormalOmake\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x15\n\rresource_type\x18\x02 \x01(\x05\x12\x13\n\x0bresource_id\x18\x03 \x01(\x05\x12\x19\n\x11resource_value_id\x18\x04 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x05\x12\x11\n\tdetail_id\x18\x06 \x01(\x05\x1a\x32\n\x0cMGachaStepup\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x10\n\x08max_loop\x18\x02 \x01(\x05\x1a\xb8\x01\n\x12MGachaStepupDetail\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x0c\n\x04step\x18\x02 \x01(\x05\x12\x12\n\ndraw_count\x18\x05 \x01(\x05\x12\x15\n\rresource_type\x18\x06 \x01(\x05\x12\x13\n\x0bresource_id\x18\x07 \x01(\x05\x12\x19\n\x11resource_value_id\x18\x08 \x01(\x05\x12\x0e\n\x06\x61mount\x18\t \x01(\x05\x12\x17\n\x0fnext_step_count\x18\n \x01(\x05\x1a\x8a\x01\n\x11MGachaStepupOmake\x12\x10\n\x08gacha_id\x18\x01 \x01(\x05\x12\x0c\n\x04step\x18\x02 \x01(\x05\x12\x15\n\rresource_type\x18\x03 \x01(\x05\x12\x13\n\x0bresource_id\x18\x04 \x01(\x05\x12\x19\n\x11resource_value_id\x18\x05 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x06 \x01(\x05\"\x9a\x06\n\x10ResponseRateList\x12=\n\x0cnormal_gacha\x18\x01 \x01(\x0b\x32\'.Spy.Gacha.ResponseRateList.NormalGacha\x12\x42\n\x11stepup_gacha_list\x18\x02 \x03(\x0b\x32\'.Spy.Gacha.ResponseRateList.StepupGacha\x1av\n\tFixedDraw\x12\x11\n\tdetail_id\x18\x01 \x01(\x05\x12\x18\n\x10\x66ixed_draw_count\x18\x02 \x01(\x05\x12<\n\x0erare_rate_list\x18\x03 \x03(\x0b\x32$.Spy.Gacha.ResponseRateList.RareRate\x1a\x8b\x01\n\x0bNormalGacha\x12<\n\x0erare_rate_list\x18\x01 \x03(\x0b\x32$.Spy.Gacha.ResponseRateList.RareRate\x12>\n\x0f\x66ixed_draw_list\x18\x02 \x03(\x0b\x32%.Spy.Gacha.ResponseRateList.FixedDraw\x1al\n\x08RareRate\x12\x0c\n\x04rare\x18\x01 \x01(\x05\x12\x0c\n\x04rate\x18\x02 \x01(\t\x12\x44\n\x12resource_rate_list\x18\x03 \x03(\x0b\x32(.Spy.Gacha.ResponseRateList.ResourceRate\x1as\n\x0cResourceRate\x12\x15\n\rresource_type\x18\x01 \x01(\x05\x12\x13\n\x0bresource_id\x18\x02 \x01(\x05\x12\x19\n\x11resource_value_id\x18\x03 \x01(\x05\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x05\x12\x0c\n\x04rate\x18\x05 \x01(\t\x1a\x99\x01\n\x0bStepupGacha\x12\x0c\n\x04step\x18\x01 \x01(\x05\x12<\n\x0erare_rate_list\x18\x02 \x03(\x0b\x32$.Spy.Gacha.ResponseRateList.RareRate\x12>\n\x0f\x66ixed_draw_list\x18\x03 \x03(\x0b\x32%.Spy.Gacha.ResponseRateList.FixedDrawb\x06proto3')



_REQUESTDRAW = DESCRIPTOR.message_types_by_name['RequestDraw']
_REQUESTLIST = DESCRIPTOR.message_types_by_name['RequestList']
_REQUESTRATELIST = DESCRIPTOR.message_types_by_name['RequestRateList']
_RESPONSEDRAW = DESCRIPTOR.message_types_by_name['ResponseDraw']
_RESPONSELIST = DESCRIPTOR.message_types_by_name['ResponseList']
_RESPONSELIST_MGACHA = _RESPONSELIST.nested_types_by_name['MGacha']
_RESPONSELIST_MGACHAFEATURE = _RESPONSELIST.nested_types_by_name['MGachaFeature']
_RESPONSELIST_MGACHANORMALDETAIL = _RESPONSELIST.nested_types_by_name['MGachaNormalDetail']
_RESPONSELIST_MGACHANORMALOMAKE = _RESPONSELIST.nested_types_by_name['MGachaNormalOmake']
_RESPONSELIST_MGACHASTEPUP = _RESPONSELIST.nested_types_by_name['MGachaStepup']
_RESPONSELIST_MGACHASTEPUPDETAIL = _RESPONSELIST.nested_types_by_name['MGachaStepupDetail']
_RESPONSELIST_MGACHASTEPUPOMAKE = _RESPONSELIST.nested_types_by_name['MGachaStepupOmake']
_RESPONSERATELIST = DESCRIPTOR.message_types_by_name['ResponseRateList']
_RESPONSERATELIST_FIXEDDRAW = _RESPONSERATELIST.nested_types_by_name['FixedDraw']
_RESPONSERATELIST_NORMALGACHA = _RESPONSERATELIST.nested_types_by_name['NormalGacha']
_RESPONSERATELIST_RARERATE = _RESPONSERATELIST.nested_types_by_name['RareRate']
_RESPONSERATELIST_RESOURCERATE = _RESPONSERATELIST.nested_types_by_name['ResourceRate']
_RESPONSERATELIST_STEPUPGACHA = _RESPONSERATELIST.nested_types_by_name['StepupGacha']
RequestDraw = _reflection.GeneratedProtocolMessageType('RequestDraw', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTDRAW,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Gacha.RequestDraw)
  })
_sym_db.RegisterMessage(RequestDraw)

RequestList = _reflection.GeneratedProtocolMessageType('RequestList', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTLIST,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Gacha.RequestList)
  })
_sym_db.RegisterMessage(RequestList)

RequestRateList = _reflection.GeneratedProtocolMessageType('RequestRateList', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRATELIST,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Gacha.RequestRateList)
  })
_sym_db.RegisterMessage(RequestRateList)

ResponseDraw = _reflection.GeneratedProtocolMessageType('ResponseDraw', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEDRAW,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseDraw)
  })
_sym_db.RegisterMessage(ResponseDraw)

ResponseList = _reflection.GeneratedProtocolMessageType('ResponseList', (_message.Message,), {

  'MGacha' : _reflection.GeneratedProtocolMessageType('MGacha', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHA,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGacha)
    })
  ,

  'MGachaFeature' : _reflection.GeneratedProtocolMessageType('MGachaFeature', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHAFEATURE,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGachaFeature)
    })
  ,

  'MGachaNormalDetail' : _reflection.GeneratedProtocolMessageType('MGachaNormalDetail', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHANORMALDETAIL,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGachaNormalDetail)
    })
  ,

  'MGachaNormalOmake' : _reflection.GeneratedProtocolMessageType('MGachaNormalOmake', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHANORMALOMAKE,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGachaNormalOmake)
    })
  ,

  'MGachaStepup' : _reflection.GeneratedProtocolMessageType('MGachaStepup', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHASTEPUP,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGachaStepup)
    })
  ,

  'MGachaStepupDetail' : _reflection.GeneratedProtocolMessageType('MGachaStepupDetail', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHASTEPUPDETAIL,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGachaStepupDetail)
    })
  ,

  'MGachaStepupOmake' : _reflection.GeneratedProtocolMessageType('MGachaStepupOmake', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSELIST_MGACHASTEPUPOMAKE,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList.MGachaStepupOmake)
    })
  ,
  'DESCRIPTOR' : _RESPONSELIST,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseList)
  })
_sym_db.RegisterMessage(ResponseList)
_sym_db.RegisterMessage(ResponseList.MGacha)
_sym_db.RegisterMessage(ResponseList.MGachaFeature)
_sym_db.RegisterMessage(ResponseList.MGachaNormalDetail)
_sym_db.RegisterMessage(ResponseList.MGachaNormalOmake)
_sym_db.RegisterMessage(ResponseList.MGachaStepup)
_sym_db.RegisterMessage(ResponseList.MGachaStepupDetail)
_sym_db.RegisterMessage(ResponseList.MGachaStepupOmake)

ResponseRateList = _reflection.GeneratedProtocolMessageType('ResponseRateList', (_message.Message,), {

  'FixedDraw' : _reflection.GeneratedProtocolMessageType('FixedDraw', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSERATELIST_FIXEDDRAW,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseRateList.FixedDraw)
    })
  ,

  'NormalGacha' : _reflection.GeneratedProtocolMessageType('NormalGacha', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSERATELIST_NORMALGACHA,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseRateList.NormalGacha)
    })
  ,

  'RareRate' : _reflection.GeneratedProtocolMessageType('RareRate', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSERATELIST_RARERATE,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseRateList.RareRate)
    })
  ,

  'ResourceRate' : _reflection.GeneratedProtocolMessageType('ResourceRate', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSERATELIST_RESOURCERATE,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseRateList.ResourceRate)
    })
  ,

  'StepupGacha' : _reflection.GeneratedProtocolMessageType('StepupGacha', (_message.Message,), {
    'DESCRIPTOR' : _RESPONSERATELIST_STEPUPGACHA,
    '__module__' : 'gacha_pb2'
    # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseRateList.StepupGacha)
    })
  ,
  'DESCRIPTOR' : _RESPONSERATELIST,
  '__module__' : 'gacha_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Gacha.ResponseRateList)
  })
_sym_db.RegisterMessage(ResponseRateList)
_sym_db.RegisterMessage(ResponseRateList.FixedDraw)
_sym_db.RegisterMessage(ResponseRateList.NormalGacha)
_sym_db.RegisterMessage(ResponseRateList.RareRate)
_sym_db.RegisterMessage(ResponseRateList.ResourceRate)
_sym_db.RegisterMessage(ResponseRateList.StepupGacha)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTDRAW._serialized_start=40
  _REQUESTDRAW._serialized_end=133
  _REQUESTLIST._serialized_start=135
  _REQUESTLIST._serialized_end=148
  _REQUESTRATELIST._serialized_start=150
  _REQUESTRATELIST._serialized_end=185
  _RESPONSEDRAW._serialized_start=188
  _RESPONSEDRAW._serialized_end=607
  _RESPONSELIST._serialized_start=610
  _RESPONSELIST._serialized_end=2368
  _RESPONSELIST_MGACHA._serialized_start=1338
  _RESPONSELIST_MGACHA._serialized_end=1561
  _RESPONSELIST_MGACHAFEATURE._serialized_start=1563
  _RESPONSELIST_MGACHAFEATURE._serialized_end=1628
  _RESPONSELIST_MGACHANORMALDETAIL._serialized_start=1631
  _RESPONSELIST_MGACHANORMALDETAIL._serialized_end=1842
  _RESPONSELIST_MGACHANORMALOMAKE._serialized_start=1845
  _RESPONSELIST_MGACHANORMALOMAKE._serialized_end=1988
  _RESPONSELIST_MGACHASTEPUP._serialized_start=1990
  _RESPONSELIST_MGACHASTEPUP._serialized_end=2040
  _RESPONSELIST_MGACHASTEPUPDETAIL._serialized_start=2043
  _RESPONSELIST_MGACHASTEPUPDETAIL._serialized_end=2227
  _RESPONSELIST_MGACHASTEPUPOMAKE._serialized_start=2230
  _RESPONSELIST_MGACHASTEPUPOMAKE._serialized_end=2368
  _RESPONSERATELIST._serialized_start=2371
  _RESPONSERATELIST._serialized_end=3165
  _RESPONSERATELIST_FIXEDDRAW._serialized_start=2522
  _RESPONSERATELIST_FIXEDDRAW._serialized_end=2640
  _RESPONSERATELIST_NORMALGACHA._serialized_start=2643
  _RESPONSERATELIST_NORMALGACHA._serialized_end=2782
  _RESPONSERATELIST_RARERATE._serialized_start=2784
  _RESPONSERATELIST_RARERATE._serialized_end=2892
  _RESPONSERATELIST_RESOURCERATE._serialized_start=2894
  _RESPONSERATELIST_RESOURCERATE._serialized_end=3009
  _RESPONSERATELIST_STEPUPGACHA._serialized_start=3012
  _RESPONSERATELIST_STEPUPGACHA._serialized_end=3165
# @@protoc_insertion_point(module_scope)

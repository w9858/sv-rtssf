# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recipe.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0crecipe.proto\x12\nSpy.Recipe\x1a\x0c\x63ommon.proto\"V\n\rRequestCreate\x12\x11\n\trecipe_id\x18\x01 \x01(\x05\x12\x15\n\rboost_item_id\x18\x02 \x01(\x05\x12\x1b\n\x13is_exchange_crystal\x18\x03 \x01(\x08\"R\n\x0eResponseCreate\x12@\n\x16update_resource_result\x18\x01 \x01(\x0b\x32 .Spy.Common.UpdateResourceResultb\x06proto3')



_REQUESTCREATE = DESCRIPTOR.message_types_by_name['RequestCreate']
_RESPONSECREATE = DESCRIPTOR.message_types_by_name['ResponseCreate']
RequestCreate = _reflection.GeneratedProtocolMessageType('RequestCreate', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCREATE,
  '__module__' : 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Recipe.RequestCreate)
  })
_sym_db.RegisterMessage(RequestCreate)

ResponseCreate = _reflection.GeneratedProtocolMessageType('ResponseCreate', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECREATE,
  '__module__' : 'recipe_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Recipe.ResponseCreate)
  })
_sym_db.RegisterMessage(ResponseCreate)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTCREATE._serialized_start=42
  _REQUESTCREATE._serialized_end=128
  _RESPONSECREATE._serialized_start=130
  _RESPONSECREATE._serialized_end=212
# @@protoc_insertion_point(module_scope)

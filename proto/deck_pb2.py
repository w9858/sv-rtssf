# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: deck.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ndeck.proto\x12\x08Spy.Deck\x1a\x0c\x63ommon.proto\"2\n\x11RequestChangeName\x12\x0f\n\x07\x64\x65\x63k_no\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\"9\n\x0bRequestSave\x12*\n\x0bt_user_deck\x18\x01 \x01(\x0b\x32\x15.Spy.Common.TUserDeck\"@\n\x12ResponseChangeName\x12*\n\x0bt_user_deck\x18\x01 \x01(\x0b\x32\x15.Spy.Common.TUserDeck\":\n\x0cResponseSave\x12*\n\x0bt_user_deck\x18\x01 \x01(\x0b\x32\x15.Spy.Common.TUserDeckb\x06proto3')



_REQUESTCHANGENAME = DESCRIPTOR.message_types_by_name['RequestChangeName']
_REQUESTSAVE = DESCRIPTOR.message_types_by_name['RequestSave']
_RESPONSECHANGENAME = DESCRIPTOR.message_types_by_name['ResponseChangeName']
_RESPONSESAVE = DESCRIPTOR.message_types_by_name['ResponseSave']
RequestChangeName = _reflection.GeneratedProtocolMessageType('RequestChangeName', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTCHANGENAME,
  '__module__' : 'deck_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Deck.RequestChangeName)
  })
_sym_db.RegisterMessage(RequestChangeName)

RequestSave = _reflection.GeneratedProtocolMessageType('RequestSave', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTSAVE,
  '__module__' : 'deck_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Deck.RequestSave)
  })
_sym_db.RegisterMessage(RequestSave)

ResponseChangeName = _reflection.GeneratedProtocolMessageType('ResponseChangeName', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSECHANGENAME,
  '__module__' : 'deck_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Deck.ResponseChangeName)
  })
_sym_db.RegisterMessage(ResponseChangeName)

ResponseSave = _reflection.GeneratedProtocolMessageType('ResponseSave', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSESAVE,
  '__module__' : 'deck_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Deck.ResponseSave)
  })
_sym_db.RegisterMessage(ResponseSave)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTCHANGENAME._serialized_start=38
  _REQUESTCHANGENAME._serialized_end=88
  _REQUESTSAVE._serialized_start=90
  _REQUESTSAVE._serialized_end=147
  _RESPONSECHANGENAME._serialized_start=149
  _RESPONSECHANGENAME._serialized_end=213
  _RESPONSESAVE._serialized_start=215
  _RESPONSESAVE._serialized_end=273
# @@protoc_insertion_point(module_scope)

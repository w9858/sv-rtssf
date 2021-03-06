# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: archive.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from proto import common_pb2 as common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rarchive.proto\x12\x0bSpy.Archive\x1a\x0c\x63ommon.proto\"\x1f\n\x0bRequestRead\x12\x10\n\x08quest_id\x18\x01 \x01(\x05\"\"\n\x0eRequestRelease\x12\x10\n\x08quest_id\x18\x01 \x01(\x05\"E\n\x0cResponseRead\x12\x35\n\x13t_user_archive_list\x18\x01 \x03(\x0b\x32\x18.Spy.Common.TUserArchive\"\x8a\x01\n\x0fResponseRelease\x12\x35\n\x13t_user_archive_list\x18\x01 \x03(\x0b\x32\x18.Spy.Common.TUserArchive\x12@\n\x16update_resource_result\x18\x02 \x01(\x0b\x32 .Spy.Common.UpdateResourceResultb\x06proto3')



_REQUESTREAD = DESCRIPTOR.message_types_by_name['RequestRead']
_REQUESTRELEASE = DESCRIPTOR.message_types_by_name['RequestRelease']
_RESPONSEREAD = DESCRIPTOR.message_types_by_name['ResponseRead']
_RESPONSERELEASE = DESCRIPTOR.message_types_by_name['ResponseRelease']
RequestRead = _reflection.GeneratedProtocolMessageType('RequestRead', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTREAD,
  '__module__' : 'archive_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Archive.RequestRead)
  })
_sym_db.RegisterMessage(RequestRead)

RequestRelease = _reflection.GeneratedProtocolMessageType('RequestRelease', (_message.Message,), {
  'DESCRIPTOR' : _REQUESTRELEASE,
  '__module__' : 'archive_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Archive.RequestRelease)
  })
_sym_db.RegisterMessage(RequestRelease)

ResponseRead = _reflection.GeneratedProtocolMessageType('ResponseRead', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEREAD,
  '__module__' : 'archive_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Archive.ResponseRead)
  })
_sym_db.RegisterMessage(ResponseRead)

ResponseRelease = _reflection.GeneratedProtocolMessageType('ResponseRelease', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSERELEASE,
  '__module__' : 'archive_pb2'
  # @@protoc_insertion_point(class_scope:Spy.Archive.ResponseRelease)
  })
_sym_db.RegisterMessage(ResponseRelease)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUESTREAD._serialized_start=44
  _REQUESTREAD._serialized_end=75
  _REQUESTRELEASE._serialized_start=77
  _REQUESTRELEASE._serialized_end=111
  _RESPONSEREAD._serialized_start=113
  _RESPONSEREAD._serialized_end=182
  _RESPONSERELEASE._serialized_start=185
  _RESPONSERELEASE._serialized_end=323
# @@protoc_insertion_point(module_scope)

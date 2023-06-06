# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: predict.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import eas_prediction.tf_request_pb2 as tf__request__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='predict.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\rpredict.proto\x1a\x10tf_request.proto\"/\n\x0f\x43ontextFeatures\x12\x1c\n\x08\x66\x65\x61tures\x18\x01 \x03(\x0b\x32\n.PBFeature\"v\n\tPBFeature\x12\x15\n\x0bint_feature\x18\x01 \x01(\x05H\x00\x12\x16\n\x0clong_feature\x18\x02 \x01(\x03H\x00\x12\x18\n\x0estring_feature\x18\x03 \x01(\tH\x00\x12\x17\n\rfloat_feature\x18\x04 \x01(\x02H\x00\x42\x07\n\x05value\"\xc6\x02\n\tPBRequest\x12\x13\n\x0b\x64\x65\x62ug_level\x18\x01 \x01(\x05\x12\x33\n\ruser_features\x18\x02 \x03(\x0b\x32\x1c.PBRequest.UserFeaturesEntry\x12\x10\n\x08item_ids\x18\x03 \x03(\t\x12\x39\n\x10\x63ontext_features\x18\x04 \x03(\x0b\x32\x1f.PBRequest.ContextFeaturesEntry\x12\x17\n\x0f\x66\x61iss_neigh_num\x18\x05 \x01(\x05\x1a?\n\x11UserFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x19\n\x05value\x18\x02 \x01(\x0b\x32\n.PBFeature:\x02\x38\x01\x1aH\n\x14\x43ontextFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.ContextFeatures:\x02\x38\x01\"\x1d\n\x07Results\x12\x12\n\x06scores\x18\x01 \x03(\x01\x42\x02\x10\x01\"\x88\x06\n\nPBResponse\x12)\n\x07results\x18\x01 \x03(\x0b\x32\x18.PBResponse.ResultsEntry\x12\x34\n\ritem_features\x18\x02 \x03(\x0b\x32\x1d.PBResponse.ItemFeaturesEntry\x12<\n\x11generate_features\x18\x03 \x03(\x0b\x32!.PBResponse.GenerateFeaturesEntry\x12:\n\x10\x63ontext_features\x18\x04 \x03(\x0b\x32 .PBResponse.ContextFeaturesEntry\x12\x11\n\terror_msg\x18\x05 \x01(\t\x12 \n\x0bstatus_code\x18\x06 \x01(\x0e\x32\x0b.StatusCode\x12\x10\n\x08item_ids\x18\x07 \x03(\t\x12\x0f\n\x07outputs\x18\x08 \x03(\t\x12\x32\n\x0craw_features\x18\t \x03(\x0b\x32\x1c.PBResponse.RawFeaturesEntry\x12.\n\ntf_outputs\x18\n \x03(\x0b\x32\x1a.PBResponse.TfOutputsEntry\x1a\x38\n\x0cResultsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x17\n\x05value\x18\x02 \x01(\x0b\x32\x08.Results:\x02\x38\x01\x1a\x33\n\x11ItemFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x37\n\x15GenerateFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1aH\n\x14\x43ontextFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.ContextFeatures:\x02\x38\x01\x1a\x32\n\x10RawFeaturesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a=\n\x0eTfOutputsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x1a\n\x05value\x18\x02 \x01(\x0b\x32\x0b.ArrayProto:\x02\x38\x01*4\n\nStatusCode\x12\x06\n\x02OK\x10\x00\x12\x0f\n\x0bINPUT_EMPTY\x10\x01\x12\r\n\tEXCEPTION\x10\x02\x62\x06proto3')
  ,
  dependencies=[tf__request__pb2.DESCRIPTOR,])

_STATUSCODE = _descriptor.EnumDescriptor(
  name='StatusCode',
  full_name='StatusCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OK', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INPUT_EMPTY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCEPTION', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1343,
  serialized_end=1395,
)
_sym_db.RegisterEnumDescriptor(_STATUSCODE)

StatusCode = enum_type_wrapper.EnumTypeWrapper(_STATUSCODE)
OK = 0
INPUT_EMPTY = 1
EXCEPTION = 2



_CONTEXTFEATURES = _descriptor.Descriptor(
  name='ContextFeatures',
  full_name='ContextFeatures',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='features', full_name='ContextFeatures.features', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=82,
)


_PBFEATURE = _descriptor.Descriptor(
  name='PBFeature',
  full_name='PBFeature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_feature', full_name='PBFeature.int_feature', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='long_feature', full_name='PBFeature.long_feature', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_feature', full_name='PBFeature.string_feature', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_feature', full_name='PBFeature.float_feature', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='value', full_name='PBFeature.value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=84,
  serialized_end=202,
)


_PBREQUEST_USERFEATURESENTRY = _descriptor.Descriptor(
  name='UserFeaturesEntry',
  full_name='PBRequest.UserFeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBRequest.UserFeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBRequest.UserFeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=457,
)

_PBREQUEST_CONTEXTFEATURESENTRY = _descriptor.Descriptor(
  name='ContextFeaturesEntry',
  full_name='PBRequest.ContextFeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBRequest.ContextFeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBRequest.ContextFeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=531,
)

_PBREQUEST = _descriptor.Descriptor(
  name='PBRequest',
  full_name='PBRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='debug_level', full_name='PBRequest.debug_level', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='user_features', full_name='PBRequest.user_features', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='PBRequest.item_ids', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context_features', full_name='PBRequest.context_features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='faiss_neigh_num', full_name='PBRequest.faiss_neigh_num', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PBREQUEST_USERFEATURESENTRY, _PBREQUEST_CONTEXTFEATURESENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=205,
  serialized_end=531,
)


_RESULTS = _descriptor.Descriptor(
  name='Results',
  full_name='Results',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='scores', full_name='Results.scores', index=0,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=533,
  serialized_end=562,
)


_PBRESPONSE_RESULTSENTRY = _descriptor.Descriptor(
  name='ResultsEntry',
  full_name='PBResponse.ResultsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBResponse.ResultsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBResponse.ResultsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=986,
  serialized_end=1042,
)

_PBRESPONSE_ITEMFEATURESENTRY = _descriptor.Descriptor(
  name='ItemFeaturesEntry',
  full_name='PBResponse.ItemFeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBResponse.ItemFeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBResponse.ItemFeaturesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1044,
  serialized_end=1095,
)

_PBRESPONSE_GENERATEFEATURESENTRY = _descriptor.Descriptor(
  name='GenerateFeaturesEntry',
  full_name='PBResponse.GenerateFeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBResponse.GenerateFeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBResponse.GenerateFeaturesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1097,
  serialized_end=1152,
)

_PBRESPONSE_CONTEXTFEATURESENTRY = _descriptor.Descriptor(
  name='ContextFeaturesEntry',
  full_name='PBResponse.ContextFeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBResponse.ContextFeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBResponse.ContextFeaturesEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=459,
  serialized_end=531,
)

_PBRESPONSE_RAWFEATURESENTRY = _descriptor.Descriptor(
  name='RawFeaturesEntry',
  full_name='PBResponse.RawFeaturesEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBResponse.RawFeaturesEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBResponse.RawFeaturesEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1228,
  serialized_end=1278,
)

_PBRESPONSE_TFOUTPUTSENTRY = _descriptor.Descriptor(
  name='TfOutputsEntry',
  full_name='PBResponse.TfOutputsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='PBResponse.TfOutputsEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='PBResponse.TfOutputsEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1280,
  serialized_end=1341,
)

_PBRESPONSE = _descriptor.Descriptor(
  name='PBResponse',
  full_name='PBResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='results', full_name='PBResponse.results', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_features', full_name='PBResponse.item_features', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='generate_features', full_name='PBResponse.generate_features', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='context_features', full_name='PBResponse.context_features', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error_msg', full_name='PBResponse.error_msg', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status_code', full_name='PBResponse.status_code', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='item_ids', full_name='PBResponse.item_ids', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='outputs', full_name='PBResponse.outputs', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='raw_features', full_name='PBResponse.raw_features', index=8,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tf_outputs', full_name='PBResponse.tf_outputs', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PBRESPONSE_RESULTSENTRY, _PBRESPONSE_ITEMFEATURESENTRY, _PBRESPONSE_GENERATEFEATURESENTRY, _PBRESPONSE_CONTEXTFEATURESENTRY, _PBRESPONSE_RAWFEATURESENTRY, _PBRESPONSE_TFOUTPUTSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=565,
  serialized_end=1341,
)

_CONTEXTFEATURES.fields_by_name['features'].message_type = _PBFEATURE
_PBFEATURE.oneofs_by_name['value'].fields.append(
  _PBFEATURE.fields_by_name['int_feature'])
_PBFEATURE.fields_by_name['int_feature'].containing_oneof = _PBFEATURE.oneofs_by_name['value']
_PBFEATURE.oneofs_by_name['value'].fields.append(
  _PBFEATURE.fields_by_name['long_feature'])
_PBFEATURE.fields_by_name['long_feature'].containing_oneof = _PBFEATURE.oneofs_by_name['value']
_PBFEATURE.oneofs_by_name['value'].fields.append(
  _PBFEATURE.fields_by_name['string_feature'])
_PBFEATURE.fields_by_name['string_feature'].containing_oneof = _PBFEATURE.oneofs_by_name['value']
_PBFEATURE.oneofs_by_name['value'].fields.append(
  _PBFEATURE.fields_by_name['float_feature'])
_PBFEATURE.fields_by_name['float_feature'].containing_oneof = _PBFEATURE.oneofs_by_name['value']
_PBREQUEST_USERFEATURESENTRY.fields_by_name['value'].message_type = _PBFEATURE
_PBREQUEST_USERFEATURESENTRY.containing_type = _PBREQUEST
_PBREQUEST_CONTEXTFEATURESENTRY.fields_by_name['value'].message_type = _CONTEXTFEATURES
_PBREQUEST_CONTEXTFEATURESENTRY.containing_type = _PBREQUEST
_PBREQUEST.fields_by_name['user_features'].message_type = _PBREQUEST_USERFEATURESENTRY
_PBREQUEST.fields_by_name['context_features'].message_type = _PBREQUEST_CONTEXTFEATURESENTRY
_PBRESPONSE_RESULTSENTRY.fields_by_name['value'].message_type = _RESULTS
_PBRESPONSE_RESULTSENTRY.containing_type = _PBRESPONSE
_PBRESPONSE_ITEMFEATURESENTRY.containing_type = _PBRESPONSE
_PBRESPONSE_GENERATEFEATURESENTRY.containing_type = _PBRESPONSE
_PBRESPONSE_CONTEXTFEATURESENTRY.fields_by_name['value'].message_type = _CONTEXTFEATURES
_PBRESPONSE_CONTEXTFEATURESENTRY.containing_type = _PBRESPONSE
_PBRESPONSE_RAWFEATURESENTRY.containing_type = _PBRESPONSE
_PBRESPONSE_TFOUTPUTSENTRY.fields_by_name['value'].message_type = tf__request__pb2._ARRAYPROTO
_PBRESPONSE_TFOUTPUTSENTRY.containing_type = _PBRESPONSE
_PBRESPONSE.fields_by_name['results'].message_type = _PBRESPONSE_RESULTSENTRY
_PBRESPONSE.fields_by_name['item_features'].message_type = _PBRESPONSE_ITEMFEATURESENTRY
_PBRESPONSE.fields_by_name['generate_features'].message_type = _PBRESPONSE_GENERATEFEATURESENTRY
_PBRESPONSE.fields_by_name['context_features'].message_type = _PBRESPONSE_CONTEXTFEATURESENTRY
_PBRESPONSE.fields_by_name['status_code'].enum_type = _STATUSCODE
_PBRESPONSE.fields_by_name['raw_features'].message_type = _PBRESPONSE_RAWFEATURESENTRY
_PBRESPONSE.fields_by_name['tf_outputs'].message_type = _PBRESPONSE_TFOUTPUTSENTRY
DESCRIPTOR.message_types_by_name['ContextFeatures'] = _CONTEXTFEATURES
DESCRIPTOR.message_types_by_name['PBFeature'] = _PBFEATURE
DESCRIPTOR.message_types_by_name['PBRequest'] = _PBREQUEST
DESCRIPTOR.message_types_by_name['Results'] = _RESULTS
DESCRIPTOR.message_types_by_name['PBResponse'] = _PBRESPONSE
DESCRIPTOR.enum_types_by_name['StatusCode'] = _STATUSCODE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ContextFeatures = _reflection.GeneratedProtocolMessageType('ContextFeatures', (_message.Message,), dict(
  DESCRIPTOR = _CONTEXTFEATURES,
  __module__ = 'predict_pb2'
  # @@protoc_insertion_point(class_scope:ContextFeatures)
  ))
_sym_db.RegisterMessage(ContextFeatures)

PBFeature = _reflection.GeneratedProtocolMessageType('PBFeature', (_message.Message,), dict(
  DESCRIPTOR = _PBFEATURE,
  __module__ = 'predict_pb2'
  # @@protoc_insertion_point(class_scope:PBFeature)
  ))
_sym_db.RegisterMessage(PBFeature)

PBRequest = _reflection.GeneratedProtocolMessageType('PBRequest', (_message.Message,), dict(

  UserFeaturesEntry = _reflection.GeneratedProtocolMessageType('UserFeaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBREQUEST_USERFEATURESENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBRequest.UserFeaturesEntry)
    ))
  ,

  ContextFeaturesEntry = _reflection.GeneratedProtocolMessageType('ContextFeaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBREQUEST_CONTEXTFEATURESENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBRequest.ContextFeaturesEntry)
    ))
  ,
  DESCRIPTOR = _PBREQUEST,
  __module__ = 'predict_pb2'
  # @@protoc_insertion_point(class_scope:PBRequest)
  ))
_sym_db.RegisterMessage(PBRequest)
_sym_db.RegisterMessage(PBRequest.UserFeaturesEntry)
_sym_db.RegisterMessage(PBRequest.ContextFeaturesEntry)

Results = _reflection.GeneratedProtocolMessageType('Results', (_message.Message,), dict(
  DESCRIPTOR = _RESULTS,
  __module__ = 'predict_pb2'
  # @@protoc_insertion_point(class_scope:Results)
  ))
_sym_db.RegisterMessage(Results)

PBResponse = _reflection.GeneratedProtocolMessageType('PBResponse', (_message.Message,), dict(

  ResultsEntry = _reflection.GeneratedProtocolMessageType('ResultsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBRESPONSE_RESULTSENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBResponse.ResultsEntry)
    ))
  ,

  ItemFeaturesEntry = _reflection.GeneratedProtocolMessageType('ItemFeaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBRESPONSE_ITEMFEATURESENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBResponse.ItemFeaturesEntry)
    ))
  ,

  GenerateFeaturesEntry = _reflection.GeneratedProtocolMessageType('GenerateFeaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBRESPONSE_GENERATEFEATURESENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBResponse.GenerateFeaturesEntry)
    ))
  ,

  ContextFeaturesEntry = _reflection.GeneratedProtocolMessageType('ContextFeaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBRESPONSE_CONTEXTFEATURESENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBResponse.ContextFeaturesEntry)
    ))
  ,

  RawFeaturesEntry = _reflection.GeneratedProtocolMessageType('RawFeaturesEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBRESPONSE_RAWFEATURESENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBResponse.RawFeaturesEntry)
    ))
  ,

  TfOutputsEntry = _reflection.GeneratedProtocolMessageType('TfOutputsEntry', (_message.Message,), dict(
    DESCRIPTOR = _PBRESPONSE_TFOUTPUTSENTRY,
    __module__ = 'predict_pb2'
    # @@protoc_insertion_point(class_scope:PBResponse.TfOutputsEntry)
    ))
  ,
  DESCRIPTOR = _PBRESPONSE,
  __module__ = 'predict_pb2'
  # @@protoc_insertion_point(class_scope:PBResponse)
  ))
_sym_db.RegisterMessage(PBResponse)
_sym_db.RegisterMessage(PBResponse.ResultsEntry)
_sym_db.RegisterMessage(PBResponse.ItemFeaturesEntry)
_sym_db.RegisterMessage(PBResponse.GenerateFeaturesEntry)
_sym_db.RegisterMessage(PBResponse.ContextFeaturesEntry)
_sym_db.RegisterMessage(PBResponse.RawFeaturesEntry)
_sym_db.RegisterMessage(PBResponse.TfOutputsEntry)


_PBREQUEST_USERFEATURESENTRY.has_options = True
_PBREQUEST_USERFEATURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PBREQUEST_CONTEXTFEATURESENTRY.has_options = True
_PBREQUEST_CONTEXTFEATURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_RESULTS.fields_by_name['scores'].has_options = True
_RESULTS.fields_by_name['scores']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
_PBRESPONSE_RESULTSENTRY.has_options = True
_PBRESPONSE_RESULTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PBRESPONSE_ITEMFEATURESENTRY.has_options = True
_PBRESPONSE_ITEMFEATURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PBRESPONSE_GENERATEFEATURESENTRY.has_options = True
_PBRESPONSE_GENERATEFEATURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PBRESPONSE_CONTEXTFEATURESENTRY.has_options = True
_PBRESPONSE_CONTEXTFEATURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PBRESPONSE_RAWFEATURESENTRY.has_options = True
_PBRESPONSE_RAWFEATURESENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_PBRESPONSE_TFOUTPUTSENTRY.has_options = True
_PBRESPONSE_TFOUTPUTSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)

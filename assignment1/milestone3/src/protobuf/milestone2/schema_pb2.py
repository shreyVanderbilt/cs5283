# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0cschema.proto\"\"\n\x05Order\x12\x19\n\x07\x63ontent\x18\x01 \x01(\x0b\x32\x08.Content\"~\n\x07\x43ontent\x12\x19\n\x07veggies\x18\x01 \x01(\x0b\x32\x08.Veggies\x12\x17\n\x06\x64rinks\x18\x02 \x01(\x0b\x32\x07.Drinks\x12\x13\n\x04milk\x18\x03 \x03(\x0b\x32\x05.Milk\x12\x15\n\x05\x62read\x18\x04 \x03(\x0b\x32\x06.Bread\x12\x13\n\x04meat\x18\x05 \x03(\x0b\x32\x05.Meat\"\xd3\x01\n\x07Veggies\x12\x13\n\x06tomato\x18\x01 \x01(\x02H\x00\x88\x01\x01\x12\x15\n\x08\x63ucumber\x18\x02 \x01(\x02H\x01\x88\x01\x01\x12\x13\n\x06pickle\x18\x03 \x01(\x02H\x02\x88\x01\x01\x12\x15\n\x08jalapeno\x18\x04 \x01(\x02H\x03\x88\x01\x01\x12\x15\n\x08mushroom\x18\x05 \x01(\x02H\x04\x88\x01\x01\x12\x12\n\x05onion\x18\x06 \x01(\x02H\x05\x88\x01\x01\x42\t\n\x07_tomatoB\x0b\n\t_cucumberB\t\n\x07_pickleB\x0b\n\t_jalapenoB\x0b\n\t_mushroomB\x08\n\x06_onion\"8\n\x06\x44rinks\x12\x13\n\x04\x63\x61ns\x18\x01 \x01(\x0b\x32\x05.Cans\x12\x19\n\x07\x62ottles\x18\x02 \x01(\x0b\x32\x08.Bottles\"r\n\x04\x43\x61ns\x12\x11\n\x04\x63oke\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x16\n\tbud_light\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x18\n\x0bmiller_lite\x18\x03 \x01(\x05H\x02\x88\x01\x01\x42\x07\n\x05_cokeB\x0c\n\n_bud_lightB\x0e\n\x0c_miller_lite\"\x87\x01\n\x07\x42ottles\x12\x13\n\x06sprite\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x12\n\x05\x66\x61nta\x18\x02 \x01(\x05H\x01\x88\x01\x01\x12\x12\n\x05pepsi\x18\x03 \x01(\x05H\x02\x88\x01\x01\x12\x14\n\x07mtn_dew\x18\x04 \x01(\x05H\x03\x88\x01\x01\x42\t\n\x07_spriteB\x08\n\x06_fantaB\x08\n\x06_pepsiB\n\n\x08_mtn_dew\"7\n\x04Milk\x12\x1d\n\tmilk_type\x18\x01 \x01(\x0e\x32\n.Milk_Type\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"7\n\x04Meat\x12\x1d\n\tmeat_Type\x18\x01 \x01(\x0e\x32\n.Meat_Type\x12\x10\n\x08quantity\x18\x02 \x01(\x05\":\n\x05\x42read\x12\x1f\n\nbread_type\x18\x01 \x01(\x0e\x32\x0b.Bread_Type\x12\x10\n\x08quantity\x18\x02 \x01(\x05\"0\n\x06Health\x12&\n\rhealthContent\x18\x01 \x01(\x0b\x32\x0f.Health_Content\"\xa7\x01\n\x0eHealth_Content\x12\x1d\n\tdispenser\x18\x01 \x01(\x0e\x32\n.Dispenser\x12\x10\n\x08icemaker\x18\x02 \x01(\x05\x12\x1a\n\tlightbulb\x18\x03 \x01(\x0e\x32\x07.Status\x12\x13\n\x0b\x66ridge_temp\x18\x04 \x01(\x05\x12\x13\n\x0b\x66reeze_temp\x18\x05 \x01(\x05\x12\x1e\n\rsensor_status\x18\x06 \x01(\x0e\x32\x07.Status\"-\n\x08Response\x12\x13\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x05.Code\x12\x0c\n\x04\x64\x61ta\x18\x02 \x01(\t*U\n\tMilk_Type\x12\t\n\x05whole\x10\x00\x12\x06\n\x02_1\x10\x01\x12\x06\n\x02_2\x10\x02\x12\x0c\n\x08\x66\x61t_free\x10\x03\x12\n\n\x06\x61lmond\x10\x04\x12\n\n\x06\x63\x61shew\x10\x05\x12\x07\n\x03oat\x10\x06*I\n\nBread_Type\x12\x0f\n\x0bwhole_wheat\x10\x00\x12\x10\n\x0cpumpernickel\x10\x01\x12\x07\n\x03rye\x10\x02\x12\x0f\n\x0bgluten_free\x10\x03*7\n\tMeat_Type\x12\x0b\n\x07\x63hicken\x10\x00\x12\x08\n\x04\x62\x65\x65\x66\x10\x01\x12\n\n\x06turkey\x10\x02\x12\x07\n\x03ham\x10\x03*\x1f\n\x04\x43ode\x12\x0f\n\x0b\x42\x41\x44_REQUEST\x10\x00\x12\x06\n\x02OK\x10\x01*3\n\tDispenser\x12\x0b\n\x07optimal\x10\x00\x12\x0b\n\x07partial\x10\x01\x12\x0c\n\x08\x62lockage\x10\x02*\x1b\n\x06Status\x12\x08\n\x04good\x10\x00\x12\x07\n\x03\x62\x61\x64\x10\x01\x32-\n\x0cOrderService\x12\x1d\n\x06method\x12\x06.Order\x1a\t.Response\"\x00\x32/\n\rHealthService\x12\x1e\n\x06method\x12\x07.Health\x1a\t.Response\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_MILK_TYPE']._serialized_start=1147
  _globals['_MILK_TYPE']._serialized_end=1232
  _globals['_BREAD_TYPE']._serialized_start=1234
  _globals['_BREAD_TYPE']._serialized_end=1307
  _globals['_MEAT_TYPE']._serialized_start=1309
  _globals['_MEAT_TYPE']._serialized_end=1364
  _globals['_CODE']._serialized_start=1366
  _globals['_CODE']._serialized_end=1397
  _globals['_DISPENSER']._serialized_start=1399
  _globals['_DISPENSER']._serialized_end=1450
  _globals['_STATUS']._serialized_start=1452
  _globals['_STATUS']._serialized_end=1479
  _globals['_ORDER']._serialized_start=16
  _globals['_ORDER']._serialized_end=50
  _globals['_CONTENT']._serialized_start=52
  _globals['_CONTENT']._serialized_end=178
  _globals['_VEGGIES']._serialized_start=181
  _globals['_VEGGIES']._serialized_end=392
  _globals['_DRINKS']._serialized_start=394
  _globals['_DRINKS']._serialized_end=450
  _globals['_CANS']._serialized_start=452
  _globals['_CANS']._serialized_end=566
  _globals['_BOTTLES']._serialized_start=569
  _globals['_BOTTLES']._serialized_end=704
  _globals['_MILK']._serialized_start=706
  _globals['_MILK']._serialized_end=761
  _globals['_MEAT']._serialized_start=763
  _globals['_MEAT']._serialized_end=818
  _globals['_BREAD']._serialized_start=820
  _globals['_BREAD']._serialized_end=878
  _globals['_HEALTH']._serialized_start=880
  _globals['_HEALTH']._serialized_end=928
  _globals['_HEALTH_CONTENT']._serialized_start=931
  _globals['_HEALTH_CONTENT']._serialized_end=1098
  _globals['_RESPONSE']._serialized_start=1100
  _globals['_RESPONSE']._serialized_end=1145
  _globals['_ORDERSERVICE']._serialized_start=1481
  _globals['_ORDERSERVICE']._serialized_end=1526
  _globals['_HEALTHSERVICE']._serialized_start=1528
  _globals['_HEALTHSERVICE']._serialized_end=1575
# @@protoc_insertion_point(module_scope)

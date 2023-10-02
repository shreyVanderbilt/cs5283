from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Milk_Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    whole: _ClassVar[Milk_Type]
    _1: _ClassVar[Milk_Type]
    _2: _ClassVar[Milk_Type]
    fat_free: _ClassVar[Milk_Type]
    almond: _ClassVar[Milk_Type]
    cashew: _ClassVar[Milk_Type]
    oat: _ClassVar[Milk_Type]

class Bread_Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    whole_wheat: _ClassVar[Bread_Type]
    pumpernickel: _ClassVar[Bread_Type]
    rye: _ClassVar[Bread_Type]
    gluten_free: _ClassVar[Bread_Type]

class Meat_Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    chicken: _ClassVar[Meat_Type]
    beef: _ClassVar[Meat_Type]
    turkey: _ClassVar[Meat_Type]
    ham: _ClassVar[Meat_Type]

class Code(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    BAD_REQUEST: _ClassVar[Code]
    OK: _ClassVar[Code]

class Dispenser(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    optimal: _ClassVar[Dispenser]
    partial: _ClassVar[Dispenser]
    blockage: _ClassVar[Dispenser]

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    good: _ClassVar[Status]
    bad: _ClassVar[Status]
whole: Milk_Type
_1: Milk_Type
_2: Milk_Type
fat_free: Milk_Type
almond: Milk_Type
cashew: Milk_Type
oat: Milk_Type
whole_wheat: Bread_Type
pumpernickel: Bread_Type
rye: Bread_Type
gluten_free: Bread_Type
chicken: Meat_Type
beef: Meat_Type
turkey: Meat_Type
ham: Meat_Type
BAD_REQUEST: Code
OK: Code
optimal: Dispenser
partial: Dispenser
blockage: Dispenser
good: Status
bad: Status

class Order(_message.Message):
    __slots__ = ["content"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: Content
    def __init__(self, content: _Optional[_Union[Content, _Mapping]] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ["veggies", "drinks", "milk", "bread", "meat"]
    VEGGIES_FIELD_NUMBER: _ClassVar[int]
    DRINKS_FIELD_NUMBER: _ClassVar[int]
    MILK_FIELD_NUMBER: _ClassVar[int]
    BREAD_FIELD_NUMBER: _ClassVar[int]
    MEAT_FIELD_NUMBER: _ClassVar[int]
    veggies: Veggies
    drinks: Drinks
    milk: _containers.RepeatedCompositeFieldContainer[Milk]
    bread: _containers.RepeatedCompositeFieldContainer[Bread]
    meat: _containers.RepeatedCompositeFieldContainer[Meat]
    def __init__(self, veggies: _Optional[_Union[Veggies, _Mapping]] = ..., drinks: _Optional[_Union[Drinks, _Mapping]] = ..., milk: _Optional[_Iterable[_Union[Milk, _Mapping]]] = ..., bread: _Optional[_Iterable[_Union[Bread, _Mapping]]] = ..., meat: _Optional[_Iterable[_Union[Meat, _Mapping]]] = ...) -> None: ...

class Veggies(_message.Message):
    __slots__ = ["tomato", "cucumber", "pickle", "jalapeno", "mushroom", "onion"]
    TOMATO_FIELD_NUMBER: _ClassVar[int]
    CUCUMBER_FIELD_NUMBER: _ClassVar[int]
    PICKLE_FIELD_NUMBER: _ClassVar[int]
    JALAPENO_FIELD_NUMBER: _ClassVar[int]
    MUSHROOM_FIELD_NUMBER: _ClassVar[int]
    ONION_FIELD_NUMBER: _ClassVar[int]
    tomato: float
    cucumber: float
    pickle: float
    jalapeno: float
    mushroom: float
    onion: float
    def __init__(self, tomato: _Optional[float] = ..., cucumber: _Optional[float] = ..., pickle: _Optional[float] = ..., jalapeno: _Optional[float] = ..., mushroom: _Optional[float] = ..., onion: _Optional[float] = ...) -> None: ...

class Drinks(_message.Message):
    __slots__ = ["cans", "bottles"]
    CANS_FIELD_NUMBER: _ClassVar[int]
    BOTTLES_FIELD_NUMBER: _ClassVar[int]
    cans: Cans
    bottles: Bottles
    def __init__(self, cans: _Optional[_Union[Cans, _Mapping]] = ..., bottles: _Optional[_Union[Bottles, _Mapping]] = ...) -> None: ...

class Cans(_message.Message):
    __slots__ = ["coke", "bud_light", "miller_lite"]
    COKE_FIELD_NUMBER: _ClassVar[int]
    BUD_LIGHT_FIELD_NUMBER: _ClassVar[int]
    MILLER_LITE_FIELD_NUMBER: _ClassVar[int]
    coke: int
    bud_light: int
    miller_lite: int
    def __init__(self, coke: _Optional[int] = ..., bud_light: _Optional[int] = ..., miller_lite: _Optional[int] = ...) -> None: ...

class Bottles(_message.Message):
    __slots__ = ["sprite", "fanta", "pepsi", "mtn_dew"]
    SPRITE_FIELD_NUMBER: _ClassVar[int]
    FANTA_FIELD_NUMBER: _ClassVar[int]
    PEPSI_FIELD_NUMBER: _ClassVar[int]
    MTN_DEW_FIELD_NUMBER: _ClassVar[int]
    sprite: int
    fanta: int
    pepsi: int
    mtn_dew: int
    def __init__(self, sprite: _Optional[int] = ..., fanta: _Optional[int] = ..., pepsi: _Optional[int] = ..., mtn_dew: _Optional[int] = ...) -> None: ...

class Milk(_message.Message):
    __slots__ = ["milk_type", "quantity"]
    MILK_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    milk_type: Milk_Type
    quantity: int
    def __init__(self, milk_type: _Optional[_Union[Milk_Type, str]] = ..., quantity: _Optional[int] = ...) -> None: ...

class Meat(_message.Message):
    __slots__ = ["meat_Type", "quantity"]
    MEAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    meat_Type: Meat_Type
    quantity: int
    def __init__(self, meat_Type: _Optional[_Union[Meat_Type, str]] = ..., quantity: _Optional[int] = ...) -> None: ...

class Bread(_message.Message):
    __slots__ = ["bread_type", "quantity"]
    BREAD_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    bread_type: Bread_Type
    quantity: int
    def __init__(self, bread_type: _Optional[_Union[Bread_Type, str]] = ..., quantity: _Optional[int] = ...) -> None: ...

class Health(_message.Message):
    __slots__ = ["healthContent"]
    HEALTHCONTENT_FIELD_NUMBER: _ClassVar[int]
    healthContent: Health_Content
    def __init__(self, healthContent: _Optional[_Union[Health_Content, _Mapping]] = ...) -> None: ...

class Health_Content(_message.Message):
    __slots__ = ["dispenser", "icemaker", "lightbulb", "fridge_temp", "freeze_temp", "sensor_status"]
    DISPENSER_FIELD_NUMBER: _ClassVar[int]
    ICEMAKER_FIELD_NUMBER: _ClassVar[int]
    LIGHTBULB_FIELD_NUMBER: _ClassVar[int]
    FRIDGE_TEMP_FIELD_NUMBER: _ClassVar[int]
    FREEZE_TEMP_FIELD_NUMBER: _ClassVar[int]
    SENSOR_STATUS_FIELD_NUMBER: _ClassVar[int]
    dispenser: Dispenser
    icemaker: int
    lightbulb: Status
    fridge_temp: int
    freeze_temp: int
    sensor_status: Status
    def __init__(self, dispenser: _Optional[_Union[Dispenser, str]] = ..., icemaker: _Optional[int] = ..., lightbulb: _Optional[_Union[Status, str]] = ..., fridge_temp: _Optional[int] = ..., freeze_temp: _Optional[int] = ..., sensor_status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ["code", "data"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    code: Code
    data: str
    def __init__(self, code: _Optional[_Union[Code, str]] = ..., data: _Optional[str] = ...) -> None: ...

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: OrderAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class MEAT(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = MEAT()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsMEAT(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # MEAT
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # MEAT
    def MeatType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int8Flags, o + self._tab.Pos)
        return 0

    # MEAT
    def Quantity(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(2)
def MEATStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddMeatType(builder, meatType): builder.PrependInt8Slot(0, meatType, 0)
def MEATAddMeatType(builder, meatType):
    """This method is deprecated. Please switch to AddMeatType."""
    return AddMeatType(builder, meatType)
def AddQuantity(builder, quantity): builder.PrependFloat32Slot(1, quantity, 0.0)
def MEATAddQuantity(builder, quantity):
    """This method is deprecated. Please switch to AddQuantity."""
    return AddQuantity(builder, quantity)
def End(builder): return builder.EndObject()
def MEATEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
# automatically generated by the FlatBuffers compiler, do not modify

# namespace: OrderAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class VEGGIES(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = VEGGIES()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsVEGGIES(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # VEGGIES
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # VEGGIES
    def Tomato(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # VEGGIES
    def Cucumber(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # VEGGIES
    def Pickle(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # VEGGIES
    def Jalapeno(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # VEGGIES
    def Mushroom(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

    # VEGGIES
    def Onion(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 0.0

def Start(builder): builder.StartObject(6)
def VEGGIESStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddTomato(builder, tomato): builder.PrependFloat32Slot(0, tomato, 0.0)
def VEGGIESAddTomato(builder, tomato):
    """This method is deprecated. Please switch to AddTomato."""
    return AddTomato(builder, tomato)
def AddCucumber(builder, cucumber): builder.PrependFloat32Slot(1, cucumber, 0.0)
def VEGGIESAddCucumber(builder, cucumber):
    """This method is deprecated. Please switch to AddCucumber."""
    return AddCucumber(builder, cucumber)
def AddPickle(builder, pickle): builder.PrependFloat32Slot(2, pickle, 0.0)
def VEGGIESAddPickle(builder, pickle):
    """This method is deprecated. Please switch to AddPickle."""
    return AddPickle(builder, pickle)
def AddJalapeno(builder, jalapeno): builder.PrependFloat32Slot(3, jalapeno, 0.0)
def VEGGIESAddJalapeno(builder, jalapeno):
    """This method is deprecated. Please switch to AddJalapeno."""
    return AddJalapeno(builder, jalapeno)
def AddMushroom(builder, mushroom): builder.PrependFloat32Slot(4, mushroom, 0.0)
def VEGGIESAddMushroom(builder, mushroom):
    """This method is deprecated. Please switch to AddMushroom."""
    return AddMushroom(builder, mushroom)
def AddOnion(builder, onion): builder.PrependFloat32Slot(5, onion, 0.0)
def VEGGIESAddOnion(builder, onion):
    """This method is deprecated. Please switch to AddOnion."""
    return AddOnion(builder, onion)
def End(builder): return builder.EndObject()
def VEGGIESEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
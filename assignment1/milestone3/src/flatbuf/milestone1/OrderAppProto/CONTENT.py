# automatically generated by the FlatBuffers compiler, do not modify

# namespace: OrderAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CONTENT(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CONTENT()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCONTENT(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CONTENT
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CONTENT
    def Veggies(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from OrderAppProto.VEGGIES import VEGGIES
            obj = VEGGIES()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CONTENT
    def Drinks(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from OrderAppProto.DRINKS import DRINKS
            obj = DRINKS()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CONTENT
    def Milk(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from OrderAppProto.MILK import MILK
            obj = MILK()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CONTENT
    def MilkLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CONTENT
    def MilkIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

    # CONTENT
    def Bread(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from OrderAppProto.BREAD import BREAD
            obj = BREAD()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CONTENT
    def BreadLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CONTENT
    def BreadIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        return o == 0

    # CONTENT
    def Meat(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from OrderAppProto.MEAT import MEAT
            obj = MEAT()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CONTENT
    def MeatLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # CONTENT
    def MeatIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        return o == 0

def Start(builder): builder.StartObject(5)
def CONTENTStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddVeggies(builder, veggies): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(veggies), 0)
def CONTENTAddVeggies(builder, veggies):
    """This method is deprecated. Please switch to AddVeggies."""
    return AddVeggies(builder, veggies)
def AddDrinks(builder, drinks): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(drinks), 0)
def CONTENTAddDrinks(builder, drinks):
    """This method is deprecated. Please switch to AddDrinks."""
    return AddDrinks(builder, drinks)
def AddMilk(builder, milk): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(milk), 0)
def CONTENTAddMilk(builder, milk):
    """This method is deprecated. Please switch to AddMilk."""
    return AddMilk(builder, milk)
def StartMilkVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CONTENTStartMilkVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMilkVector(builder, numElems)
def AddBread(builder, bread): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(bread), 0)
def CONTENTAddBread(builder, bread):
    """This method is deprecated. Please switch to AddBread."""
    return AddBread(builder, bread)
def StartBreadVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CONTENTStartBreadVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartBreadVector(builder, numElems)
def AddMeat(builder, meat): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(meat), 0)
def CONTENTAddMeat(builder, meat):
    """This method is deprecated. Please switch to AddMeat."""
    return AddMeat(builder, meat)
def StartMeatVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def CONTENTStartMeatVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartMeatVector(builder, numElems)
def End(builder): return builder.EndObject()
def CONTENTEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
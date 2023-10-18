# automatically generated by the FlatBuffers compiler, do not modify

# namespace: OrderAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CANS(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 12

    # CANS
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CANS
    def Coke(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # CANS
    def BudLight(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))
    # CANS
    def MillerLite(self): return self._tab.Get(flatbuffers.number_types.Int32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(8))

def CreateCANS(builder, coke, budLight, millerLite):
    builder.Prep(4, 12)
    builder.PrependInt32(millerLite)
    builder.PrependInt32(budLight)
    builder.PrependInt32(coke)
    return builder.Offset()

# automatically generated by the FlatBuffers compiler, do not modify

# namespace: OrderAppProto

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ORDER(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ORDER()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsORDER(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ORDER
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ORDER
    def Contents(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from OrderAppProto.CONTENT import CONTENT
            obj = CONTENT()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(1)
def ORDERStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddContents(builder, contents): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(contents), 0)
def ORDERAddContents(builder, contents):
    """This method is deprecated. Please switch to AddContents."""
    return AddContents(builder, contents)
def End(builder): return builder.EndObject()
def ORDEREnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)
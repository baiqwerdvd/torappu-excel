from ..common import BaseStruct


class KeyFrames_2(BaseStruct):
    pass

    class KeyFrame(BaseStruct):
        level: int
        data: object

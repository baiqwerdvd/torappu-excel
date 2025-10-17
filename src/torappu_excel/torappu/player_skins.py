from ..common import BaseStruct


class PlayerSkins(BaseStruct):
    characterSkins: dict[str, int]
    skinTs: dict[str, int]
    skinSp: dict[str, int]

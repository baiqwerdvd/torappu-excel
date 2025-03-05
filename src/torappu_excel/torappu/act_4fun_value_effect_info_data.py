from ..common import BaseStruct


class Act4funValueEffectInfoData(BaseStruct):
    valueEffectId: str
    effectParams: dict[str, int]

from ..common import BaseStruct


class ArkdexAdvantageTypeData(BaseStruct):
    advantageType: str
    sortId: int
    name: str
    typeIcon: str
    entryEffectKey: str
    damageScaleMap: dict[str, float]

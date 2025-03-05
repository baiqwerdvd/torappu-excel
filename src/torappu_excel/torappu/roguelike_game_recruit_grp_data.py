from ..common import BaseStruct

from msgspec import field


class RoguelikeGameRecruitGrpData(BaseStruct):
    id_: str = field(name="id")
    iconId: str
    name: str
    desc: str
    unlockDesc: str | None

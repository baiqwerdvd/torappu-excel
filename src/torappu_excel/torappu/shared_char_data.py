# pyright: reportUnknownArgumentType=false
from ..common import BaseStruct

from msgspec import field


class SharedCharData(BaseStruct):
    charId: str
    potentialRank: int
    mainSkillLvl: int
    evolvePhase: int
    level: int
    favorPoint: int
    currentEquip: str | None = field(name="currentEquip", default=None)
    equips: dict[str, "SharedCharData.CharEquipInfo"] | None = field(name="equip", default={})
    skillIndex: int | None = field(default=None)
    skinId: str | None = field(default=None)
    skin: str | None = field(default=None)
    skills: list["SharedCharData.SharedCharSkillData"] | None = field(default=None)
    crisisRecord: dict[str, int] | None = field(default=None)
    crisisV2Record: dict[str, int] | None = field(default=None)
    currentTmpl: str | None = field(default=None)
    tmpl: dict[str, "SharedCharData.TmplData"] | None = field(default=None)

    class CharEquipInfo(BaseStruct):
        hide: int
        locked: bool | int
        level: int

    class SharedCharSkillData(BaseStruct):
        skillId: str
        specializeLevel: int
        completeUpgradeTime: int | None = field(default=None)
        unlock: bool | int | None = field(default=None)
        state: int | None = field(default=None)

    class TmplData(BaseStruct):
        skinId: str
        defaultSkillIndex: int
        skills: list["SharedCharData.SharedCharSkillData"]
        currentEquip: str | None
        equip: dict[str, "SharedCharData.SharedCharSkillData"] | None = field(default=None)

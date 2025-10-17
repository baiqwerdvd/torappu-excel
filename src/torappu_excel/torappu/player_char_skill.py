from ..common import BaseStruct


class PlayerCharSkill(BaseStruct):
    unlock: int
    skillId: str
    state: int
    specializeLevel: int
    completeUpgradeTime: int

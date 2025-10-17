from .roguelike_recruit_upgrade_character import RoguelikeRecruitUpgradeCharacter
from ..common import BaseStruct


class PlayerRoguelikeItem(BaseStruct):
    index: str
    id: str
    count: int
    ts: int
    recruit: list[RoguelikeRecruitUpgradeCharacter]
    upgrade: list[RoguelikeRecruitUpgradeCharacter]

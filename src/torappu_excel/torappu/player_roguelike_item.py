from pydantic import BaseModel, ConfigDict

from .roguelike_recruit_upgrade_character import RoguelikeRecruitUpgradeCharacter


class PlayerRoguelikeItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    index: str
    id: str
    count: int
    ts: int
    recruit: list[RoguelikeRecruitUpgradeCharacter]
    upgrade: list[RoguelikeRecruitUpgradeCharacter]

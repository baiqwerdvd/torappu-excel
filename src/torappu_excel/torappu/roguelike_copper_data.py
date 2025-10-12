from pydantic import BaseModel, ConfigDict

from .roguelike_copper_buff_type import RoguelikeCopperBuffType
from .roguelike_copper_lucky_level import RoguelikeCopperLuckyLevel


class RoguelikeCopperData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    groupId: str
    gildTypeId: str | None
    luckyLevel: RoguelikeCopperLuckyLevel
    buffType: RoguelikeCopperBuffType
    layerCntDesc: str
    poemList: list[str]
    alwaysShowCountDown: bool
    buffItemIdList: list[str]

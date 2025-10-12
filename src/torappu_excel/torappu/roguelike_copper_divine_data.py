from pydantic import BaseModel, ConfigDict

from .roguelike_copper_divine_result_type import RoguelikeCopperDivineResultType
from .roguelike_copper_divine_type import RoguelikeCopperDivineType


class RoguelikeCopperDivineData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    eventId: str
    groupId: str
    showDesc: str
    divineType: RoguelikeCopperDivineType
    resultType: RoguelikeCopperDivineResultType

from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class HandbookDisplayCondition(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    class DisplayType(StrEnum):
        DISPLAY_IF_CHAREXIST = "DISPLAY_IF_CHAREXIST"
        INVISIBLE_IF_CHAREXIST = "INVISIBLE_IF_CHAREXIST"

    charId: str
    conditionCharId: str
    type: "HandbookDisplayCondition.DisplayType"

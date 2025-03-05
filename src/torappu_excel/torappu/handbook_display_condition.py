from enum import StrEnum

from ..common import BaseStruct

from msgspec import field


class HandbookDisplayCondition(BaseStruct):
    class DisplayType(StrEnum):
        DISPLAY_IF_CHAREXIST = "DISPLAY_IF_CHAREXIST"
        INVISIBLE_IF_CHAREXIST = "INVISIBLE_IF_CHAREXIST"

    charId: str
    conditionCharId: str
    type_: "HandbookDisplayCondition.DisplayType" = field(name="type")

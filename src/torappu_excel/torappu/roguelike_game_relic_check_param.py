from .profession_category import ProfessionCategory
from ..common import BaseStruct


class RoguelikeGameRelicCheckParam(BaseStruct):
    valueProfessionMask: ProfessionCategory | int
    valueStrs: list[str] | None
    valueInt: int

from ..common import BaseStruct


class RoguelikeLegacyItemData(BaseStruct):
    legacyId: str
    hideLegacyItem: bool
    legacyGroupId: str | None

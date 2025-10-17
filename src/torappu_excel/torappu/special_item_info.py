from msgspec import field

from ..common import BaseStruct


class SpecialItemInfo(BaseStruct):
    showPreview: bool
    specialDesc: str
    specialBtnText: str | None = field(default=None)

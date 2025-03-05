from ..common import BaseStruct

from msgspec import field


class SpecialItemInfo(BaseStruct):
    showPreview: bool
    specialDesc: str
    specialBtnText: str | None = field(default=None)

from ..common import BaseStruct


class ResolutionSettingItemData(BaseStruct):
    sortId: int
    resolutionWidth: int
    resolutionHeight: int
    resolutionText: str
    isFullScreen: bool
    isBorderless: bool

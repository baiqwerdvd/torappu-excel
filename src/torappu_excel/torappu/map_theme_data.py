from ..common import BaseStruct


class MapThemeData(BaseStruct):
    themeId: str
    unitColor: str
    buildableColor: str | None
    themeType: str | None
    trapTintColor: str | None

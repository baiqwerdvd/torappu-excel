from ..common import BaseStruct


class PlayerNameCardSkin(BaseStruct):
    selected: str
    state: dict[str, "PlayerNameCardSkin.SkinState"]
    tmpl: dict[str, int]

    class SkinState(BaseStruct):
        unlock: bool
        progress: list[list[int]] | None

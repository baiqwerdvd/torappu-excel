from ..common import BaseStruct


class PlayerTemplateTrap(BaseStruct):
    domains: dict[str, "PlayerTemplateTrap.Domin"]

    class Trap(BaseStruct):
        count: int

    class Domin(BaseStruct):
        traps: dict[str, "PlayerTemplateTrap.Trap"]
        squad: list[str]

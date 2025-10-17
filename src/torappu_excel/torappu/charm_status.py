from ..common import BaseStruct


class CharmStatus(BaseStruct):
    charms: dict[str, int]
    squad: list[str]

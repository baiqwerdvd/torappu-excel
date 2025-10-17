from ..common import BaseStruct


class PlayerCollection(BaseStruct):
    team: dict[str, int]

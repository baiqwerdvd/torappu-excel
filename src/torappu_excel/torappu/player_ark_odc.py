from ..common import BaseStruct


class PlayerArkOdcTopic(BaseStruct):
    position: "PlayerArkOdcTopic.Position"
    rewards: dict[str, int]
    varSeqs: dict[str, int]

    class Position(BaseStruct):
        x: float
        y: float
        z: float


class PlayerArkOdc(BaseStruct):
    topics: dict[str, PlayerArkOdcTopic]

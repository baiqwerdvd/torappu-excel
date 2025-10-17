from ..common import BaseStruct


class PlayerBuildingTradingBuff(BaseStruct):
    speed: float
    limit: int
    apCost: "PlayerBuildingTradingBuff.APCost"
    rate: dict[str, float | int]
    tgw: list[tuple[str, dict[str, int], int]]
    point: dict[str, int]
    manuLines: dict[str, int]
    orderBuff: list[tuple[str, bool, int, int, str]]
    violatedInfo: "PlayerBuildingTradingBuff.ViolatedInfo"
    orderWtBuff: list["PlayerBuildingTradingBuff.OrderWtBuff"]
    speGoldOrder: "PlayerBuildingTradingBuff.SpeGoldOrder"

    class APCost(BaseStruct):
        self: dict[str, int]
        all: int
        single: dict[str, int]

    class ViolatedInfo(BaseStruct):
        orderChecker: list["PlayerBuildingTradingBuff.ViolatedInfo.OrderChecker"]
        cntBuff: list["PlayerBuildingTradingBuff.ViolatedInfo.CntBuff"]

        class OrderChecker(BaseStruct):
            itemId: str
            ordTyp: str
            cnt: int

        class CntBuff(BaseStruct):
            itemId: str
            ordTyp: str
            itemCnt: int
            coinId: str
            coinCnt: int

    class OrderWtBuff(BaseStruct):
        itemId: str
        orderType: str
        cnt: int

    class SpeGoldOrder(BaseStruct):
        activated: bool

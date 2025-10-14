from pydantic import BaseModel, ConfigDict


class PlayerBuildingTradingBuff(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

    class APCost(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        self: dict[str, int]
        all: int
        single: dict[str, int]

    class ViolatedInfo(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        orderChecker: list["PlayerBuildingTradingBuff.ViolatedInfo.OrderChecker"]
        cntBuff: list["PlayerBuildingTradingBuff.ViolatedInfo.CntBuff"]

        class OrderChecker(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            itemId: str
            ordTyp: str
            cnt: int

        class CntBuff(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            itemId: str
            ordTyp: str
            itemCnt: int
            coinId: str
            coinCnt: int

    class OrderWtBuff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        itemId: str
        orderType: str
        cnt: int

    class SpeGoldOrder(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        activated: bool

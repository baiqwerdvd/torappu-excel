from pydantic import BaseModel, ConfigDict


class MileStonePlayerInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    points: dict[str, int]
    got: dict[str, "MileStonePlayerInfo.MileStoneRewardTicketItem"]

    class MileStoneRewardTicketItem(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        ts: int
        count: int

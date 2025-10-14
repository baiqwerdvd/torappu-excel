from pydantic import BaseModel, ConfigDict


class PlayerCheckIn(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    canCheckIn: bool
    checkInGroupId: str
    checkInRewardIndex: int
    checkInHistory: list[bool]
    newbiePackage: "PlayerCheckIn.PlayerNewbiePackage"
    showCount: int
    longTermRecvRecord: dict[str, int]

    class PlayerNewbiePackage(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        open: bool
        groupId: str
        checkInHistory: list[int]
        finish: int
        stopSale: int

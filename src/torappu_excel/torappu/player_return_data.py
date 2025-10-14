from enum import StrEnum

from pydantic import BaseModel, ConfigDict


class PlayerReturnData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    open: bool
    current: "PlayerReturnData.CurrentData | None"
    currentV2: "PlayerReturnData.CurrentV2Data | None" = None
    version: "PlayerReturnData.Version | None" = None

    class Version(StrEnum):
        OLD = "OLD"
        NEW = "NEW"

    class CurrentData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        start: int
        lastOnlineTs: int
        mission: "PlayerReturnData.Mission"
        checkIn: "PlayerReturnData.CheckIn"
        fullOpen: "PlayerReturnData.FullOpen"
        reward: bool

    class CurrentV2Data(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        start: int
        finishTs: int
        lastOnlineTs: int
        checkIn: "PlayerReturnData.CheckInV2"
        fullOpen: "PlayerReturnData.FullOpen"
        mission: "PlayerReturnData.MissionV2"
        reward: bool
        backGiftPack: "PlayerReturnData.GiftPackData"
        cumulativeLoginPack: "PlayerReturnData.LoginPackData"

    class GiftPackData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        packs: dict[str, "PlayerReturnData.GiftPackItemData"]

    class GiftPackItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        boughtCount: int
        saleEndAt: int

    class LoginPackData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        hasBought: bool
        groupId: str
        loginRecord: int
        recvStage: int
        checkinFinTs: int
        gpSaleEndAt: int

    class MissionV2(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        point: int
        stageAwardSt: list[int]
        dailySupplySt: list[int]
        long: dict[str, "list[PlayerReturnData.MissionV2Data]"]

    class MissionV2Data(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        current: int
        target: int
        status: int

    class MissionLongData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        current: float
        target: float
        status: int

    class MissionDailyData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        missionId: str
        missionGroupId: str
        current: float
        target: float
        status: int

    class Mission(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        point: int
        long: "list[PlayerReturnData.MissionLongData]"
        daily: "list[PlayerReturnData.MissionDailyData]"
        reward: bool

    class CheckIn(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        history: list[int]

    class CheckInV2(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        groupId: str
        history: list[int]

    class FullOpen(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        last: int
        today: bool
        remain: int

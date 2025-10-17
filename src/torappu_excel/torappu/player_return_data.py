from enum import StrEnum

from ..common import BaseStruct


class PlayerReturnData(BaseStruct):
    open: bool
    current: "PlayerReturnData.CurrentData | None"
    currentV2: "PlayerReturnData.CurrentV2Data | None" = None
    version: "PlayerReturnData.Version | None" = None

    class Version(StrEnum):
        OLD = "OLD"
        NEW = "NEW"

    class CurrentData(BaseStruct):
        start: int
        lastOnlineTs: int
        mission: "PlayerReturnData.Mission"
        checkIn: "PlayerReturnData.CheckIn"
        fullOpen: "PlayerReturnData.FullOpen"
        reward: bool

    class CurrentV2Data(BaseStruct):
        start: int
        finishTs: int
        lastOnlineTs: int
        checkIn: "PlayerReturnData.CheckInV2"
        fullOpen: "PlayerReturnData.FullOpen"
        mission: "PlayerReturnData.MissionV2"
        reward: bool
        backGiftPack: "PlayerReturnData.GiftPackData"
        cumulativeLoginPack: "PlayerReturnData.LoginPackData"

    class GiftPackData(BaseStruct):
        packs: dict[str, "PlayerReturnData.GiftPackItemData"]

    class GiftPackItemData(BaseStruct):
        boughtCount: int
        saleEndAt: int

    class LoginPackData(BaseStruct):
        hasBought: bool
        groupId: str
        loginRecord: int
        recvStage: int
        checkinFinTs: int
        gpSaleEndAt: int

    class MissionV2(BaseStruct):
        point: int
        stageAwardSt: list[int]
        dailySupplySt: list[int]
        long: dict[str, "list[PlayerReturnData.MissionV2Data]"]

    class MissionV2Data(BaseStruct):
        missionId: str
        current: int
        target: int
        status: int

    class MissionLongData(BaseStruct):
        missionId: str
        current: float
        target: float
        status: int

    class MissionDailyData(BaseStruct):
        missionId: str
        missionGroupId: str
        current: float
        target: float
        status: int

    class Mission(BaseStruct):
        point: int
        long: "list[PlayerReturnData.MissionLongData]"
        daily: "list[PlayerReturnData.MissionDailyData]"
        reward: bool

    class CheckIn(BaseStruct):
        history: list[int]

    class CheckInV2(BaseStruct):
        groupId: str
        history: list[int]

    class FullOpen(BaseStruct):
        last: int
        today: bool
        remain: int

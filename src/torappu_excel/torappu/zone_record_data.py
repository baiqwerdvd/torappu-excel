from pydantic import BaseModel, ConfigDict

from .record_reward_info import RecordRewardInfo


class ZoneRecordData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recordId: str
    zoneId: str
    recordTitleName: str
    preRecordId: str | None
    nodeTitle1: str | None
    nodeTitle2: str | None
    rewards: list[RecordRewardInfo]

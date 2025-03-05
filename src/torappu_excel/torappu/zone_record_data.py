from .record_reward_info import RecordRewardInfo
from ..common import BaseStruct


class ZoneRecordData(BaseStruct):
    recordId: str
    zoneId: str
    recordTitleName: str
    preRecordId: str | None
    nodeTitle1: str | None
    nodeTitle2: str | None
    rewards: list[RecordRewardInfo]

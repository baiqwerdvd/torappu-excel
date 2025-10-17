from .item_bundle import ItemBundle
from .record_reward_stage_diff import RecordRewardStageDiff
from .stage_diff_group import StageDiffGroup
from ..common import BaseStruct


class RecordRewardInfo(BaseStruct):
    bindStageId: str
    stageDiff1: RecordRewardStageDiff
    stageDiff: StageDiffGroup
    picRes: str | None
    textPath: str | None
    textDesc: str | None
    recordReward: list[ItemBundle] | None

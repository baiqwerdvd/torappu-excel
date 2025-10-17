from .retro_trail_reward_item import RetroTrailRewardItem
from ..common import BaseStruct


class RetroTrailData(BaseStruct):
    retroId: str
    trailStartTime: int
    trailRewardList: list[RetroTrailRewardItem]
    stageList: list[str]
    relatedChar: str
    relatedFullPotentialItemId: str | None
    themeColor: str
    fullPotentialItemId: str | None

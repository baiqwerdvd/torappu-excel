from pydantic import BaseModel, ConfigDict

from .retro_trail_reward_item import RetroTrailRewardItem


class RetroTrailData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    retroId: str
    trailStartTime: int
    trailRewardList: list[RetroTrailRewardItem]
    stageList: list[str]
    relatedChar: str
    relatedFullPotentialItemId: str | None
    themeColor: str
    fullPotentialItemId: str | None

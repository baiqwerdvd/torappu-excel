from enum import StrEnum

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle
from .player_stage_state import PlayerStageState


class StoryData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    needCommit: bool
    repeatable: bool
    disabled: bool
    videoResource: bool
    trigger: "StoryData.Trigger"
    condition: "StoryData.Condition | None"
    setProgress: int
    setFlags: list[str] | None
    completedRewards: list[ItemBundle] | None

    class Trigger(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        class TriggerType(StrEnum):
            GAME_START = "GAME_START"
            BEFORE_BATTLE = "BEFORE_BATTLE"
            AFTER_BATTLE = "AFTER_BATTLE"
            SWITCH_TO_SCENE = "SWITCH_TO_SCENE"
            PAGE_LOADED = "PAGE_LOADED"
            STORY_FINISH = "STORY_FINISH"
            CUSTOM_OPERATION = "CUSTOM_OPERATION"
            STORY_FINISH_OR_PAGE_LOADED = "STORY_FINISH_OR_PAGE_LOADED"
            ACTIVITY_LOADED = "ACTIVITY_LOADED"
            ACTIVITY_ANNOUNCE = "ACTIVITY_ANNOUNCE"
            CRISIS_SEASON_LOADED = "CRISIS_SEASON_LOADED"
            STORY_FINISH_OR_CUSTOM_OPERATION = "STORY_FINISH_OR_CUSTOM_OPERATION"
            E_NUM = "E_NUM"

        type: "StoryData.Trigger.TriggerType"
        key: str | None
        useRegex: bool

    class Condition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        minProgress: int
        maxProgress: int
        minPlayerLevel: int
        requiredFlags: list[str]
        excludedFlags: list[str]
        requiredStages: list["StoryData.Condition.StageCondition"]

        class StageCondition(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            stageId: str
            minState: PlayerStageState
            maxState: PlayerStageState

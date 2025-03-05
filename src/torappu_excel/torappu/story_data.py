from enum import StrEnum

from .item_bundle import ItemBundle
from .player_stage_state import PlayerStageState
from ..common import BaseStruct

from msgspec import field


class StoryData(BaseStruct):
    id_: str = field(name="id")
    needCommit: bool
    repeatable: bool
    disabled: bool
    videoResource: bool
    trigger: "StoryData.Trigger"
    condition: "StoryData.Condition | None"
    setProgress: int
    setFlags: list[str] | None
    completedRewards: list[ItemBundle] | None

    class Trigger(BaseStruct):
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

        type_: "StoryData.Trigger.TriggerType" = field(name="type")
        key: str | None
        useRegex: bool

    class Condition(BaseStruct):
        minProgress: int
        maxProgress: int
        minPlayerLevel: int
        requiredFlags: list[str]
        excludedFlags: list[str]
        requiredStages: list["StoryData.Condition.StageCondition"]

        class StageCondition(BaseStruct):
            stageId: str
            minState: PlayerStageState
            maxState: PlayerStageState

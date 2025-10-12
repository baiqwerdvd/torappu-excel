from pydantic import BaseModel, ConfigDict

from .roguelike_activity_basic_data import RoguelikeActivityBasicData
from .roguelike_activity_table import RoguelikeActivityTable


class RoguelikeActivityData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    basicDatas: dict[str, RoguelikeActivityBasicData]
    activityTable: RoguelikeActivityTable

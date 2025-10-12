from pydantic import BaseModel, ConfigDict

from .act_archive_timeline_item_data import ActArchiveTimelineItemData


class ActArchiveTimelineData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    timelineList: list[ActArchiveTimelineItemData]

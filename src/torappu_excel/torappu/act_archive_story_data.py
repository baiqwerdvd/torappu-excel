from pydantic import BaseModel, ConfigDict

from .act_archive_story_item_data import ActArchiveStoryItemData


class ActArchiveStoryData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    stories: dict[str, ActArchiveStoryItemData]

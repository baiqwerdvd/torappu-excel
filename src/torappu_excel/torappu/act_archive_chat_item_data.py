from pydantic import BaseModel, ConfigDict


class ActArchiveChatItemData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    floor: int
    chatZoneId: str
    chatDesc: str | None
    chatStoryId: str

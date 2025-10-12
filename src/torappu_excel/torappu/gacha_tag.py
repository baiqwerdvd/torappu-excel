from pydantic import BaseModel, ConfigDict


class GachaTag(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    tagId: int
    tagName: str
    tagGroup: int

from pydantic import BaseModel, ConfigDict


class RoguelikeEndingRelicDetailText(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relicId: str
    summaryEventText: str

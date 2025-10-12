from pydantic import BaseModel, ConfigDict, Field


class SpecialItemInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    showPreview: bool
    specialDesc: str
    specialBtnText: str | None = Field(default=None)

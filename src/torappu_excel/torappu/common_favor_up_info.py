from pydantic import BaseModel, ConfigDict


class CommonFavorUpInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    displayStartTime: int
    displayEndTime: int

from pydantic import BaseModel, ConfigDict


class PlayerMedalCustomLayoutItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    pos: list[int]

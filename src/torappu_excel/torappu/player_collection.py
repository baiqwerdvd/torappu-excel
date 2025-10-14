from pydantic import BaseModel, ConfigDict


class PlayerCollection(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    team: dict[str, int]

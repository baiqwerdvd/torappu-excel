from pydantic import BaseModel, ConfigDict


class CharmStatus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charms: dict[str, int]
    squad: list[str]

from pydantic import BaseModel, ConfigDict


class PlayerSkins(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    characterSkins: dict[str, int]
    skinTs: dict[str, int]
    skinSp: dict[str, bool]

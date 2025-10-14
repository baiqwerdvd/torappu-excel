from pydantic import BaseModel, ConfigDict


class PlayerEnemyHandBook(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    enemies: dict[str, int]
    stage: dict[str, list[str]]

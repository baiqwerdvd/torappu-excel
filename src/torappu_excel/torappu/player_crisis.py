from pydantic import BaseModel, ConfigDict

from .player_crisis_season import PlayerCrisisSeason
from .player_crisis_shop import PlayerCrisisShop


class PlayerCrisisMap(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rank: int
    confirmed: int


class PlayerCrisisTrainingStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    point: int


class PlayerCrisisTraining(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    currentStage: list[str]
    stage: dict[str, PlayerCrisisTrainingStage]
    nst: int


class PlayerCrisis(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    current: str
    map: dict[str, PlayerCrisisMap]
    shop: PlayerCrisisShop
    training: PlayerCrisisTraining
    season: dict[str, PlayerCrisisSeason]
    lst: int
    nst: int
    box: list["PlayerCrisis.BoxItem"]

    class BoxItem(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        type: str
        count: int

from pydantic import BaseModel, ConfigDict

from .player_building_diysolution import PlayerBuildingDIYSolution


class PlayerBuildingDormitory(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: "PlayerBuildingDormitory.Buff"
    comfort: int
    diySolution: PlayerBuildingDIYSolution
    lockQueue: list[int]

    class Buff(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        apCost: "PlayerBuildingDormitory.Buff.APCost"
        point: dict[str, int]

        class APCost(BaseModel):
            model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

            all: int
            self: dict[str, float | int]
            single: "PlayerBuildingDormitory.Buff.APCost.SingleTarget"
            exclude: dict[str, int]

            class SingleTarget(BaseModel):
                model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

                target: str | None
                value: int

from pydantic import BaseModel, ConfigDict

from .player_building_workshop_buff import PlayerBuildingWorkshopBuff


class PlayerBuildingWorkshop(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    buff: PlayerBuildingWorkshopBuff
    statistic: "PlayerBuildingWorkshop.Statistic"

    class Statistic(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        noAddition: int

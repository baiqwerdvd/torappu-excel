from pydantic import BaseModel, ConfigDict

from .player_equip_mission import PlayerEquipMission


class PlayerEquipment(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missions: dict[str, PlayerEquipMission]

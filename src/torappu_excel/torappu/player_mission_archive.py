from pydantic import BaseModel, ConfigDict

from .player_mission_archive_node_state import PlayerMissionArchiveNodeState


class PlayerMissionArchive(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    isOpen: bool
    confirmEnterReward: bool
    nodes: dict[str, PlayerMissionArchiveNodeState]

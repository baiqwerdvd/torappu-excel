from .player_mission_archive_node_state import PlayerMissionArchiveNodeState
from ..common import BaseStruct


class PlayerMissionArchive(BaseStruct):
    isOpen: bool
    confirmEnterReward: bool
    nodes: dict[str, PlayerMissionArchiveNodeState]

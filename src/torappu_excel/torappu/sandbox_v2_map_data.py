from .sandbox_v2_map_config import SandboxV2MapConfig
from .sandbox_v2_map_zone_data import SandboxV2MapZoneData
from .sandbox_v2_node_data import SandboxV2NodeData
from ..common import BaseStruct


class SandboxV2MapData(BaseStruct):
    nodes: dict[str, SandboxV2NodeData]
    zones: dict[str, SandboxV2MapZoneData]
    mapConfig: SandboxV2MapConfig
    centerNodeId: str
    monthModeNodeId: str | None

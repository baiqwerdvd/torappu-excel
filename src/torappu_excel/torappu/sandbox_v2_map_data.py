from pydantic import BaseModel, ConfigDict

from .sandbox_v2_map_config import SandboxV2MapConfig
from .sandbox_v2_map_zone_data import SandboxV2MapZoneData
from .sandbox_v2_node_data import SandboxV2NodeData


class SandboxV2MapData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodes: dict[str, SandboxV2NodeData]
    zones: dict[str, SandboxV2MapZoneData]
    mapConfig: SandboxV2MapConfig
    centerNodeId: str
    monthModeNodeId: str | None

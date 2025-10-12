from pydantic import BaseModel, ConfigDict

from .roguelike_sky_zone_node_type import RoguelikeSkyZoneNodeType


class RoguelikeSkyNodeSubTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    evtType: RoguelikeSkyZoneNodeType
    subTypeId: int
    desc: str

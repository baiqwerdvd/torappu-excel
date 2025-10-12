from pydantic import BaseModel, ConfigDict

from .roguelike_sky_zone_node_type import RoguelikeSkyZoneNodeType


class RoguelikeSkyNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    evtType: RoguelikeSkyZoneNodeType
    name: str
    iconId: str
    effId: str
    desc: str
    nameBkgClr: str
    selectClr: str
    isRepeatedly: bool

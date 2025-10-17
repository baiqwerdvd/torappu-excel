from .roguelike_sky_zone_node_type import RoguelikeSkyZoneNodeType
from ..common import BaseStruct


class RoguelikeSkyNodeData(BaseStruct):
    evtType: RoguelikeSkyZoneNodeType
    name: str
    iconId: str
    effId: str
    desc: str
    nameBkgClr: str
    selectClr: str
    isRepeatedly: bool

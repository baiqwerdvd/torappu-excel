from .roguelike_sky_zone_node_type import RoguelikeSkyZoneNodeType
from ..common import BaseStruct


class RoguelikeSkyNodeSubTypeData(BaseStruct):
    evtType: RoguelikeSkyZoneNodeType
    subTypeId: int
    desc: str

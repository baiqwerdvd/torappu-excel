from .roguelike_totem_color_type import RoguelikeTotemColorType
from .roguelike_totem_linked_node_type_data import RoguelikeTotemLinkedNodeTypeData
from .roguelike_totem_pos_type import RoguelikeTotemPosType
from ..common import BaseStruct


class RoguelikeTotemBuffData(BaseStruct):
    totemId: str
    color: RoguelikeTotemColorType
    pos: RoguelikeTotemPosType
    rhythm: str
    normalDesc: str
    synergyDesc: str
    archiveDesc: str
    combineGroupName: str
    bgIconId: str
    isManual: bool
    linkedNodeTypeData: RoguelikeTotemLinkedNodeTypeData
    distanceMin: int
    distanceMax: int
    vertPassable: bool
    expandLength: int
    onlyForVert: bool
    portalLinkedNodeTypeData: RoguelikeTotemLinkedNodeTypeData

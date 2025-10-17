from .player_node_detail_content import PlayerNodeDetailContent
from .player_node_foresight_type import PlayerNodeForesightType
from .player_node_roll_info import PlayerNodeRollInfo
from .player_roguelike_pending_event import PlayerRoguelikePendingEvent
from .roguelike_event_type import RoguelikeEventType
from .roguelike_node_line import RoguelikeNodeLine
from .roguelike_node_position import RoguelikeNodePosition
from .roguelike_shop import RoguelikeShop
from ..common import BaseStruct


class PlayerRoguelikeNode(BaseStruct):
    pos: RoguelikeNodePosition
    next: list[RoguelikeNodeLine]
    type: RoguelikeEventType
    style: int
    fts: int
    realContent: PlayerNodeDetailContent
    attach: list[str]
    shop: RoguelikeShop
    scenes: "list[PlayerRoguelikePendingEvent.SceneContent]"
    stage: str
    visibility: PlayerNodeForesightType
    refresh: PlayerNodeRollInfo

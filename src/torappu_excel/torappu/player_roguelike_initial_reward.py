from .player_roguelike_pending_event import PlayerRoguelikePendingEvent
from .roguelike_reward import RoguelikeReward
from ..common import BaseStruct


class PlayerRoguelikeInitialReward(BaseStruct):
    relic: RoguelikeReward
    scene: "PlayerRoguelikePendingEvent.SceneContent"
    recruit: RoguelikeReward

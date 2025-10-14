from pydantic import BaseModel, ConfigDict

from .roguelike_reward import RoguelikeReward

from .player_roguelike_pending_event import PlayerRoguelikePendingEvent


class PlayerRoguelikeInitialReward(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    relic: RoguelikeReward
    scene: "PlayerRoguelikePendingEvent.SceneContent"
    recruit: RoguelikeReward

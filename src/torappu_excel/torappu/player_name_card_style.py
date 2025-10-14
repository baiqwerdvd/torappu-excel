from pydantic import BaseModel, ConfigDict

from .player_name_card_misc import PlayerNameCardMisc
from .player_name_card_skin import PlayerNameCardSkin


class PlayerNameCardStyle(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    componentOrder: list[str]
    skin: PlayerNameCardSkin
    misc: PlayerNameCardMisc

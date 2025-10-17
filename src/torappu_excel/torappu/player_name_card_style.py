from .player_name_card_misc import PlayerNameCardMisc
from .player_name_card_skin import PlayerNameCardSkin
from ..common import BaseStruct


class PlayerNameCardStyle(BaseStruct):
    componentOrder: list[str]
    skin: PlayerNameCardSkin
    misc: PlayerNameCardMisc

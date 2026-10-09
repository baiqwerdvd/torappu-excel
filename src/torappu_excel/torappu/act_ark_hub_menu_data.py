from .act_ark_hub_menu_type import ActArkHubMenuType
from ..common import BaseStruct


class ActArkHubMenuData(BaseStruct):
    type: ActArkHubMenuType
    name: str
    iconId: str
    isPermanent: bool
    sortId: int
    unlockToast: str | None
    bannedToast: str | None

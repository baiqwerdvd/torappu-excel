from .act_ark_hub_name_card_state import ActArkHubNameCardState
from ..common import BaseStruct


class ActArkHubPlayerStateInfoData(BaseStruct):
    state: ActArkHubNameCardState
    iconId: str
    name: str

from .custom_ticket_type import CustomTicketType
from ..common import BaseStruct

from msgspec import field


class RoguelikeGameCustomTicketData(BaseStruct):
    id_: str = field(name="id")
    subType: CustomTicketType
    discardText: str

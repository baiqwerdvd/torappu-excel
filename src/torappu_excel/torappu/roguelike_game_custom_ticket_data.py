from .custom_ticket_type import CustomTicketType
from ..common import BaseStruct


class RoguelikeGameCustomTicketData(BaseStruct):
    id: str
    subType: CustomTicketType
    discardText: str

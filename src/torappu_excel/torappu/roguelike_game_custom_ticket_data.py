from pydantic import BaseModel, ConfigDict

from .custom_ticket_type import CustomTicketType


class RoguelikeGameCustomTicketData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    subType: CustomTicketType
    discardText: str

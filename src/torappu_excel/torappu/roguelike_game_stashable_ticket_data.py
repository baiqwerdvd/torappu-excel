from pydantic import BaseModel, ConfigDict


class RoguelikeGameStashableTicketData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ticketId: str
    stashedTicketId: str

from pydantic import BaseModel, ConfigDict


class PlayerTicketItem(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ts: int
    count: int

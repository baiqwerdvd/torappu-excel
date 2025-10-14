from pydantic import BaseModel, ConfigDict


class PlayerInviteInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    uid: str
    idx: int
    ts: int
    msg: list[str]

from pydantic import BaseModel, ConfigDict


class PlayerSquadTmpl(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skillIndex: int
    currentEquip: str

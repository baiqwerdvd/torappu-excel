from pydantic import BaseModel, ConfigDict


class Act5FunBasicNpcData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    npcId: str
    avatarId: str
    name: str

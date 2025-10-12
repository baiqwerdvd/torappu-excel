from pydantic import BaseModel, ConfigDict


class RoguelikeGameRecruitGrpData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    iconId: str
    name: str
    desc: str
    unlockDesc: str | None

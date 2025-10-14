from pydantic import BaseModel, ConfigDict


class PlayerCharSkill(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    unlock: bool
    skillId: str
    state: int
    specializeLevel: int
    completeUpgradeTime: int

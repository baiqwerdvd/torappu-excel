from pydantic import BaseModel, ConfigDict


class TowerTactical(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    PIONEER: str
    WARRIOR: str
    TANK: str
    SNIPER: str
    CASTER: str
    SUPPORT: str
    MEDIC: str
    SPECIAL: str

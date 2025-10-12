from pydantic import BaseModel, ConfigDict


class ClimbTowerCurseCardData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    towerIdList: list[str]
    name: str
    desc: str
    trapId: str

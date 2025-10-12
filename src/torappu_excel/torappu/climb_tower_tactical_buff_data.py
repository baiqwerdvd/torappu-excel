from pydantic import BaseModel, ConfigDict

from .climb_tower_tatical_buff_type import ClimbTowerTaticalBuffType


class ClimbTowerTacticalBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    desc: str
    profession: str
    isDefaultActive: bool
    sortId: int
    buffType: ClimbTowerTaticalBuffType

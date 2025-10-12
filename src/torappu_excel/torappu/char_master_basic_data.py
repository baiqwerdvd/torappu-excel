from pydantic import BaseModel, ConfigDict

from .char_master_level_data import CharMasterLevelData
from .char_master_type import CharMasterType


class CharMasterBasicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    charId: str
    masterId: str
    sortId: int
    masterType: CharMasterType
    levelList: list[CharMasterLevelData]

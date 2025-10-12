from pydantic import BaseModel, ConfigDict

from .sub_profession_data import SubProfessionData
from .uni_equip_data import UniEquipData, UniEquipDataOld
from .uni_equip_mission_data import UniEquipMissionData, UniEquipMissionDataOld
from .uni_equip_time_info import UniEquipTimeInfo
from .uni_equip_type_info import UniEquipTypeInfo


class UniEquipTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    equipDict: dict[str, UniEquipData]
    missionList: dict[str, UniEquipMissionData]
    subProfDict: dict[str, SubProfessionData]
    subProfToProfDict: dict[str, int]
    charEquip: dict[str, list[str]]
    equipTypeInfos: list[UniEquipTypeInfo]
    equipTrackDict: list[UniEquipTimeInfo]


class UniEquipTableOld(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    equipDict: dict[str, UniEquipDataOld]
    missionList: dict[str, UniEquipMissionDataOld]
    subProfDict: dict[str, SubProfessionData]
    charEquip: dict[str, list[str]]

from pydantic import BaseModel, ConfigDict, Field

from .evolve_phase import EvolvePhase
from .item_bundle import ItemBundle
from .uni_equip_type import UniEquipType


class UniEquipData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    uniEquipId: str
    uniEquipName: str
    uniEquipIcon: str
    uniEquipDesc: str
    typeIcon: str
    typeName1: str
    typeName2: str | None
    equipShiningColor: str
    showEvolvePhase: EvolvePhase
    unlockEvolvePhase: EvolvePhase
    charId: str
    tmplId: str | None
    showLevel: int
    unlockLevel: int
    missionList: list[str]
    unlockFavors: dict[str, int] | None
    itemCost: dict[str, list[ItemBundle]] | None
    type: str
    uniEquipGetTime: int
    uniEquipShowEnd: int
    charEquipOrder: int
    hasUnlockMission: bool
    isSpecialEquip: bool
    specialEquipDesc: str | None
    specialEquipColor: str | None
    charColor: str | None
    unlockFavorPoint: int | None = Field(default=None)


class UniEquipDataOld(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    uniEquipId: str
    uniEquipName: str
    uniEquipIcon: str
    uniEquipDesc: str
    typeIcon: str
    typeName: str
    showEvolvePhase: int  # FIXME: EvolvePhase
    unlockEvolvePhase: int  # FIXME: EvolvePhase
    charId: str
    tmplId: str | None
    showLevel: int
    unlockLevel: int
    unlockFavorPercent: int
    missionList: list[str]
    itemCost: list[ItemBundle] | None
    type: UniEquipType
    traitDescBundle: list["UniEquipDataOld.TraitDescBundle"]

    class TraitDescBundle(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        unlockCondition: "UniEquipDataOld.UnlockCondition"
        requiredPotentialRank: int
        overrideDescription: str | None
        additiveDescription: str

    class UnlockCondition(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        phase: int
        level: int

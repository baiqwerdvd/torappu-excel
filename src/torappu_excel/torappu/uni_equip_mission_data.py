from pydantic import BaseModel, ConfigDict


class UniEquipMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    template: str | None
    desc: str | None
    paramList: list[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str
    jumpStageId: str | None


class UniEquipMissionDataOld(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    template: str | None
    desc: str | None
    paramList: list[str]
    uniEquipMissionId: str
    uniEquipMissionSort: int
    uniEquipId: str

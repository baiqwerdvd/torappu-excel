from pydantic import BaseModel, ConfigDict


class ZoneRecordMissionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missionId: str
    recordStageId: str
    templateDesc: str
    desc: str

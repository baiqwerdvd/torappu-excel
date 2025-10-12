from pydantic import BaseModel, ConfigDict


class ActRecruitOnlyData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recruitData: "ActRecruitOnlyData.RecruitOnlyItemData"
    previewData: "ActRecruitOnlyData.RecruitOnlyItemData"

    class RecruitOnlyItemData(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        id: str
        phaseNum: int
        tagId: int
        tagTimes: int
        startTime: int
        endTime: int
        startTimeDesc: str
        endTimeDesc: str
        desc1: str
        desc2: str

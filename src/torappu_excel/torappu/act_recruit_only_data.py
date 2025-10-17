from ..common import BaseStruct


class ActRecruitOnlyData(BaseStruct):
    recruitData: "ActRecruitOnlyData.RecruitOnlyItemData"
    previewData: "ActRecruitOnlyData.RecruitOnlyItemData"

    class RecruitOnlyItemData(BaseStruct):
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

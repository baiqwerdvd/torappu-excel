from ..common import BaseStruct


class ActMainlineBpExtraData(BaseStruct):
    periodDataList: list["ActMainlineBpExtraData.ActMainlineBpExtraPeriodData"]

    class ActMainlineBpExtraPeriodData(BaseStruct):
        periodId: str
        startTs: int
        endTs: int

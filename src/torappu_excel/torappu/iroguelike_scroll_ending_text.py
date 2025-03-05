from ..common import BaseStruct


class IRoguelikeScrollEndingText(BaseStruct):
    summaryActor: str
    summaryTop: str
    summaryZone: str
    summaryEnding: str
    summaryDifficultyZone: str | None
    summaryDifficultyEnding: str | None
    summaryMode: str
    summaryGroup: str
    summarySupport: str
    summaryNormalRecruit: str
    summaryDirectRecruit: str
    summaryFriendRecruit: str
    summaryFreeRecruit: str
    summaryMonthRecruit: str
    summaryUpgrade: str
    summaryCompleteEnding: str
    summaryEachZone: str
    summaryPerfectBattle: str
    summaryMeetBattle: str
    summaryMeetEvent: str
    summaryMeetShop: str
    summaryMeetTreasure: str
    summaryBuy: str
    summaryInvest: str
    summaryGet: str
    summaryRelic: str
    summarySafeHouse: str
    summaryFailEnd: str

from .iroguelike_scroll_ending_text import IRoguelikeScrollEndingText


class RL01EndingText(IRoguelikeScrollEndingText):
    summaryVariation: str
    summaryFusion: str
    summaryCapsule: str
    summaryMeetSpZone: str | None
    summaryMeetSecretpath: str | None
    summaryExchangeRelic: str | None
    summaryMeetTrade: str | None
    summaryBuyWithPriceId: str | None
    summaryStockRecruitTicket: str | None
    summaryDuelWin: str | None
    summaryDuelTie: str | None
    summaryDuelLose: str | None
    summaryExpeditionGo: str | None
    summaryExpeditionBack: str | None
    summaryDefeatBoss: str | None = None
    summaryAccidentMeet: str | None = None
    summaryActiveTool: str | None = None

from ..common import BaseStruct


class RL02EndingText(BaseStruct):
    summaryMutation: str
    summaryDice: str
    summaryDiceResultGood: str
    summaryDiceResultNormal: str
    summaryDiceResultBad: str
    summaryDiceResultDesc: str
    summaryCommuDesc: str
    summaryHiddenDesc: str
    summaryKnightDesc: str
    summaryGoldDesc: str
    summaryPracticeDesc: str
    summaryCommuEmptyDesc: str
    summaryCommuNotEmptyDesc: str
    summaryHiddenPassedDesc: str
    summaryHiddenNotPassedDesc: str
    summaryKnightPassedDesc: str
    summaryKnightNotPassedDesc: str
    summaryGoldThreshold: int
    summaryGoldHighDesc: str
    summaryGoldLowDesc: str
    summaryPracticeThreshold: int
    summaryPracticeHighDesc: str
    summaryPracticeLowDesc: str

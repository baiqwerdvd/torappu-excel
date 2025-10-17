from ..common import BaseStruct


class PlayerRoguelikeRecord(BaseStruct):
    passedZone: int
    moveTimes: int
    battleNormalTimes: int
    battleEliteTimes: int
    battleBossTimes: int
    holdRelicCount: int
    recruitChars: int
    initialRelic: str
    totalSeconds: int
    ending: str
    isDead: bool
    totalScore: int
    unlockRelic: list[str]
    unlockMode: list[str]

from pydantic import BaseModel, ConfigDict


class PlayerRoguelikeRecord(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

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

from ..common import BaseStruct


class PlayerCrisisChallenge(BaseStruct):
    pointList: dict[str, int]
    topPoint: int
    taskList: dict[str, "PlayerCrisisChallenge.PlayerChallengeTask"]

    class PlayerChallengeTask(BaseStruct):
        fts: int
        rts: int


class PlayerCrisisPermanent(BaseStruct):
    rune: dict[str, int]
    challenge: PlayerCrisisChallenge
    point: int
    nst: int


class PlayerCrisisTemporary(BaseStruct):
    schedule: str
    challenge: PlayerCrisisChallenge
    point: int
    nst: int


class PlayerCrisisSocialInfo(BaseStruct):
    assistCnt: int
    maxPnt: str | int
    chars: list["PlayerCrisisSocialInfo.AssistChar"]
    history: dict[str, int] | None

    class AssistChar(BaseStruct):
        charId: str
        cnt: int


class PlayerCrisisSeason(BaseStruct):
    coin: int
    tCoin: int
    permanent: PlayerCrisisPermanent
    temporary: PlayerCrisisTemporary
    sInfo: PlayerCrisisSocialInfo

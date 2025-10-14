from pydantic import BaseModel, ConfigDict


class PlayerCrisisChallenge(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    pointList: dict[str, int]
    topPoint: int
    taskList: dict[str, "PlayerCrisisChallenge.PlayerChallengeTask"]

    class PlayerChallengeTask(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        fts: int
        rts: int


class PlayerCrisisPermanent(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    rune: dict[str, int]
    challenge: PlayerCrisisChallenge
    point: int
    nst: int


class PlayerCrisisTemporary(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    schedule: str
    challenge: PlayerCrisisChallenge
    point: int
    nst: int


class PlayerCrisisSocialInfo(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    assistCnt: int
    maxPnt: str | int
    chars: list["PlayerCrisisSocialInfo.AssistChar"]
    history: dict[str, int] | None

    class AssistChar(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        charId: str
        cnt: int


class PlayerCrisisSeason(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    coin: int
    tCoin: int
    permanent: PlayerCrisisPermanent
    temporary: PlayerCrisisTemporary
    sInfo: PlayerCrisisSocialInfo

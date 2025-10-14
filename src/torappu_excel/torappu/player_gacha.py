from enum import IntEnum

from pydantic import BaseModel, ConfigDict


class PlayerGacha(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    newbee: "PlayerGacha.PlayerNewbeeGachaPool"
    normal: dict[str, "PlayerGacha.PlayerGachaPool"]
    limit: dict[str, "PlayerGacha.PlayerFreeLimitGacha"]
    linkage: dict[str, dict[str, "PlayerGacha.PlayerLinkageGacha"]]
    attain: dict[str, "PlayerGacha.PlayerAttainGacha"]
    single: dict[str, "PlayerGacha.PlayerSingleGacha"]
    double: dict[str, "PlayerGacha.PlayerDoubleGacha"]
    fesClassic: dict[str, "PlayerGacha.PlayerFesClassicGacha"]
    special: dict[str, "PlayerGacha.PlayerSpecialGacha"]

    class PlayerNewbeeGachaPool(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        openFlag: bool
        cnt: int
        poolId: str

    class PlayerGachaPool(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cnt: int
        maxCnt: int
        rarity: int
        avail: bool

    class PlayerFreeLimitGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        leastFree: int
        poolCnt: int | None = None
        recruitedFreeChar: bool | None = None

    class PlayerLinkageGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        next5: bool
        next5Char: str
        must6: bool
        must6Char: str
        must6Count: int
        must6Level: int

    class PlayerAttainGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        attain6Count: int

    class PlayerSingleGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        cnt: int | None = None
        maxCnt: int | None = None
        avail: bool | None = None
        singleEnsureCnt: int
        singleEnsureUse: bool
        singleEnsureChar: str

    class PlayerDoubleGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        showCnt: int
        hitCharState: "PlayerGacha.PlayerDoubleGacha.HitCharState"
        hitCharId: str | None

        class HitCharState(IntEnum):
            NONE = 0
            FIRST = 1
            SECOND = 2

    class PlayerFesClassicGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        upChar: dict[int, list[str]]

    class PlayerSpecialGacha(BaseModel):
        model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

        upChar: dict[int, list[str]]

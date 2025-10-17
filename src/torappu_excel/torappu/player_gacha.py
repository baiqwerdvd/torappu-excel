from enum import IntEnum

from ..common import BaseStruct


class PlayerGacha(BaseStruct):
    newbee: "PlayerGacha.PlayerNewbeeGachaPool"
    normal: dict[str, "PlayerGacha.PlayerGachaPool"]
    limit: dict[str, "PlayerGacha.PlayerFreeLimitGacha"]
    linkage: dict[str, dict[str, "PlayerGacha.PlayerLinkageGacha"]]
    attain: dict[str, "PlayerGacha.PlayerAttainGacha"]
    single: dict[str, "PlayerGacha.PlayerSingleGacha"]
    double: dict[str, "PlayerGacha.PlayerDoubleGacha"]
    fesClassic: dict[str, "PlayerGacha.PlayerFesClassicGacha"]
    special: dict[str, "PlayerGacha.PlayerSpecialGacha"]

    class PlayerNewbeeGachaPool(BaseStruct):
        openFlag: int
        cnt: int
        poolId: str

    class PlayerGachaPool(BaseStruct):
        cnt: int
        maxCnt: int
        rarity: int
        avail: bool

    class PlayerFreeLimitGacha(BaseStruct):
        leastFree: int
        poolCnt: int | None = None
        recruitedFreeChar: bool | None = None

    class PlayerLinkageGacha(BaseStruct):
        next5: bool
        next5Char: str
        must6: bool
        must6Char: str
        must6Count: int
        must6Level: int

    class PlayerAttainGacha(BaseStruct):
        attain6Count: int

    class PlayerSingleGacha(BaseStruct):
        singleEnsureCnt: int
        singleEnsureUse: bool
        singleEnsureChar: str
        cnt: int | None = None
        maxCnt: int | None = None
        avail: bool | None = None

    class PlayerDoubleGacha(BaseStruct):
        showCnt: int
        hitCharState: "PlayerGacha.PlayerDoubleGacha.HitCharState"
        hitCharId: str | None

        class HitCharState(IntEnum):
            NONE = 0
            FIRST = 1
            SECOND = 2

    class PlayerFesClassicGacha(BaseStruct):
        upChar: dict[str, list[str]]

    class PlayerSpecialGacha(BaseStruct):
        upChar: dict[str, list[str]]

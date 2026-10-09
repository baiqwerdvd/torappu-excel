from ..common import CustomIntEnum


class ArkdexModeType(CustomIntEnum):
    NONE = "NONE", 0
    ARKDEX_DUEL_SINGLEROUND = "ARKDEX_DUEL_SINGLEROUND", 1
    ARKDEX_DUEL_BO3 = "ARKDEX_DUEL_BO3", 2
    ARKDEX_DUEL_4PLAYER = "ARKDEX_DUEL_4PLAYER", 3

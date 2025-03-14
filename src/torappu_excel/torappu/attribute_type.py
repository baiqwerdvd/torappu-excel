from ..common import CustomIntEnum


class AttributeType(CustomIntEnum):
    MAX_HP = "MAX_HP", 0
    ATK = "ATK", 1
    DEF = "DEF", 2
    MAGIC_RESISTANCE = "MAGIC_RESISTANCE", 3
    COST = "COST", 4
    BLOCK_CNT = "BLOCK_CNT", 5
    MOVE_SPEED = "MOVE_SPEED", 6
    ATTACK_SPEED = "ATTACK_SPEED", 7
    BASE_ATTACK_TIME = "BASE_ATTACK_TIME", 8
    RESERVED_0 = "RESERVED_0", 9
    RESERVED_1 = "RESERVED_1", 10
    RESERVED_2 = "RESERVED_2", 11
    HP_RECOVERY_PER_SEC = "HP_RECOVERY_PER_SEC", 12
    SP_RECOVERY_PER_SEC = "SP_RECOVERY_PER_SEC", 13
    ABILITY_RANGE_FORWARD_EXTEND = "ABILITY_RANGE_FORWARD_EXTEND", 14
    MAX_DEPLOY_COUNT = "MAX_DEPLOY_COUNT", 15
    DEF_PENETRATE = "DEF_PENETRATE", 16
    MAGIC_RESIST_PENETRATE = "MAGIC_RESIST_PENETRATE", 17
    HP_RECOVERY_PER_SEC_BY_MAX_HP_RATIO = "HP_RECOVERY_PER_SEC_BY_MAX_HP_RATIO", 18
    TAUNT_LEVEL = "TAUNT_LEVEL", 19
    RESPAWN_TIME = "RESPAWN_TIME", 20
    MAX_DECK_STACK_CNT = "MAX_DECK_STACK_CNT", 21
    MASS_LEVEL = "MASS_LEVEL", 22
    BASE_FORCE_LEVEL = "BASE_FORCE_LEVEL", 23
    DEF_PENETRATE_FIXED = "DEF_PENETRATE_FIXED", 24
    ONE_MINUS_STATUS_RESISTANCE = "ONE_MINUS_STATUS_RESISTANCE", 25
    MAGIC_RESIST_PENETRATE_FIXED = "MAGIC_RESIST_PENETRATE_FIXED", 26
    MAX_EP = "MAX_EP", 27
    EP_RECOVERY_PER_SEC = "EP_RECOVERY_PER_SEC", 28
    SP_RECOVER_RATIO = "SP_RECOVER_RATIO", 29
    EP_DAMAGE_RESISTANCE = "EP_DAMAGE_RESISTANCE", 30
    EP_RESISTANCE = "EP_RESISTANCE", 31
    DAMAGE_HITRATE_PHYSICAL = "DAMAGE_HITRATE_PHYSICAL", 32
    DAMAGE_HITRATE_MAGICAL = "DAMAGE_HITRATE_MAGICAL", 33
    E_NUM = "E_NUM", 34

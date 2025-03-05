from ..common import CustomIntEnum


class ProfessionCategory(CustomIntEnum):
    NONE = "NONE", 0
    WARRIOR = "WARRIOR", 1
    SNIPER = "SNIPER", 2
    TANK = "TANK", 4
    MEDIC = "MEDIC", 8
    SUPPORT = "SUPPORT", 16
    CASTER = "CASTER", 32
    SPECIAL = "SPECIAL", 64
    TOKEN = "TOKEN", 128
    TRAP = "TRAP", 256
    PIONEER = "PIONEER", 512

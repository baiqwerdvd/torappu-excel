from ..common import BaseStruct, CustomIntEnum


class BattleVoiceOption(BaseStruct):
    class BattleVoiceType(CustomIntEnum):
        BATTLE_START = "BATTLE_START", 0
        ENCOUNTER_ENEMY = "ENCOUNTER_ENEMY", 1
        PLACE_CHAR = "PLACE_CHAR", 2
        FOCUS_CHAR = "FOCUS_CHAR", 3
        SKILL_ACTIVE = "SKILL_ACTIVE", 4
        SKILL_PASSIVE_IMP = "SKILL_PASSIVE_IMP", 5
        SKILL_PASSIVE_NOR = "SKILL_PASSIVE_NOR", 6
        NORMAL_ATTACK = "NORMAL_ATTACK", 7
        E_NUM = "E_NUM", 8

    voiceType: "BattleVoiceOption.BattleVoiceType"
    priority: int
    overlapIfSamePriority: bool
    cooldown: float
    delay: float

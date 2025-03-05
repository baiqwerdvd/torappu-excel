from .battle_voice_option import BattleVoiceOption
from ..common import BaseStruct


class BattleVoiceData(BaseStruct):
    crossfade: float
    minTimeDeltaForEnemyEncounter: float
    minSpCostForImportantPassiveSkill: int
    voiceTypeOptions: list[BattleVoiceOption]

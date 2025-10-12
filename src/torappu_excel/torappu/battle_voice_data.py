from pydantic import BaseModel, ConfigDict

from .battle_voice_option import BattleVoiceOption


class BattleVoiceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    crossfade: float
    minTimeDeltaForEnemyEncounter: float
    minSpCostForImportantPassiveSkill: int
    voiceTypeOptions: list[BattleVoiceOption]

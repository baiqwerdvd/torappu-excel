from pydantic import BaseModel, ConfigDict

from .mission_calc_state import MissionCalcState


class PlayerHiddenStage(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    missions: list[MissionCalcState]
    unlock: int

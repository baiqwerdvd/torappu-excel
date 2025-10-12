from pydantic import BaseModel, ConfigDict

from .act_main_sszone_addition_data import ActMainSSZoneAdditionData


class ActMainSSData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    zoneAdditionDataMap: dict[str, ActMainSSZoneAdditionData]

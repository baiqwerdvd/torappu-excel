from pydantic import BaseModel, ConfigDict


class PlayerBuildingWorkshopStatus(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    bonus: dict[str, list[int]]
    bonusActive: int | None

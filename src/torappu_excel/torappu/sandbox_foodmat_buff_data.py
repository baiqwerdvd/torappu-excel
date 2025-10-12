from pydantic import BaseModel, ConfigDict

from .sandbox_food_mat_type import SandboxFoodMatType


class SandboxFoodmatBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    buffId: str | None
    buffDesc: str | None
    matType: SandboxFoodMatType
    sortId: int

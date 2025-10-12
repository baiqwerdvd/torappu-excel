from pydantic import BaseModel, ConfigDict, Field

from .sandbox_v2_food_attribute import SandboxV2FoodAttribute
from .sandbox_v2_food_mat_type import SandboxV2FoodMatType
from .sandbox_v2_food_variant_type import SandboxV2FoodVariantType


class SandboxV2FoodMatData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    type: SandboxV2FoodMatType
    sortId: int
    variantType: SandboxV2FoodVariantType
    bonusDuration: int
    buffDesc: str | None = Field(default=None)
    attribute: SandboxV2FoodAttribute | None = Field(default=None)

from pydantic import BaseModel, ConfigDict

from .sandbox_v2_food_variant_type import SandboxV2FoodVariantType


class SandboxV2FoodVariantData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    type: SandboxV2FoodVariantType
    name: str
    usage: str

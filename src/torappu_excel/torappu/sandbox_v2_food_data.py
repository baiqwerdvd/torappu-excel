from pydantic import BaseModel, ConfigDict, Field

from .sandbox_v2_food_attribute import SandboxV2FoodAttribute
from .sandbox_v2_food_recipe_data import SandboxV2FoodRecipeData
from .sandbox_v2_food_variant_data import SandboxV2FoodVariantData


class SandboxV2FoodData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    id: str
    attributes: list[SandboxV2FoodAttribute]
    duration: int
    sortId: int
    variants: list[SandboxV2FoodVariantData]
    itemName: str | None = Field(default=None)
    itemUsage: str | None = Field(default=None)
    recipes: list[SandboxV2FoodRecipeData] | None = Field(default=None)
    generalName: str | None = Field(default=None)
    enhancedName: str | None = Field(default=None)
    enhancedUsage: str | None = Field(default=None)

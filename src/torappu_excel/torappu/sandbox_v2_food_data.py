from .sandbox_v2_food_attribute import SandboxV2FoodAttribute
from .sandbox_v2_food_recipe_data import SandboxV2FoodRecipeData
from .sandbox_v2_food_variant_data import SandboxV2FoodVariantData
from ..common import BaseStruct

from msgspec import field


class SandboxV2FoodData(BaseStruct):
    id_: str = field(name="id")
    attributes: list[SandboxV2FoodAttribute]
    duration: int
    sortId: int
    variants: list[SandboxV2FoodVariantData]
    itemName: str | None = field(default=None)
    itemUsage: str | None = field(default=None)
    recipes: list[SandboxV2FoodRecipeData] | None = field(default=None)
    generalName: str | None = field(default=None)
    enhancedName: str | None = field(default=None)
    enhancedUsage: str | None = field(default=None)

from ..common import BaseStruct


class SandboxV2FoodRecipeData(BaseStruct):
    foodId: str
    mats: list[str]

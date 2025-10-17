from .sandbox_v2_alchemy_material_data import SandboxV2AlchemyMaterialData
from ..common import BaseStruct


class SandboxV2AlchemyRecipeData(BaseStruct):
    recipeId: str
    materials: list[SandboxV2AlchemyMaterialData]
    itemId: str
    onceAlchemyRatio: int
    recipeLevel: int
    unlockDesc: str

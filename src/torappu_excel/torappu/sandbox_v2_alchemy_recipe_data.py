from pydantic import BaseModel, ConfigDict

from .sandbox_v2_alchemy_material_data import SandboxV2AlchemyMaterialData


class SandboxV2AlchemyRecipeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    recipeId: str
    materials: list[SandboxV2AlchemyMaterialData]
    itemId: str
    onceAlchemyRatio: int
    recipeLevel: int
    unlockDesc: str

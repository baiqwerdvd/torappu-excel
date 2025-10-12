from pydantic import BaseModel, ConfigDict


class SandboxV2FoodRecipeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    foodId: str
    mats: list[str]

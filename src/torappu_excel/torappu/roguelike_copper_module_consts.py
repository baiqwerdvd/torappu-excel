from pydantic import BaseModel, ConfigDict


class RoguelikeCopperModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    copperDrawMaxNum: int
    copperDrawMinNum: int

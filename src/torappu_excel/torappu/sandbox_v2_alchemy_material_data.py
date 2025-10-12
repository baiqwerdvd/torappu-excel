from pydantic import BaseModel, ConfigDict


class SandboxV2AlchemyMaterialData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    count: int

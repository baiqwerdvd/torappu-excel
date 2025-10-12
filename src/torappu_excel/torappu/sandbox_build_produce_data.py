from pydantic import BaseModel, ConfigDict


class SandboxBuildProduceData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemProduceId: str
    itemId: str
    itemTypeText: str
    materialItems: dict[str, int]

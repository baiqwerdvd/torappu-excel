from pydantic import BaseModel, ConfigDict


class SandboxV2CraftGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    items: list[str]

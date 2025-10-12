from pydantic import BaseModel, ConfigDict


class SandboxV2NodeBuffData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    runeId: str
    name: str
    description: str
    extra: str
    iconId: str

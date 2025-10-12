from pydantic import BaseModel, ConfigDict


class RoguelikeCandleModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    candleHolderBuffId: str

from pydantic import BaseModel, ConfigDict


class RoguelikeChaosModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    maxChaosLevel: int
    maxChaosSlot: int
    chaosNotMaxDescription: str
    chaosMaxDescription: str
    chaosPredictDescription: str

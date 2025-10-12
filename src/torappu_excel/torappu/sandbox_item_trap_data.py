from pydantic import BaseModel, ConfigDict


class SandboxItemTrapData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    itemId: str
    trapId: str
    trapPhase: int
    trapLevel: int
    skillIndex: int
    skillLevel: int

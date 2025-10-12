from pydantic import BaseModel, ConfigDict


class SpecialOperatorDetailSkillNodeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    nodeId: str
    skillKey: str
    skillLevel: int
    skillSpLevel: int

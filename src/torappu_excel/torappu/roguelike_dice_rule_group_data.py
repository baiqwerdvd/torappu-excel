from pydantic import BaseModel, ConfigDict


class RoguelikeDiceRuleGroupData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    ruleGroupId: str
    minGoodNum: int

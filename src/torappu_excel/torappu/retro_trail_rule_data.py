from pydantic import BaseModel, ConfigDict


class RetroTrailRuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    title: list[str]
    desc: list[str]

from pydantic import BaseModel, ConfigDict


class RoguelikeBattleSummeryDescriptionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    randomDescriptionList: list[str]

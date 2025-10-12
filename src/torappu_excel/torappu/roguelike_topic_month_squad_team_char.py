from pydantic import BaseModel, ConfigDict


class RoguelikeTopicMonthSquadTeamChar(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    teamCharId: str
    teamTmplId: str | None

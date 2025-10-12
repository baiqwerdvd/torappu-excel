from pydantic import BaseModel, ConfigDict


class TermDescriptionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    termId: str
    termName: str
    description: str

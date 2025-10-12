from pydantic import BaseModel, ConfigDict


class MailArchiveConstData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    funcOpenTs: int

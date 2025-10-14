from pydantic import BaseModel, ConfigDict


class DateTime(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    pass

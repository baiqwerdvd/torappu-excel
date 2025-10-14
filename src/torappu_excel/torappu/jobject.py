from pydantic import BaseModel, ConfigDict


class JObject(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    base64: str

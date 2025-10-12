from pydantic import BaseModel, ConfigDict


class RoguelikeZoneVariationData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    pass

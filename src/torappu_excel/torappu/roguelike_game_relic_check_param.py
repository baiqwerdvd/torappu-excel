from pydantic import BaseModel, ConfigDict

from .profession_category import ProfessionCategory


class RoguelikeGameRelicCheckParam(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    valueProfessionMask: ProfessionCategory | int
    valueStrs: list[str] | None
    valueInt: int

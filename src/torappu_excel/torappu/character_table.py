from pydantic import BaseModel, ConfigDict

from .character_data import CharacterData


class CharacterTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    chars: dict[str, CharacterData]

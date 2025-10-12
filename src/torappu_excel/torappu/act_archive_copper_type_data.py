from pydantic import BaseModel, ConfigDict

from .roguelike_copper_type import RoguelikeCopperType


class ActArchiveCopperTypeData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    copperType: RoguelikeCopperType
    typeName: str
    typeIconId: str

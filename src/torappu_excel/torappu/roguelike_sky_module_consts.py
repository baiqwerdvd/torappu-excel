from pydantic import BaseModel, ConfigDict


class RoguelikeSkyModuleConsts(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    skyApItemId: str
    skyMaxColumns: int
    skySacrificeChoiceDynamicKey: str

from pydantic import BaseModel, ConfigDict


class SubProfessionData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    subProfessionId: str
    subProfessionName: str
    subProfessionCatagory: int

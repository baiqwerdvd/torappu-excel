from pydantic import BaseModel, ConfigDict


class PlayerFormulaUnlockRecord(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    shop: dict[str, int]
    manufacture: dict[str, int]
    workshop: dict[str, int]

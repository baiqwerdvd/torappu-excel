from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class PotentialMaterialConverterConfig(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    items: dict[str, ItemBundle]

from pydantic import BaseModel, ConfigDict

from .item_bundle import ItemBundle


class ReplicateData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    item: ItemBundle
    replicateTokenItem: ItemBundle

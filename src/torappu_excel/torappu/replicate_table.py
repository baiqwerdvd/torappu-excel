from pydantic import BaseModel, ConfigDict

from .replicate_data import ReplicateData


class ReplicateTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    replicateList: list[ReplicateData]

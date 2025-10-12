from pydantic import BaseModel, ConfigDict

from .act_archive_component_data import ActArchiveComponentData


class ActArchiveComponentTable(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    components: dict[str, ActArchiveComponentData]

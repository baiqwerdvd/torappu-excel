from pydantic import BaseModel, ConfigDict

from .act_archive_fragment_item_data import ActArchiveFragmentItemData


class ActArchiveFragmentData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    fragment: dict[str, ActArchiveFragmentItemData]

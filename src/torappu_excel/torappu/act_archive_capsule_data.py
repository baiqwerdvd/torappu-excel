from pydantic import BaseModel, ConfigDict

from .act_archive_capsule_item_data import ActArchiveCapsuleItemData


class ActArchiveCapsuleData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    capsule: dict[str, ActArchiveCapsuleItemData]

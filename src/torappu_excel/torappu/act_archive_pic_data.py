from pydantic import BaseModel, ConfigDict

from .act_archive_pic_item_data import ActArchivePicItemData


class ActArchivePicData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    pics: dict[str, ActArchivePicItemData]

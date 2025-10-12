from pydantic import BaseModel, ConfigDict

from .act_multi_v3_block_dir_type import ActMultiV3BlockDirType
from .act_multi_v3_block_type import ActMultiV3BlockType


class ActMultiV3SailBoatBlockInfoData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    blockId: str
    blockLevelId: str
    startDirType: ActMultiV3BlockDirType
    endDirType: ActMultiV3BlockDirType
    blockType: ActMultiV3BlockType

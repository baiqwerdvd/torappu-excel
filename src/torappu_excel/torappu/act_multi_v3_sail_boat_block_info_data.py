from .act_multi_v3_block_dir_type import ActMultiV3BlockDirType
from .act_multi_v3_block_type import ActMultiV3BlockType
from ..common import BaseStruct


class ActMultiV3SailBoatBlockInfoData(BaseStruct):
    blockId: str
    blockLevelId: str
    startDirType: ActMultiV3BlockDirType
    endDirType: ActMultiV3BlockDirType
    blockType: ActMultiV3BlockType

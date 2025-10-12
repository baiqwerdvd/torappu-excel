from pydantic import BaseModel, ConfigDict

from .act_multi_v3_block_dir_type import ActMultiV3BlockDirType


class ActMultiV3SailBoatBlockPoolData(BaseModel):
    model_config: ConfigDict = ConfigDict(extra="forbid")  # pyright: ignore[reportIncompatibleVariableOverride]

    blockPool: str
    blockId: str
    startDirType: ActMultiV3BlockDirType
    endDirType: ActMultiV3BlockDirType
    weight: int

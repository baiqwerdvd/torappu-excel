from ..common import BaseStruct


class SandboxV2RiftDifficultyData(BaseStruct):
    id: str
    riftId: str
    desc: str
    difficultyLevel: int
    rewardGroupId: str

from .sandbox_v2_challenge_const import SandboxV2ChallengeConst
from .sandbox_v2_challenge_mode_difficulty_data import SandboxV2ChallengeModeDifficultyData
from .sandbox_v2_challenge_mode_reward_data import SandboxV2ChallengeModeRewardData
from .sandbox_v2_challenge_mode_unlock_data import SandboxV2ChallengeModeUnlockData
from ..common import BaseStruct


class SandboxV2ChallengeModeData(BaseStruct):
    challengeConst: SandboxV2ChallengeConst
    challengeModeUnlockData: dict[str, SandboxV2ChallengeModeUnlockData]
    challengeModeRewardData: dict[str, SandboxV2ChallengeModeRewardData]
    challengeModeDifficultyData: list[SandboxV2ChallengeModeDifficultyData]
